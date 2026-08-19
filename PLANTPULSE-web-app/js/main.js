let menu = document.querySelector("#menu-btn");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  menu.classList.toggle("fa-times");
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  menu.classList.remove("fa-times");
  navbar.classList.remove("active");
};

document.addEventListener('DOMContentLoaded', function() {
  const menuBtn = document.getElementById('left-menu-btn');
  const menu = document.getElementById('left-menu');
  const page = document.getElementById('page');
  const whole = document.getElementById('whole');

  menuBtn.addEventListener('click', function() {
    menu.classList.toggle('show');
    page.classList.toggle('move-right');
    whole.classList.toggle('move-right');
    menuBtn.classList.toggle('disable');
  });

  document.addEventListener('click', function(event) {
    if (!menu.contains(event.target) && !menuBtn.contains(event.target)) {
      menu.classList.remove('show');
      page.classList.remove('move-right');
      whole.classList.remove('move-right');
      menuBtn.classList.remove('disable');
    }
  });
});

const scrollButton = document.getElementById('scrollButton');

    window.addEventListener('scroll', () => {
      if (window.scrollY > 500) {
        scrollButton.classList.add('visible');
      } else {
        scrollButton.classList.remove('visible');
      }
    });



    