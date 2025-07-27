// RFID DOOR LOCK SYSTEM //
// Before uploading the code you have to install the nessary libraries 
// Servo Library https://www.arduino.cc/reference/en/libraries/servo/ version (1.2.2)
// RFID library https://github.com/miguelbalboa/rfid version (1.4.11)
// Written by Chirrenthen 

#include <Servo.h>                       // Including Servo library
#include <SPI.h>                         // Including SPI communication protocol library
#include <MFRC522.h>                     // Including RFID library

#define Buzzer 3                         // Creating a variable for buzzer (pin 3)
#define Button 4                         // Creating a variable for servo (pin 4)

long duration;                           // Creating variable for duration
int distance;                            // Creating variable for distance
int servopin = 2;                        // Creating a variable for servo (pin 2)
const int Trig = 5;                      // Creating a variable for Ultrasonic Trig (pin 5)
const int Echo = 6;                      // Creating a variable for Ultrasonic Echo (pin 6)                                           

#define RST_PIN 9                        // Creating a variable for RFID RST pin (pin 9)
#define SS_PIN 10                        // Creating a variable for RFID SS pin (pin 10)

String UID1 = "F3 A0 8D FC";             // Registering card1 UID
String UID2 = "3 34 55 F5";              // Registering card2 UID
byte lock = 0;                             

Servo Servo;                             // Declaring the  servo
MFRC522 rfid(SS_PIN, RST_PIN);           // RFID properties

void setup() {
  Serial.begin(11500);                   // Declaring baud rate in Serial Monitor
  Servo.attach(servopin);                // Assigning servo pin 
  Servo.write(70);                       // Assigning servo position
  delay(750);                            // Delay for 750 milliseconds
  pinMode(Echo, INPUT);                  // Declaring Echo pin as input
  pinMode(Button,INPUT);                 // Declaring Button variable as input
  pinMode(Trig, OUTPUT);                 // Declaring Trig variable as output
  pinMode(Buzzer,OUTPUT);                // Declaring Buzzer variable as output
  tone(Buzzer,500,100);
  SPI.begin();                           // Starting SPI communication
  rfid.PCD_Init();                       // Initializing RFID reader
 }

void loop() {

  if ( ! rfid.PICC_IsNewCardPresent())    // Checking for RFID cards
    return;                               // Return fuction
  if ( ! rfid.PICC_ReadCardSerial())      // Reading the RFID card serial
    return;                               // Return function

// For reading card serial
  Serial.print("Reading card Serial \n");                          
  String ID = "";                                                 
  for (byte i = 0; i < rfid.uid.size; i++) {
    ID.concat(String(rfid.uid.uidByte[i] < 0x10 ? " 0" : " "));
    ID.concat(String(rfid.uid.uidByte[i], HEX));
    delay(300);
  }
  ID.toUpperCase();

  digitalWrite(Trig, LOW);                 // Providing 0 volts to Trig pin
  delayMicroseconds(2);                    // Delay of 2 microseconds
  digitalWrite(Trig, HIGH);                // Providing 5 volts to Trig pin
  delayMicroseconds(10);                   // Delay of 10 microseconds
  digitalWrite(Trig, LOW);                 // Providing 0 vlots to Trig pin
  duration = pulseIn(Echo, HIGH);          // Defining duration and reading the time taken to receive ultrasound
  distance = duration * 0.034 / 2;         // Calculating distance 'Distance = Speed*time' -> "Distance = Speed of sound / 2" 
  return distance;

  if (ID.substring(1) == UID1 && lock == 0 ) {
    Serial.print("Card placed, Locking.. \n");
    Servo.write(70);
    Serial.print(" Lock Closed \n");
    tone(Buzzer,1000,150);
    delay(1500);
    lock = 1;
  }
 else if (ID.substring(1) == UID1 && lock == 1 ) {
    Serial.print("Card placed, Opening.. \n");
    Servo.write(160);
    Serial.print(" Lock Opened \n");
    tone(Buzzer,500,100);
    delay(5000);
    Servo.write(70);
    Serial.print("Lock Closed \n");
    tone(Buzzer,1000,150);
    delay(1500);
    lock = 0;
}
  else if (ID.substring(1) == UID2 && lock == 0 ) {
    Serial.print("Card placed, Locking.. \n");
    Servo.write(70);
    Serial.print("Lock Closed \n");
    tone(Buzzer,1000,150);
    delay(1500);
    lock = 1;
}
  else if (ID.substring(1) == UID2 && lock == 1 ) {
    Serial.print(" Card placed, Opening.. \n");
    Servo.write(160);
    Serial.print("Lock Opened \n");
    tone(Buzzer,500,100);
    delay(5000);
    Servo.write(70);
    Serial.print(" Lock Closed \n");
    tone(Buzzer,1000,150);
    delay(1500);
    lock = 0;
}
  else if (distance <= 5) {
   Serial.print("Hand placed! \n");
   Servo.write(160);
   Serial.print(" Lock Opened! \n");
   tone(Buzzer,500,100);
   delay(5000);
   Servo.write(70);
   Serial.print("Lock Closed \n");
   tone(Buzzer,1000,150);
   delay(1500);
}
  else if(digitalRead(Button) == HIGH) {
   Serial.print("Button pressed! \n");
   Servo.write(160);
   Serial.print("Lock Opened \n");
   tone(Buzzer,500,100);
   delay(5000);
   Serial.print("Lock Closed \n");
   tone(Buzzer,1000,150);
   delay(1500);
}
  else {
   Servo.write(70);
}
 }