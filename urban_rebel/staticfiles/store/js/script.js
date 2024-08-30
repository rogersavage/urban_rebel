// script.js
document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  function showNextSlide() {
    let prevSlide = currentSlide;
    currentSlide = (currentSlide + 1) % slides.length;
    slides[prevSlide].classList.add("fading");
    slides[prevSlide].classList.remove("active");
    slides[currentSlide].classList.remove("fading");
    slides[currentSlide].classList.add("active");
  }

  slides[currentSlide].classList.add("active");

  setInterval(showNextSlide, 6000);
});

document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".card");

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry, index) => {
      if (entry.isIntersecting) {
        setTimeout(
          () => {
            entry.target.style.transform = "translateX(0)";
            entry.target.style.opacity = "1";
            observer.unobserve(entry.target);
          },
          (index % 4) * 200,
        );
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
  const site_container = document.querySelector(".site-container");
  const site_container_rect = site_container.getBoundingClientRect();

  hamburger.addEventListener("click", function () {
    dropdown.classList.toggle("show");
    console.log(site_container_rect.x);
    // dropdown.style.left = `${site_container_rect.x}px`;
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const close_button = document.getElementById("dropdown-close");
  const menu = document.getElementById("hamburger-menu");

  close_button.addEventListener("click", function () {
    menu.classList.toggle("show");
  });
});

document.addEventListener("DOMContentLoaded", function () {
  const siteContainer = document.querySelector(".site-container");
  const dropdownMenu = document.getElementById("hamburger-menu");

  function updateMenuPosition() {
    const containerRect = siteContainer.getBoundingClientRect();
    dropdownMenu.style.left = `${containerRect.left}px`;
  }

  updateMenuPosition();

  window.addEventListener("resize", updateMenuPosition);
});
