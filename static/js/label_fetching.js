$.ajax({
    headers: {"X-CSRFToken": token}, //new item added here the csrf token
   url: `${window.location.origin}/example/`, //url changed to be dynamic for all base origins
   type: "POST",
   data: JSON.stringify(param),
   success: function () {
    alert("Success");
       },
   error: function(error) {
       console.log("error: " + error);
       }
  });