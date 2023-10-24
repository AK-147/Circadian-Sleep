int light_intensity;

void setup() {
  Serial.begin(9600);
}

void loop() {
  light_intensity = analogRead(A0);
  Serial.println(light_intensity);
  delay(100);
}
