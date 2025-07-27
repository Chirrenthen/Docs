#include <Keypad.h>
#include <SoftwareSerial.h>

#define A9G_RX 10
#define A9G_TX 11
#define BUZZER_PIN 12  // Pin for the buzzer

SoftwareSerial a9gSerial(A9G_RX, A9G_TX);

enum State { IDLE, TYPING, DIALING, INCOMING, IN_CALL };
State callState = IDLE;

const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};
byte rowPins[ROWS] = {9, 8, 7, 6};
byte colPins[COLS] = {5, 4, 3, 2};

Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

String number = "";
int volumeLevel = 5;

void setup() {
  Serial.begin(9600);
  a9gSerial.begin(9600);
  pinMode(BUZZER_PIN, OUTPUT);
  delay(2000);
  a9gSerial.println("AT");
  Serial.println("Telephone Ready.");
}

void loop() {
  checkA9GResponse(); // 👂 Listen to A9G

  char key = keypad.getKey();
  if (key) {
    handleKeypadInput(key);
  }
}

void handleKeypadInput(char key) {
  switch (key) {
    case 'C':
      if (callState == IDLE) {
        number = "";
        callState = TYPING;
        Serial.println("Enter number:");
      }
      break;

    case 'B':
      if (callState == TYPING && number.length() > 0) {
        Serial.println("Dialing: " + number);
        a9gSerial.print("ATD");
        a9gSerial.print(number);
        a9gSerial.println(";");
        callState = DIALING;
        number = "";
      }
      break;

    case 'A':
      if (callState == INCOMING) {
        Serial.println("Answering Call...");
        a9gSerial.println("ATA");
        callState = IN_CALL;
        noTone(BUZZER_PIN); // Stop ringtone when call is answered
      }
      break;

    case 'D':
      if (callState == INCOMING || callState == IN_CALL || callState == DIALING) {
        Serial.println("Ending Call...");
        a9gSerial.println("ATH");
        callState = IDLE;
        noTone(BUZZER_PIN); // Stop ringtone when call is declined
      }
      break;

    case '*':
      if (volumeLevel > 0) volumeLevel--;
      setVolume(volumeLevel);
      Serial.println("Volume ↓ → " + String(volumeLevel));
      break;

    case '#':
      if (volumeLevel < 10) volumeLevel++;
      setVolume(volumeLevel);
      Serial.println("Volume ↑ → " + String(volumeLevel));
      break;

    default:
      if (callState == TYPING && isDigit(key)) {
        number += key;
        Serial.println("Number: " + number);
      }
      break;
  }
}

void checkA9GResponse() {
  if (a9gSerial.available()) {
    String response = a9gSerial.readStringUntil('\n');
    response.trim();
    if (response.length() > 0) {
      Serial.println("A9G: " + response);
      if (response == "RING") {
        callState = INCOMING;
        Serial.println("📞 Incoming Call! Press A to answer, D to decline.");
        playSmoothTrrTrr(); // Play ringtone
      }
      if (response.startsWith("+CLIP:")) {
        Serial.println("📇 Caller ID: " + response);
      }
      if (response.indexOf("NO CARRIER") >= 0 || response.indexOf("BUSY") >= 0) {
        Serial.println("Call ended.");
        callState = IDLE;
        noTone(BUZZER_PIN); // Stop ringtone if call ends
      }
    }
  }
}

void playSmoothTrrTrr() {
  for (int i = 0; i < 2; i++) {
    tone(BUZZER_PIN, 650);  // Soft, low tone
    delay(400);             // Duration of each "trr"
    noTone(BUZZER_PIN);     
    delay(120);             // Gap between pulses
  }
}

void setVolume(int level) {
  level = constrain(level, 0, 10);
  a9gSerial.print("AT+CLVL=");
  a9gSerial.println(level);
}
