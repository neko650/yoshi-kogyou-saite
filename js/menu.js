
document.addEventListener("DOMContentLoaded", () => {
  const menu = document.querySelector(".nav-menu");
  const hamburger = document.querySelector(".hamburger");
  hamburger.addEventListener("click", () => {
    menu.classList.toggle("active");
  });

  const fadeIns = document.querySelectorAll(".fade-in, .gallery-item");
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  });
  fadeIns.forEach(el => observer.observe(el));
});
