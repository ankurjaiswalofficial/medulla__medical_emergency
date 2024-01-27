$(document).ready(function() {
    $("#loadContentBtn").click(function() {
      // AJAX request
      $.ajax({
        url: "ambulancelist.php", // Replace with the actual URL of your page
        type: "GET",
        success: function(response) {
          // Update the content of the div with the loaded page
          $("#contentDiv").html(response);
        },
        error: function(xhr, status, error) {
          console.error("Error loading page:", error);
        }
      });
    });
  });
