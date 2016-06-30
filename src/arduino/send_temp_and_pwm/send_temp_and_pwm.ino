#include <OneWire.h>
#include <DallasTemperature.h>

#define PIN_TEMPSENSORS 22
#define PIN_POT 5
#define PIN_PWM 2
#define INDEXOF_CONTACT_SENSOR 0
#define INDEXOF_AMBIENT_SENSOR 1
#define NUMBER_OF_POT_READS_PER_VALUE 10

OneWire oneWire(PIN_TEMPSENSORS);
DallasTemperature sensors(&oneWire);

int pwmValue = 0;

void setup() {
  Serial.begin(9600);
  sensors.begin();
}

void loop(){
  pwmValue = readPot();
  analogWrite(PIN_PWM, pwmValue);
  sensors.requestTemperatures(); 
  float contact = sensors.getTempCByIndex(INDEXOF_CONTACT_SENSOR);
  float ambient = sensors.getTempCByIndex(INDEXOF_AMBIENT_SENSOR);

  Serial.print(contact);
  Serial.print(",");
  Serial.print(ambient);
  Serial.print(",");
  Serial.print(pwmValue);
  Serial.println();
  delay(1000);
  
}

int readPot(){
  int sum = 0;
  
  for(int i = 0; i < NUMBER_OF_POT_READS_PER_VALUE; i++){
    sum += analogRead(PIN_POT);
    delay(10);
  }

  int average = sum / NUMBER_OF_POT_READS_PER_VALUE;
  return average / 4;
}







