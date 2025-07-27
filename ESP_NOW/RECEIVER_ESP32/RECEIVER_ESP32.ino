#include <WiFi.h>
#include <esp_now.h>
#include <Servo.h>
// mac address C4:D8:D5:96:17:1C
#define SERVO_PIN 27

Servo myServo;

typedef struct struct_message {
  int potValue;
} struct_message;

struct_message receivedData;

void OnDataRecv(const uint8_t * mac, const uint8_t *incomingData, int len) {
  memcpy(&receivedData, incomingData, sizeof(receivedData));
  Serial.print("Received Pot Value: ");
  Serial.println(receivedData.potValue);

  // Map the analog reading (0-4095) to servo angle (0-180)
  int angle = map(receivedData.potValue, 0, 4095, 0, 180);
  myServo.write(angle);
  Serial.print("Servo angle set to: ");
  Serial.println(angle);
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);  // Setting device to Wi-Fi station mode
  myServo.attach(SERVO_PIN);

  if (esp_now_init() != ESP_OK) {
    Serial.println("ESP-NOW initialization failed");
    return;
  }
  esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
  // No tasks required in loop as ESP-NOW handles reception asynchronously.
}
