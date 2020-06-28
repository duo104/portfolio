const modal = document.querySelector(".modal");
const imgs = document.querySelectorAll(".gallery img");
const original = document.querySelector(".full-img");
const caption = document.querySelector(".caption");

imgs.forEach((img) => {
  img.addEventListener("click", () => {
    modal.classList.add("open");
    const originalSrc = img.getAttribute("data-original");
    original.src = "./img/" + originalSrc
    console.log(originalSrc)
    const altText = img.alt;
    caption.textContent = altText;
  });
});

modal.addEventListener("click", (e) => {
  if (e.target.classList.contains("modal")) {
    modal.classList.remove("open")
  }
});