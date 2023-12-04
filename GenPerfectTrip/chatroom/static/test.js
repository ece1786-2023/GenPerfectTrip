
$(document).ready(function() {

    $("#test-generate").click(function(event) {
        event.preventDefault()
        $("#output").text("");
        $("#new-output").text("");
        $("#loading-box").fadeIn()
        var textareaValue = $("#user_input").val();
        $.ajax({
            url: "test_generate",
            type: "GET",
            data: {
                user_input: textareaValue
            },
            success: function(response) {
                console.log(response.data)
                $("#output").text(response.data);
                $("#test-improve").fadeIn()
                $("#output").fadeIn()
                $("#loading-box").fadeOut()
            }
        });
    });
    $("#test-improve").click(function(event) {
        event.preventDefault()
        $("#loading-box").fadeIn()
        var textareaValue = $("#user_input").val();
        var original_plan = $("#output").val();
        $.ajax({
            url: "test_improve",
            type: "GET",
            data: {
                user_input: textareaValue,
                original_plan: original_plan
            },
            success: function(response) {
                $("#new_output").text(response.data);
                $("#new_output").fadeIn()
                $("#loading-box").fadeOut()
            }cd
        });
    });
});
