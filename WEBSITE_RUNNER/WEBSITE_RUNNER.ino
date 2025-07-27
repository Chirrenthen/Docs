#include <WiFi.h>
#include <WebServer.h>

const char* ssid = "Ramesh Gopal";
const char* password = "9894704796";

WebServer server(80);
String chatHistory = "";
const char* loginPassword = "deepseek123";  // Staff password

bool isLoggedIn = false;

const char* loginPage = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial, sans-serif; background: #f5f7fa; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
        input[type="password"] { width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 20px; border: 1px solid #ccc; }
        input[type="submit"] { width: 100%; padding: 10px; background: #1a73e8; color: white; border: none; border-radius: 20px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="login-box">
        <h2>Login</h2>
        <form action="/login" method="POST">
            <input type="password" name="password" placeholder="Enter password" required>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
)rawliteral";

const char* htmlContent = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
    <title>Server Messager | Chirrenthen</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #f5f7fa; margin: 0; padding: 0; }
        .container { max-width: 600px; margin: 40px auto; background: white; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); padding: 20px; }
        h1 { color: #1a73e8; text-align: center; }
        #chat {
            border: 1px solid #ddd;
            padding: 10px;
            height: 400px;
            overflow-y: scroll;
            margin-bottom: 10px;
            border-radius: 4px;
            background: #fafafa;
            display: flex;
            flex-direction: column;
        }
        .msg {
            margin: 8px 0;
            padding: 8px 12px;
            border-radius: 20px;
            max-width: 80%;
            word-wrap: break-word;
        }
        .web {
            background: #e8f0fe;
            align-self: flex-end;
            text-align: right;
        }
        .serial {
            background: #d1e7dd;
            align-self: flex-start;
            text-align: left;
        }
        form { display: flex; gap: 10px; margin-top: 10px; }
        input[type="text"] { flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 20px; }
        input[type="submit"] { background: #1a73e8; color: white; border: none; padding: 10px 20px; border-radius: 20px; cursor: pointer; }
        input[type="submit"]:hover { background: #155ab6; }
        .top-buttons { display: flex; justify-content: space-between; margin-bottom: 10px; }
        button { padding: 8px 16px; border: none; border-radius: 20px; cursor: pointer; }
        .logout { background: #e53935; color: white; }
        .clear { background: #fbc02d; color: white; }
    </style>
    <script>
        function fetchChat() {
            fetch('/get').then(response => response.text()).then(data => {
                document.getElementById('chat').innerHTML = data;
                document.getElementById('chat').scrollTop = document.getElementById('chat').scrollHeight;
            });
        }
        setInterval(fetchChat, 1000);
        window.onload = fetchChat;
    </script>
</head>
<body>
    <div class="container">
        <h1>Messages</h1>
        <div class="top-buttons">
            <button class="logout" onclick="location.href='/logout'">Logout</button>
            <button class="clear" onclick="location.href='/clear'">Clear Chat</button>
        </div>
        <div id="chat"></div>
        <form action="/message" method="POST">
            <input type="text" name="message" placeholder="Type your message">
            <input type="submit" value="Send">
        </form>
    </div>
</body>
</html>
)rawliteral";

void handleRoot() {
    if (isLoggedIn) {
        server.send(200, "text/html", htmlContent);
    } else {
        server.send(200, "text/html", loginPage);
    }
}

void handleLogin() {
    if (server.method() == HTTP_POST) {
        String pass = server.arg("password");
        if (pass == loginPassword) {
            isLoggedIn = true;
            server.sendHeader("Location", "/");
            server.send(303);
        } else {
            server.send(200, "text/html", "<h2>Wrong Password!</h2><a href='/'>Try Again</a>");
        }
    }
}

void handleLogout() {
    isLoggedIn = false;
    server.sendHeader("Location", "/");
    server.send(303);
}

void handleGetChat() {
    if (isLoggedIn) {
        server.send(200, "text/html", chatHistory);
    } else {
        server.sendHeader("Location", "/");
        server.send(303);
    }
}

void handleClearChat() {
    if (isLoggedIn) {
        chatHistory = "";
        server.sendHeader("Location", "/");
        server.send(303);
    }
}

void handleMessage() {
    if (!isLoggedIn) {
        server.sendHeader("Location", "/");
        server.send(303);
        return;
    }
    if (server.method() == HTTP_POST) {
        String message = server.arg("message");
        if (message.length() > 0) {
            chatHistory += "<div class='msg web'>" + message + "</div><br>";
            Serial.println("User: " + message);
            limitChatMemory();
        }
    }
    server.sendHeader("Location", "/");
    server.send(303);
}

void limitChatMemory() {
    if (chatHistory.length() > 3000) {
        chatHistory = chatHistory.substring(chatHistory.length() - 2000);
    }
}

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);
    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nConnected! Server URL:");
    Serial.println("http://" + WiFi.localIP().toString());

    server.on("/", handleRoot);
    server.on("/login", handleLogin);
    server.on("/logout", handleLogout);
    server.on("/get", handleGetChat);
    server.on("/clear", handleClearChat);
    server.on("/message", handleMessage);
    server.begin();
}

void loop() {
    server.handleClient();

    if (Serial.available() > 0) {
        String serialInput = Serial.readStringUntil('\n');
        serialInput.trim();
        if (serialInput.length() > 0) {
            chatHistory += "<div class='msg serial'>" + serialInput + "</div><br>";
            Serial.println("You: " + serialInput);
            limitChatMemory();
        }
    }
}