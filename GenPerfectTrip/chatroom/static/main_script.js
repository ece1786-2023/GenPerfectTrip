
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
            type: "POST",
            data: {
                user_input: textareaValue,
                original_plan: original_plan
            },
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            success: function(response) {
                $("#new_output").text(response.data);
                $("#new_output").fadeIn()
                $("#loading-box").fadeOut()
            }
        });
    });
    // Function to get the CSRF token from cookies
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
            var cookies = document.cookie.split(";");
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Search for the CSRF cookie by name
                if (cookie.substring(0, name.length + 1) === name + "=") {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
