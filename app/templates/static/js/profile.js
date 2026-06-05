const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "/login";
}

async function loadProfile() {

    try {

        const response = await fetch(
            "/users/me",
            {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            }
        );

        const data = await response.json();

        document.getElementById("username").innerText =
            data.username;

        document.getElementById("email").innerText =
            data.email;

    } catch (error) {

        console.log(error);

        alert("Failed to load profile");
    }
}

function logout() {

    localStorage.removeItem("token");

    window.location.href = "/login";
}

function goDashboard() {

    window.location.href = "/dashboard";
}

loadProfile();