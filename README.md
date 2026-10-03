# Arc2Liv public pages

Application home page, privacy, terms of service, and support information for **Arc2Liv: AI Goal Planner**.

Hosted on **Cloudflare Pages** at [arc2liv.pages.dev](https://arc2liv.pages.dev/).

- [Application Home](https://arc2liv.pages.dev/)
- [Privacy Policy](https://arc2liv.pages.dev/privacy/)
- [Support](https://arc2liv.pages.dev/support/)
- [Terms of Service](https://arc2liv.pages.dev/terms/)

## Public repository safety

This repository is for public website content. Do not commit credentials, API keys, signing keys, app backups, databases, private app data, or build artifacts. Review screenshots manually for personal information before uploading them.

The **Public repository safety** workflow runs on pull requests and pushes to `main`. It checks Git history for prohibited app artifacts and uses Gitleaks to detect secrets. The workflow uses read-only permissions and does not upload secret reports or post findings in PR comments. Automated scans cannot identify every sensitive detail, especially text inside images. A PR check runs after a branch is uploaded; it does not prevent initial disclosure in a public repository.

GitHub secret scanning and push protection are enabled. Keep push protection enabled to block supported secret types before upload. If a real secret is exposed, revoke or rotate it immediately; deleting the file does not remove it from Git history.

### Require PRs instead of direct pushes

In **Settings → Rules → Rulesets → New ruleset → New branch ruleset**:

1. Name it `Protect main`, set enforcement to **Active**, and target the default branch (`main`).
2. Leave the bypass list empty so administrators also follow the rule.
3. Enable **Require a pull request before merging**. If a second trusted reviewer is available, require one approval and dismiss stale approvals. A sole maintainer should use zero required approvals because authors cannot approve their own PRs.
4. Enable **Require status checks to pass**, select **Public repository safety** from GitHub Actions, and require branches to be up to date. The check becomes selectable after its first run.
5. Enable **Block force pushes**, **Restrict deletions**, and **Require conversation resolution before merging**.
6. Save the ruleset.

This blocks direct updates to `main`, while allowing work on other branches and merging passing PRs. Do not enable **Restrict updates** with an empty bypass list: that would also block PR merges. Administrators can still edit or disable rulesets; limit repository admin access to trusted maintainers.

For permissions, use **Settings → Collaborators** to remove unwanted access or grant read access instead of write/admin. For an organization-owned repository, use **Collaborators and teams**. Keep the default GitHub Actions workflow token permissions read-only and grant additional permissions only when needed.

References: [GitHub ruleset rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets), [Gitleaks Action](https://github.com/gitleaks/gitleaks-action).
