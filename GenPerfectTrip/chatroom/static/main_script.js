
$(document).ready(function() {

    $("#generate").click(function(event) {
        event.preventDefault()
        $("#output").text("");
        $("#new-output").text("");
        $("#loading-box").fadeIn();
        var textareaValue = $("#user_input").val();
        $.ajax({
            url: "generate",
            type: "GET",
            data: {
                user_input: textareaValue
            },
            success: function(response) {
                $("#output").text(response.data);
                $("#improve").fadeIn()
                $("#output").fadeIn()
                $("#loading-box").fadeOut()
            }
        });
    });
    $("#improve").click(function(event) {
        event.preventDefault()
        $("#loading-box").fadeIn()
        var textareaValue = $("#user_input").val();
        var original_plan = $("#output").val();
        $.ajax({
            url: "improve",
            type: "GET",
            data: {
                user_input: textareaValue,
                original_plan: original_plan
            },
            success: function(response) {
                $("#new_output").text(response.data);
                $("#new_output").fadeIn()
                $("#loading-box").fadeOut()
            }
        });
    });
});
