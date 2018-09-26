const menuBtn = document.querySelector('.nav-btn');
const mainNav = document.querySelector('.main-nav');

menuBtn.addEventListener('click', toggleMenu);

function toggleMenu() {
  mainNav.classList.toggle('hidden');
  menuBtn.classList.toggle('close');
}

// inputArea.keypress(function(event) {
//   if (event.which == 13) {
//     event.preventDefault();
//       var s = $(this).val();
//       $(this).val(s+"\n");
//   }
// });

// const inputArea = document.querySelectorAll('input');

// function skipLine(event){
//   if (event.keyCode === 13) {
//     const s = this.value;
//     this.value = s+"\n";
//     event.preventDefault();
//   }
// }

// for (var i=0; i<inputArea.length; i++) {
//   inputArea[i].addEventListener('keypress', skipLine);
// }

