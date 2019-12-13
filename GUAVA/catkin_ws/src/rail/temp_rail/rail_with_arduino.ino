'''
This is code for arduino.
With this code, you can control rail 4/7 inches/sec. (total 70 seconds)
'''

const int ENA = 2;
const int DIR = 3;
const int PUL = 4;
int gap = 800;
long long int forty_inch = 138180;
long long int temp = 0;
const int FROM_MOTOR = HIGH;
const int TO_MOTOR = LOW;

void setup() {
  // put your setup code here, to run once:
  pinMode(ENA, OUTPUT);
  pinMode(DIR, OUTPUT);
  pinMode(PUL, OUTPUT);
  digitalWrite(ENA, LOW);
  //digitalWrite(DIR, TO_MOTOR);
  digitalWrite(DIR, FROM_MOTOR);
  digitalWrite(PUL, HIGH);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int j = 0; j < 6; j++)
  {
    digitalWrite(PUL, HIGH);
    delayMicroseconds(gap);
    digitalWrite(PUL, LOW);
    //delayMicroseconds(gap);
  }
  if (gap > 78) gap--;
  temp++;
  if (temp >= forty_inch) delay(1000000);
}
