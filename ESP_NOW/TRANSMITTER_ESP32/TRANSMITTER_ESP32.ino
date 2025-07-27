#include <WiFi.h>
#include <esp_now.h>

#define POT_PIN 15  // Choose one from [15, 2, 4, 5, 18, 19, 21]

typedef struct struct_message {
  int potValue;
} struct_message;

struct_message myData;

// Replace with your receiver's MAC address
uint8_t receiverAddress[] = {0xC4, 0xD8, 0xD5, 0x96, 0x17, 0x1C};//C4:D8:D5:96:17:1C

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("Packet send status: ");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Success" : "Failure");
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);  // Set device as a Wi-Fi Station

  if (esp_now_init() != ESP_OK) {
    Serial.println("ESP-NOW initialization failed");
    return;
  }
  esp_now_register_send_cb(OnDataSent);

  // Register peer information
  esp_now_peer_info_t peerInfo;
  memcpy(peerInfo.peer_addr, receiverAddress, 6);
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;

  if (esp_now_add_peer(&peerInfo) != ESP_OK) {
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {
  // Read the potentiometer value (typically a range of 0-4095)
  myData.potValue = analogRead(POT_PIN);
  Serial.print("Pot value: ");
  Serial.println(myData.potValue);

  // Transmit the pot value via ESP-NOW
  esp_err_t result = esp_now_send(receiverAddress, (uint8_t *)&myData, sizeof(myData));
  if (result != ESP_OK) {
    Serial.println("Error sending data");
  }
  delay(100);  // Adjust the interval as needed
}
