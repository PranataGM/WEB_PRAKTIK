document.addEventListener("DOMContentLoaded", function () {
  const slides = document.querySelectorAll(".slideshow .slide");
  let currentIndex = 0;

  setInterval(() => {
    slides[currentIndex].classList.remove("active");
    currentIndex = (currentIndex + 1) % slides.length;
    slides[currentIndex].classList.add("active");
  }, 4000);
});

function confirmDelete(id) {
    const deleteModal = new bootstrap.Modal(document.getElementById('deleteConfirmationModal'));
    const deleteButton = document.getElementById('deleteBeritaBtn');
    deleteButton.href = `/admin/delete/${id}`;
    deleteModal.show();
}
