#include <WiFi.h>

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA); // Set device to station mode
  delay(1000);         // Let things stabilize

  // Retrieve and print the MAC address
  String macAddress = WiFi.macAddress();
  Serial.print("ESP32 MAC Address: ");
  Serial.println(macAddress);
}

void loop() {
  // Nothing needed here
}
