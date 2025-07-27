void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("Triple Touch Light Using ESP32");
  pinMode(33, OUTPUT);
  pinMode(34, OUTPUT);
  pinMode(26, OUTPUT);
}

void loop() {                                                   
  // put your main code here, to run repeatedly:
  if(touchRead(27) < 40){
    Serial.print("Value1: ");
    Serial.print(touchRead(27));
    Serial.println("RED LIGHT ON");
    Serial.println("  ");
    digitalWrite(33, HIGH);

  }else if(touchRead(14) < 40){
    Serial.print("Value2: ");
    Serial.print(touchRead(14));
    Serial.println("GREEN LIGHT ON");
    Serial.println("  ");
    digitalWrite(34, HIGH);

  }else if(touchRead(13) < 40){
    Serial.print("Value3: ");
    Serial.print(touchRead(13));
    Serial.println("BLUE LIGHT ON");
    Serial.println("  ");
    digitalWrite(26, HIGH);

  }else{
    Serial.print("Value1: ");
    Serial.println(touchRead(27));
    digitalWrite(33, LOW);
    Serial.print("Value2: ");
    Serial.println(touchRead(14));
    digitalWrite(25, LOW);
    Serial.print("Value3: ");
    Serial.println(touchRead(13));
    digitalWrite(26, LOW);
    Serial.println("ALL LIGHTS OFF");
  }
}