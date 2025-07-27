#include <DHT.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>

// ------------------- Pin Definitions -------------------
#define DHTPIN 2           // Digital pin for DHT11
#define DHTTYPE DHT11      // Type of DHT sensor DHT11 or DHT22
#define MQ2PIN A0          // Analog pin for MQ2 gas sensor
#define VIBRATIONPIN 3     // Digital pin for Vibration sensor
#define RAINPIN A1         // Analog pin for Raindrop sensor

// ------------------- Sensor Initialization -------------------
DHT dht(DHTPIN, DHTTYPE);
Adafruit_BMP280 bmp;

// ------------------- Setup -------------------
void setup() {
  Serial.begin(9600);
  dht.begin();
  
  if (!bmp.begin(0x76)) { // Use 0x76 or 0x77 depending on your BMP280 address
    Serial.println("BMP280 not detected. Check wiring.");
    while (1);
  }

  pinMode(VIBRATIONPIN, INPUT);
  Serial.println("🌦️ AIO Weather Station Initialized...");
  delay(1000);
}

// ------------------- Main Loop -------------------
void loop() {
  // DHT11 Readings
  float temp = dht.readTemperature();
  float hum = dht.readHumidity();

  // BMP280 Readings
  float pressure = bmp.readPressure() / 100.0F; // Convert to hPa

 // Altitude
  float altitude = bmp.readAltitude(1013.25);

  // MQ2 Reading
  int gasValue = analogRead(MQ2PIN);

  // Vibration Detection
  bool vibrationDetected = digitalRead(VIBRATIONPIN);

  // Raindrop Sensor
  int rainValue = analogRead(RAINPIN);
  bool isRaining = rainValue < 500; // Adjust threshold based on testing

  // ------------------- Serial Output -------------------
  Serial.println("-------- 📊 Weather Station Data --------");
  Serial.print("🌡️ Temperature: "); Serial.print(temp); Serial.println(" °C");
  Serial.print("💧 Humidity: "); Serial.print(hum); Serial.println(" %");
  Serial.print("📉 Pressure: "); Serial.print(pressure); Serial.println(" hPa");
  Serial.print("👆🏻 Altitude: "); Serial.print(altitude); Serial.print("m");
  Serial.print("\n🔥 Gas Level (MQ2): "); Serial.println(gasValue);
  Serial.print("🪵 Vibration: "); Serial.println(vibrationDetected ? "Detected" : "None");
  Serial.print("🌧️ Rain: "); Serial.println(isRaining ? "Yes" : "No");
  Serial.println("----------------------------------------\n");

  delay(4000); // Delay before next reading
}
