console.log("Signup.js Loaded")
document
    .getElementById("signupForm")
    .addEventListener("submit", function (e) {

        e.preventDefault();
        console.log("Button Clicked")

        window.location.href = "/otp";

    });