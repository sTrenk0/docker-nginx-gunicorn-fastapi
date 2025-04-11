let ws = null;

function callWs() {
  const output = document.getElementById("output-websocket");

  if (ws && ws.readyState === WebSocket.OPEN) {
    output.textContent += "WebSocket is already connected. Sending...\n";
    ws.send("Hello!");
    return;
  }

  output.textContent = "Connecting to WebSocket...\n";

  ws = new WebSocket("ws://" + location.host + "/ws/");

  ws.onopen = () => {
    output.textContent += "The connection is established.\n";
    ws.send("Hello!");
  };

  ws.onmessage = (event) => {
    output.textContent += "Received: " + event.data + "\n";
  };

  ws.onerror = () => {
    output.textContent += "A WebSocket error has occurred.\n";
  };

  ws.onclose = () => {
    output.textContent += "The connection is closed.\n";
    ws = null;
  };
}


function callApi() {
  fetch('/api/')
    .then(res => res.json())
    .then(data => {
      document.getElementById('output-rest-api').textContent += '\n' + JSON.stringify(data, null, 2);
    });
}