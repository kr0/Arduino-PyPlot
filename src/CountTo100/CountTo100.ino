void setup() {
  Serial.begin(9600);
  Serial.println("Counting to 100"); 
}

int count = 0;
void loop() {

  while(count <= 100){
    Serial.println(count);  
    count = count + 1;
  }

}
