#include <Adafruit_Sensor.h>
#include <DHT.h>
// DHT pin:
#define DHTPIN 2

#define DHTTYPE DHT22   // DHT 22  (AM2302)

// Inicializar:
DHT dht = DHT(DHTPIN, DHTTYPE);

int LDR_pin = A0;
int LED_pin = 5;

void setup() {

  pinMode(LDR_pin, INPUT);
  pinMode(LED_pin, OUTPUT);
  // Comunicacion serial a 9600:
  Serial.begin(9600);
  dht.begin();
}
void loop() {
 
  int luz = analogRead(LDR_pin);
  // Leer la humedad en %:
  float h = dht.readHumidity();
  // Leer la temperatura en Celsius:
  float t = dht.readTemperature();
  
  // verificar si las medidas son correctas:
  if (isnan(h) || isnan(t)) {
    Serial.println("No ha sido posible leer datos!");
    return;
  }
  
  // Se define en que rango es necesaria la luz LED
  if (luz > 500) {
    digitalWrite(LED_pin, HIGH); // pin 13 HIGH
  }
  else{
    digitalWrite(LED_pin, LOW); // pin 13 LOW
  }
  
  // Enviamos datos a serial
  Serial.print(t);
  Serial.print(',');
  Serial.print(h);
  Serial.print(',');
  Serial.println(light);
 
  delay(1000);

}
