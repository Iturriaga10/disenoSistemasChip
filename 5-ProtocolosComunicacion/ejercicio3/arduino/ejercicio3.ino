#include <ArduinoHttpClient.h>
//#include <ArduinoJson.h>
#include <WiFiNINA.h>

char ssid[] = "Totalplay-2.4G-54d8";
char password[] = "qmF3H9Y8KY28jSz3";

int status = WL_IDLE_STATUS;

char server[] = "";    //Always modify when re-run ngrok

WiFiClient client;

#define led 8
float valor;

void setup(){
  Serial.begin(9600);

  while (status != WL_CONNECTED) {
    Serial.println("Attempting to connect to Network: ");
    Serial.println(ssid);
    status = WiFi.begin(ssid,password);
    delay (1000);
  }

  Serial.print("Connected to SSID: ");
  Serial.println(WiFi.SSID());
  IPAddress ip = WiFi.localIP();
  IPAddress gateway = WiFi.gatewayIP();
  Serial.print("IP Address: ");
  Serial.println(ip);

  pinMode(led,OUTPUT);
  Serial.begin(9600);

}

void loop(){




  valor=analogRead(A0);
  
  if (valor < 800){
    Serial.print(1);
    if (client.connect(server, 80)) {
    client.println("GET /1 HTTP/1.1");
    client.println("Host: bd1b-187-189-173-143.ngrok.io/1");
   }
    digitalWrite(led,HIGH);
  }
  else{
    Serial.print(2);
    
    if (client.connect(server, 80)) {
    client.println("GET /1 HTTP/1.1");
    client.println("Host: bd1b-187-189-173-143.ngrok.io/0");
   }
    digitalWrite(led,LOW);
  }

  if (client.connected()) {
    client.stop();
  }
  
  delay(1000);
  
}