int lp = 5;
int lpt = 6;
int lpth = 8;


void setup(){
  Serial.begin(9600);
  pinMode(lp, OUTPUT);
  pinMode(lpt, OUTPUT);
  pinMode(lpth, OUTPUT);
  
}

void loop() {
  digitalWrite(lp, HIGH);
  digitalWrite(lpt, LOW);
  digitalWrite(lpth, LOW);
  Serial.println('1');
  delay(2000);
  digitalWrite(lp, LOW);
  digitalWrite(lpt, HIGH);
  digitalWrite(lpth, LOW);
  Serial.println('2');
  delay(2000);
  digitalWrite(lp, LOW);
  digitalWrite(lpt, LOW);
  digitalWrite(lpth, HIGH);
  Serial.println('3');
  delay(2000);
}
*/
void setup() {
  Serial.begin(9600);
  Serial.print("Type any number");
}
char rx = 0;
void loop() {
  if (Serial.available() > 0){
    rx = Serial.read();
    if ((rx > "0") || ({
      Serial.println("It is a number");
    }
    else{
      Serial.println("It is a multidigit number");
    }
}}