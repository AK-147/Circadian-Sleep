const int GSR = A0;
int sensor = 0;
int gsr_avg = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  long sum = 0;
  for(int i = 0; i < 10; i++) {
    sensor = analogRead(GSR);
    sum += sensor;
    delay(10);
  }
  gsr_avg = sum / 13.27;
  Serial.println(gsr_avg);
  delay(50);
}
