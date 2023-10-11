document.addEventListener("DOMContentLoaded", function () {
  const usernameLabel = document.getElementById("usernameLabel");
  const passwordLabel = document.getElementById("passwordLabel");

  const editButton = document.querySelector(".button-edit");

  editButton.addEventListener("mouseenter", () => {
    // usernameLabel.classList.add("hovered");
    // passwordLabel.classList.add("hovered");
  });

  editButton.addEventListener("mouseleave", () => {
    // usernameLabel.classList.remove("hovered");
    // passwordLabel.classList.remove("hovered");
  });
});
