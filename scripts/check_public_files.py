"""Reject common private app artifacts from the public website's Git history."""
from pathlib import PurePosixPath
import subprocess
import sys

PRIVATE_DIRECTORIES = {'.aws', '.ssh', '.gnupg', 'node_modules', 'private', 'secrets'}
PRIVATE_NAMES = {
    'google-services.json', 'googleservice-info.plist', 'credentials.json',
    'service-account.json', 'serviceaccount.json', 'key.properties',
    'keystore.properties', 'id_rsa', 'id_ed25519', '.npmrc', '.pypirc',
}
PRIVATE_EXTENSIONS = {
    '.arc2liv', '.db', '.sqlite', '.sqlite3', '.sql', '.pem', '.key', '.p12',
    '.pfx', '.jks', '.keystore', '.apk', '.aab', '.ipa', '.log',
}


def forbidden(name):
    path = PurePosixPath(name.lower())
    return (
        bool(set(path.parts) & PRIVATE_DIRECTORIES)
        or path.name in PRIVATE_NAMES
        or path.name == '.env'
        or path.name.startswith('.env.')
        or path.suffix in PRIVATE_EXTENSIONS
        or 'service-account' in path.name
        or 'service_account' in path.name
    )


def git_paths():
    paths = set(subprocess.check_output(['git', 'ls-files', '-z']).split(b'\0'))
    commits = subprocess.check_output(['git', 'rev-list', 'HEAD']).splitlines()
    for commit in commits:
        paths.update(subprocess.check_output([
            'git', 'diff-tree', '--root', '--no-commit-id', '--name-only',
            '-r', '-z', commit.decode('ascii'),
        ]).split(b'\0'))
    return {p.decode('utf-8', errors='replace') for p in paths if p}


def main():
    blocked = sorted(name for name in git_paths() if forbidden(name))
    if blocked:
        # Do not print file contents or sensitive filenames into public logs.
        print(f'FAILED: {len(blocked)} private app artifact path(s) found in Git history.')
        print('Remove private artifacts before publishing; inspect paths locally using this script.')
        return 1
    print('PASS: no prohibited private app artifact paths found in Git history.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
