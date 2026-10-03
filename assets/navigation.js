// Native details provides keyboard and touch support without JavaScript.
// Enhance it with outside-click, Escape, and selection dismissal.
document.querySelectorAll('.home-dropdown').forEach((dropdown) => {
  document.addEventListener('click', (event) => {
    if (!dropdown.contains(event.target)) dropdown.open = false;
  });
  dropdown.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && dropdown.open) {
      dropdown.open = false;
      dropdown.querySelector('summary').focus();
    }
  });
  dropdown.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => { dropdown.open = false; });
  });
});
