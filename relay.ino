const int trigPin = 9;
const int echoPin = 10;

long duration;
int distance;

void setup() {
  // put your setup code here, to run once:
  pinMode(11,OUTPUT);
  Serial.begin(9600);
  pinMode(trigPin,OUTPUT);
  pinMode(echoPin, INPUT);
}

String incomingByte ;

void loop() {

  if(Serial.available()>0){
    incomingByte = Serial.readStringUntil('\n');
      if(incomingByte=="on"){

      digitalWrite(11,HIGH);

      Serial.write("Relay on");

    }

    else if (incomingByte == "off") {
      
      digitalWrite(11,LOW);

      Serial.write("Relay off");

    }

    else{

     Serial.write("invald input");

    }
  }
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  Serial.println(distance);
  delay(333);
}
