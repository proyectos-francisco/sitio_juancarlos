const menuBtn = document.querySelector('.nav-btn');
const mainNav = document.querySelector('.main-nav');

menuBtn.addEventListener('click', toggleMenu);

function toggleMenu() {
  mainNav.classList.toggle('hidden');
  menuBtn.classList.toggle('close');
}