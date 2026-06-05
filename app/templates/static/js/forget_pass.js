document
    .getElementById("forgotForm")
    .addEventListener("submit", function (e) {

        e.preventDefault();

        alert(
            "Recovery email sent successfully."
        );

        window.location.href =
            "/login";

    });