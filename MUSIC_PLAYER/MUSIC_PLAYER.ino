#include <SoftwareSerial.h>
#include <DFRobotDFPlayerMini.h>

const int joyX = A0;  // Joystick X-axis pin
const int joyY = A1;  // Joystick Y-axis pin
const int joyBtn = 2; // Joystick button pin

SoftwareSerial mp3Serial(10, 9); // RX, TX to DFPlayer Mini
DFRobotDFPlayerMini mp3;

bool buttonPressed = false;
unsigned long lastActionTime = 0;
const unsigned long debounceDelay = 500;
bool isPlaying = true;

void setup() {
  Serial.begin(9600);
  mp3Serial.begin(9600);
  pinMode(joyBtn, INPUT_PULLUP);

  delay(2000);
  if (!mp3.begin(mp3Serial)) {
    Serial.println("\n DFPlayer not found 😢");
    while (true);
  }
  Serial.println("DFPlayer Mini ready 🎶");

  mp3.volume(25); // Set initial volume (0–30)
  mp3.play(1);    // Start with track 1
}

void loop() {
  int x = analogRead(joyX);
  int y = analogRead(joyY);
  bool btn = digitalRead(joyBtn) == LOW;

  String dir = getDirection(x, y);

  if (btn && !buttonPressed && millis() - lastActionTime > debounceDelay) {
    buttonPressed = true;
    lastActionTime = millis();

    if (dir == "Forward") {
      mp3.volumeUp();
      Serial.println("🔊 Volume Up");
    } 
    else if (dir == "Down") {
      mp3.volumeDown();
      Serial.println("🔉 Volume Down");
    } 
    else if (dir == "Right") {
      mp3.next();
      Serial.println("⏭️ Next Track");
      isPlaying = true;
    } 
    else if (dir == "Left") {
      mp3.previous();
      Serial.println("⏮️ Previous Track");
      isPlaying = true;
    } 
    else if (dir == "Center") {
      if (isPlaying) {
        mp3.pause();
        Serial.println("⏸️ Paused");
      } else {
        mp3.start();
        Serial.println("▶️ Playing");
      }
      isPlaying = !isPlaying;
    }
  }

  if (!btn) {
    buttonPressed = false;
  }

  // Auto-play next song if the current one ends
  if (mp3.available()) {
    uint8_t type = mp3.readType();
    if (type == DFPlayerPlayFinished) {
      Serial.println("✅ Track finished. Playing next...");
      mp3.next();
      isPlaying = true;
    }
  }
}

String getDirection(int x, int y) {
  // ML-style joystick zone classification
  if (x >= 250 && x <= 700 && y >= 400 && y <= 512)
    return "Center";
  else if (x >= 410 && x <= 490 && y >= 370 && y <= 445)
    return "Forward";
  else if (x >= 390 && x <= 470 && y >= 445 && y <= 470)
    return "Down";
  else if (x >= 800)
    return "Right";
  else if (x <= 100)
    return "Left";
  else
    return "Unknown";
}
