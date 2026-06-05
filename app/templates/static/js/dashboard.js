console.log("Dashboard Loaded 🚀");

const sendButton =
    document.querySelector(".message-box button");

const messageInput =
    document.querySelector(".message-box input");

const chatArea =
    document.querySelector(".chat-area");

sendButton.addEventListener("click", () => {

    const text =
        messageInput.value.trim();

    if (text === "")
        return;

    const message =
        document.createElement("div");

    message.classList.add(
        "message",
        "sent"
    );

    message.textContent = text;

    chatArea.appendChild(message);

    messageInput.value = "";

    chatArea.scrollTop =
        chatArea.scrollHeight;
});

messageInput.addEventListener(
    "keypress",
    (e) => {

        if (e.key === "Enter") {

            sendButton.click();
        }
    }
);