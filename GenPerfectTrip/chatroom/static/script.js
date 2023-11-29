
$(document).ready(function() {
    $("#generate").click(function(event) {
        event.preventDefault()
        var textareaValue = $("#user_input").val();
        $.ajax({
            url: "/generate",
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken")
            },
            data: {
                user_input: textareaValue
            },
            success: function(response) {
                console.log(response.data)
                $("#output").val(response.data);

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
