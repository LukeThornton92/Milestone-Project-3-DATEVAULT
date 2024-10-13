function confirmDeletion(event) {
  if (
    !confirm(
      "Are you sure you want to delete this date? This action cannot be undone."
    )
  ) {
    event.preventDefault();
  }
}

function confirmLogOut(event) {
  if (!confirm("Are you sure you want to Logout?")) {
    event.preventDefault();
  }
}

// Hides filters in pick_a_date:

document.addEventListener("DOMContentLoaded", function () {
  var randomDateCard = document.getElementById("random-date");
  if (randomDateCard) {
    var filterForm = document.getElementById("filter-form");
    filterForm.style.display = "none"; // Hide the filter form
  }
});

function reloadPage() {
  location.reload();
}
