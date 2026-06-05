console.log("Settings Page Loaded ⚙️");

/* Buttons */

const editBtn =
    document.querySelectorAll("button")[0];

const passwordBtn =
    document.querySelectorAll("button")[1];

const logoutBtn =
    document.querySelector(".logout-btn");

/* Profile Settings */

if (editBtn) {

    editBtn.addEventListener(
        "click",
        () => {

            alert(
                "Profile Settings feature coming soon 🚀"
            );

        }
    );
}

/* Change Password */

if (passwordBtn) {

    passwordBtn.addEventListener(
        "click",
        () => {

            alert(
                "Change Password feature coming soon 🔐"
            );

        }
    );
}

/* Notification Toggle */

const notificationToggle =
    document.querySelectorAll(
        ".switch input"
    )[0];

if (notificationToggle) {

    notificationToggle.addEventListener(
        "change",
        () => {

            if (notificationToggle.checked) {

                console.log(
                    "Notifications Enabled 🔔"
                );

            } else {

                console.log(
                    "Notifications Disabled 🔕"
                );
            }
        }
    );
}

/* Dark Mode Toggle */

const darkModeToggle =
    document.querySelectorAll(
        ".switch input"
    )[1];

if (darkModeToggle) {

    darkModeToggle.addEventListener(
        "change",
        () => {

            if (darkModeToggle.checked) {

                console.log(
                    "Dark Mode Enabled 🌙"
                );

            } else {

                console.log(
                    "Dark Mode Disabled ☀️"
                );
            }
        }
    );
}

/* Logout */

if (logoutBtn) {

    logoutBtn.addEventListener(
        "click",
        () => {

            const confirmLogout =
                confirm(
                    "Are you sure you want to logout?"
                );

            if (confirmLogout) {

                alert(
                    "Logout Successful 👋"
                );

            }
        }
    );
}