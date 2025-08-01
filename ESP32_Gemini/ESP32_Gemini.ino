#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "Airtel_pkum_0262";
const char* password = "air47250";
const char* Gemini_Token = "AIzaSyCwJrvi0RjLMdG2OYf8iEFRJ2X4gsbArAM";
const char* Gemini_Max_Tokens = "150";
String res = "";

void rapidblink(){
digitalWrite(LED_BUILTIN,HIGH);
delay(300);
digitalWrite(LED_BUILTIN,LOW);
delay(300);
}

void setup() {
  Serial.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.disconnect();


  while (!Serial);
  pinMode(LED_BUILTIN,OUTPUT);

  // wait for WiFi connection
  WiFi.begin(ssid, password);
  Serial.print("Connecting to ");
  Serial.println(ssid);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
    rapidblink();
  }
  digitalWrite(LED_BUILTIN,HIGH);
  Serial.println("connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  delay(500);
  digitalWrite(LED_BUILTIN,LOW);
}

void loop() 
{
  Serial.println("");
  Serial.println("Ask your Question: ");
  while (!Serial.available());
  while (Serial.available()) {
    char add = Serial.read();
    res = res + add;
    delay(1);
  }
  int len = res.length();
  res = res.substring(0, (len - 1));
  res = "\"" + res + "\"";
  Serial.println("");
  Serial.print("Asking Your Question : ");
  Serial.println(res);

  HTTPClient https;

  //Serial.print("[HTTPS] begin...\n");
  if (https.begin("https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + (String)Gemini_Token)) {  // HTTPS

    https.addHeader("Content-Type", "application/json");
    String payload = String("{\"contents\": [{\"parts\":[{\"text\":" + res + "}]}],\"generationConfig\": {\"maxOutputTokens\": " + (String)Gemini_Max_Tokens + "}}");

    //Serial.print("[HTTPS] GET...\n");

    // start connection and send HTTP header
    int httpCode = https.POST(payload);

    // httpCode will be negative on error
    // file found at server

    if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
      String payload = https.getString();
      //Serial.println(payload);

      DynamicJsonDocument doc(1024);


      deserializeJson(doc, payload);
      String Answer = doc["candidates"][0]["content"]["parts"][0]["text"];


      // Note: use this only if you want a filtered character
      // For Filtering our Special Characters, WhiteSpaces and NewLine Characters
     // Answer.trim();
      // String filteredAnswer = "";
      //for (size_t i = 0; i < Answer.length(); i++) {
      //  char c = Answer[i];
      //  if (isalnum(c) || isspace(c)) {
       //   filteredAnswer += c;
      //  } else {
      //    filteredAnswer += ' ';
      //  }
      //}
      //Answer = filteredAnswer;


      Serial.println("");
      Serial.println("Here is your Answer: ");
      Serial.println("");
      Serial.println(Answer);
    } else {
      Serial.printf("[HTTPS] GET... failed, error: %s\n", https.errorToString(httpCode).c_str());
    }
    https.end();
  } else {
    Serial.printf("[HTTPS] Unable to connect\n");
  }
  res = "";
}