$(document).ready(function () {
    $("#id_password1").keyup(function (event) {
        if ($(this).val().length < 8) {
            $(this).css("border", "2px solid red")
        } else if (/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/.test($(this).val())) {
            $(this).css("border", "2px solid green")
        } else {
            $(this).css("border", "2px solid yellow")

        }
    });

    $("#id_password2").keyup(function (event) {
        if ($(this).val() == $("#id_password1").val()) {
            $(this).css("border", "2px solid green");
        }
    });

    $("#id_password2")on("myEvent", function() {
    	alert("HAHAHAHA!")
    });

    // $("#id_password2").trigger("myEvent");
});