$(document).ready(function() {

   $("#ajax_load").click(function(event) {
       $.ajax($(this).attr("href"), {
           method: "get",
           success: function(data) {
               $("#ajax_place").append(data);
           }
       });
       event.preventDefault();
   });

   $("#ajax_place").on("click", ".ajax_result", function() {
       $(this).fadeOut()
   });

});


// Замыкания:

var func = function(a ,b) {
    var c = a / b;

    return function() {
        console.log(c)

    }
};

var object = func(10, 5);

object();