const ws = new WebSocket("ws://localhost:8888/ws");

const textarea = document.getElementById("editor");
const preview = document.getElementById("preview");

ws.onmessage = (event) => {
    const data = JSON.parse(event.data);

    if (data.type === "init" || data.type === "update") {
        textarea.value = data.content;
        preview.innerHTML = marked.parse(data.content);
    }
};

textarea.addEventListener("input", () => {
    ws.send(JSON.stringify({
        type: "update",
        content: textarea.value
    }));
});