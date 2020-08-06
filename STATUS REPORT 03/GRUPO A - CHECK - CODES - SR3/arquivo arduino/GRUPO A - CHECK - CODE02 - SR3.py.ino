/*
  RFID RDM6300 data decoder library
 (c) Stephane Driussi 20150623
 Not for commercial use
 
 Refer to rdm6300_decoder_wiring.jpg diagram for proper connection
 
 */

#include <SoftwareSerial.h>
SoftwareSerial RFID(2, 3); // RX and TX
int botao=9;
int Led=13;
uint8_t Payload[6]; // used for read comparisons

void setup()
{
  pinMode(Led, OUTPUT);
  pinMode (botao, INPUT);
  RFID.begin(9600);    // start serial to RFID reader
  Serial.begin(9600);  // start serial to PC 
}

void loop()
{
  if (RFID.available() > 0){
    Serial.println("");
 
  }
  int x = 0;
  while (RFID.available() > 0) 
  {
    x ++;
    digitalWrite(Led, HIGH);
    uint8_t c = RFID.read();
    Serial.print(" ");
    Serial.print(c,DEC);
    if (x >= 14){
      delay(1000);
      while(RFID.available() > 0){
        c = RFID.read();
        }

    }
  }
  if (digitalRead(botao)){
    Serial.print("stop");
    delay(500);
  }
  digitalWrite(Led, LOW);   
  delay(100);
}
