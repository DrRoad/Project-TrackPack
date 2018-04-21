void setup() {
    float Co-ords[] = {51.5074, 0.1278};

}

void loop() {
  // put your main code here, to run repeatedly:
  delay(300000)
  incdec_decision = random(1, 2)
  distances = {random(0.0001, 0.0005), random(0.0001, 0.0005)}
  
  switch (var) {
    case 1:
      Co-ords[0] += distances[0] 
      Co-ords[1] += distances[1] 
      break;
    case 2:
      Co-ords[0] -= distances[0] 
      Co-ords[1] -= distances[1] 
      break;
  Serial.print(Co-ords)
}
}
