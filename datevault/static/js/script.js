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
