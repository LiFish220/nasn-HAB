#include <MQUnifiedsensor.h>
#include <DHT.h>
#include <DHT_U.h>
#define DHTTYPE DHT22



//float temp, val = A0;
int gasSensor = A1;
int chk;
float hum;  //humidity value
float temp; //temperature value
float co2; // co2
float co; // co
DHT dht(DHTPIN, DHTTYPE);




float NewTemp ;        
                      
void setup() {
  Serial.begin(9600);
  pinMode(6,OUTPUT);
  pinMode(A2,INPUT);
  pinMode(7,OUTPUT);
  pinMode(A3,INPUT);

  dht.begin();
}

void loop() {
  {

    //MQ135

    co2 = analogRead(A2)*9.0;

    //MQ5

    co = analogRead(A3);
    
    //DHT22

    hum = dht.readHumidity();
    temp= dht.readTemperature()*0.97;

    Serial.print(hum);
    Serial.print(" %");
    Serial.print("#");
    Serial.print(temp);
    Serial.print("co2：");
    Serial.println(co2);
    Serial.print("ppm");
    Serial.print("#");
    Serial.println(co);

    delay(2000); 
    

  }

}
