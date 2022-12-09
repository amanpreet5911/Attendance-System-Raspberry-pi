window.addEventListener("DOMContentLoaded", (event) => {
  // Toggle the side navigation
  const sidebarToggle = document.body.querySelector("#sidebarToggle");
  if (sidebarToggle) {
    // Uncomment Below to persist sidebar toggle between refreshes
    if (localStorage.getItem("sb|sidebar-toggle") === "true") {
      document.body.classList.toggle("sb-sidenav-toggled");
    }
    sidebarToggle.addEventListener("click", (event) => {
      event.preventDefault();
      document.body.classList.toggle("sb-sidenav-toggled");
      localStorage.setItem(
        "sb|sidebar-toggle",
        document.body.classList.contains("sb-sidenav-toggled")
      );
    });
  }
});

// $(document).ready(function () {
//   $('#dtHorizontalVerticalExample').DataTable({
//     "scrollX": true,
//     "scrollY": 200,
//   });
//   $('.dataTables_length').addClass('bs-select');
// });

// const deleteMethod = () => {
//   let url = delbutton.value;
//   let options = {
//     method: "DELETE",
//   };
//   fetch(url, options).then(function (response) {
//     alert("Employee deleted successfully");
//   });

//   delbutton.addEventListener("click", function (event) {
//     event.preventDefault();
//     deleteMethod();
//   });
// };

$(".delbutton").on("click", function (e) {
    e.preventDefault();
    url = $(this).attr("data-url");
    console.log(url)

    $.ajax({
      type: "DELETE",
      url: url,
      success: function (response) {
            console.log(response)
          }
    });
  });