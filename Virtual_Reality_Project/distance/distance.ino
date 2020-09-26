const byte trigPin=10;
const byte echoPin=9;
const int soundSpeed=340; //m/s 
float temp,distance;
void setup() {
 
  // put your setup code here, to run once:
Serial.begin(9600);

pinMode(echoPin,INPUT);
pinMode(trigPin,OUTPUT);
digitalWrite(trigPin,LOW);
}

void loop() {
  digitalWrite(trigPin,HIGH);
  delayMicroseconds(15);
  digitalWrite(trigPin,LOW);
  temp=pulseIn(echoPin,HIGH);
  distance = temp*soundSpeed/20000. ;
  
  Serial.println(distance);
 delay(1000); // put your main code here, to run repeatedly:

}
