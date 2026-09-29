const html = document.documentElement;
const themeBtn = document.getElementById("themeBtn");
const menuBtn = document.getElementById("menuBtn");
const navLinks = document.getElementById("navLinks");

const savedTheme = localStorage.getItem("theme");
if (savedTheme) html.dataset.theme = savedTheme;

function updateThemeIcon() {
  themeBtn.textContent = html.dataset.theme === "light" ? "☾" : "☼";
}
updateThemeIcon();

themeBtn.addEventListener("click", () => {
  html.dataset.theme = html.dataset.theme === "light" ? "dark" : "light";
  localStorage.setItem("theme", html.dataset.theme);
  updateThemeIcon();
});

menuBtn.addEventListener("click", () => {
  const open = navLinks.classList.toggle("open");
  menuBtn.setAttribute("aria-expanded", open);
});

document.querySelectorAll("#navLinks a").forEach(a => {
  a.addEventListener("click", () => navLinks.classList.remove("open"));
});

const progress = document.querySelector(".progress");
window.addEventListener("scroll", () => {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  progress.style.width = `${max ? (window.scrollY / max) * 100 : 0}%`;
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(".reveal").forEach(el => observer.observe(el));
