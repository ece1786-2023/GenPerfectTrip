
$(document).ready(function() {

    $("#hotels-generate").click(function(event) {
        event.preventDefault()
        $("#output").text("");
        $("#new-output").text("");
        $("#loading-box").fadeIn()
        var textareaValue = $("#user_input").val();
        $.ajax({
            url: "hotels_generate",
            type: "GET",
            data: {
                user_input: textareaValue
            },
            success: function(response) {
                console.log(response)
                $("#output").text(response.data);
                $("#hotels-improve").fadeIn()
                $("#output").fadeIn()
                $("#loading-box").fadeOut()
            }
        });
    });
    $("#hotels-improve").click(function(event) {
        event.preventDefault()
        $("#loading-box").fadeIn()
        var textareaValue = $("#user_input").val();
        $.ajax({
            url: "hotels_improve",
            type: "GET",
            data: {
                user_input: textareaValue
            },
            success: function(response) {
                console.log(response)
                $("#new_output").text(response.data);
                $("#new_output").fadeIn()
                $("#loading-box").fadeOut()
            }
        });
    });
});
