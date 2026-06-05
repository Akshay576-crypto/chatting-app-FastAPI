const socket = new WebSocket(
    "ws://127.0.0.1:8000/ws"
);

const messagesDiv =
    document.getElementById("messages");

socket.onmessage = function (event) {

    const messageElement =
        document.createElement("div");

    messageElement.classList.add("message");

    messageElement.textContent =
        event.data;

    messagesDiv.appendChild(
        messageElement
    );

    messagesDiv.scrollTop =
        messagesDiv.scrollHeight;
};

function sendMessage() {

    const input =
        document.getElementById(
            "messageInput"
        );

    const message =
        input.value.trim();

    if (message === "") {
        return;
    }

    socket.send(message);

    input.value = "";
}