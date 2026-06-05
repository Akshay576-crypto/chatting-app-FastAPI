const inputs =
    document.querySelectorAll(".otp-boxes input");

inputs.forEach((input, index) => {

    input.addEventListener("input", () => {

        if (
            input.value.length === 1 &&
            index < inputs.length - 1
        ) {
            inputs[index + 1].focus();
        }

    });

});

let time = 60;

const timer =
    document.getElementById("timer");

setInterval(() => {

    if (time > 0) {

        time--;

        timer.textContent = time;
    }

}, 1000);

document
    .getElementById("otpForm")
    .addEventListener("submit", function (e) {

        e.preventDefault();

        window.location.href =
            "/login";

    });