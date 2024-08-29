// script.js
document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  function showNextSlide() {
    let prevSlide = currentSlide - 1;
    if (prevSlide == -1) prevSlide = slides.length - 1;
    slides[prevSlide].classList.remove("fading");
    slides[currentSlide].classList.remove("active");
    slides[currentSlide].classList.add("fading");
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].classList.add("active");
    const img = slides[currentSlide];
    img.offsetHeight;
  }

  slides[currentSlide].classList.add("active");
  slides[slides.length - 1].classList.add("fading");

  setInterval(showNextSlide, 5000);
});

document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".card");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(() => {
          entry.target.style.transform = "translateX(0)";
          entry.target.style.opacity = "1";
          observer.unobserve(entry.target);
        }, index * 300);
      }
    });
  });

  cards.forEach((card) => {
    observer.observe(card);
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const hamburger = document.getElementById("hamburger");
  const dropdown = document.getElementById("hamburger-menu");

  hamburger.addEventListener("click", function () {
    dropdown.classList.toggle("show");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const close_button = document.getElementById("dropdown-close");
  const menu = document.getElementById("hamburger-menu");

  close_button.addEventListener("click", function () {
    menu.classList.toggle("show");
  });
});
