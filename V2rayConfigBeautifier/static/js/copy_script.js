const copyButtons = [...document.querySelectorAll('.copy-button')];
copyButtons.forEach(button => {
  button.addEventListener('click', () => {
    const copyTarget = document.querySelector(`#${button.dataset.copyTarget}`);
    copyTarget.select();
    document.execCommand('copy');
    alert('config copied to clipboard!');
  });
});