/*int lp = 5;
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


/*void setup() {
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
*/


/*int buzpin1 = 7;
int buzpin2 = 8;
int randoms = 0;

void setup(){
  pinMode(buzpin1, OUTPUT);
  pinMode(buzpin2, OUTPUT);  
}

void loop(){
  randoms = randoms+1;
  digitalWrite(buzpin1, HIGH);
  digitalWrite(buzpin2, LOW);
  delay(250);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, LOW);
  delay(100);
  digitalWrite(buzpin1, HIGH);
  digitalWrite(buzpin2, LOW);
  delay(250);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, LOW);
  delay(100);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, HIGH);
  delay(300);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, LOW);
  delay(100);
  digitalWrite(buzpin1, HIGH);
  digitalWrite(buzpin2, LOW);
  delay(250);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, LOW);
  delay(100);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, HIGH);
  delay(300);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, LOW);
  delay(100);
  digitalWrite(buzpin1, HIGH);
  digitalWrite(buzpin2, LOW);
  delay(250);
  digitalWrite(buzpin1, LOW);
  digitalWrite(buzpin2, LOW);
  delay(100);
  if (randoms == 3){
    randoms = 0;
    digitalWrite(buzpin1, HIGH);
    digitalWrite(buzpin2, LOW);
    delay(250);
    digitalWrite(buzpin1, LOW);
    digitalWrite(buzpin2, LOW);
    delay(100);
  }
}*/

/*
int speakerPin = 9;
int length = 28;
char notes[] = "GGAGcB GGAGdc GGxecBA yyecdc";
int beats[] = { 2, 2, 8, 8, 8, 16, 1, 2, 2, 8, 8,8, 16, 1, 2,2,8,8,8,8,16, 1,2,2,8,8,8,16 };
int tempo = 150;

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
}}
void playNote(char note, int duration) {
  char names[] = {'C', 'D', 'E', 'F', 'G', 'A', 'B',           
                  'c', 'd', 'e', 'f', 'g', 'a', 'b',
                  'x', 'y' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014,
                  956,  834,  765,  593,  468,  346,  224,
                  655 , 715 };
  int SPEE = 5;
  for (int i = 0; i < 17; i++) {
    if (names[i] == note) {
      int newduration = duration/SPEE;
      playTone(tones[i], newduration);
  }}}
void setup() {
  pinMode(speakerPin, OUTPUT);
}
void loop() {
  int i = 0;
  for (;i < length;) {
    i++;
    if (notes[i] == ' ') {
      delay(beats[i] * tempo);
    } else {
      playNote(notes[i], beats[i] * tempo);
      }
    delay(tempo);
}}

*/
int speakerPin = 9;
int length = 15; // the number of notes
char notes[] = "ccgga agffeeddc "; // a space represents a rest
int beats[] = { 1,1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 4 };
int tempo = 300;

void playTone(int tone, int duration) {
  for (long i = 0; i < duration * 1000L; i += tone * 2) {
    digitalWrite(speakerPin, HIGH);
    delayMicroseconds(tone);
    digitalWrite(speakerPin, LOW);
    delayMicroseconds(tone);
  }}

void playNote(char note, int duration) {
  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int tones[] = { 1915, 1700, 1519, 1432, 1275, 1136, 1014, 956 };
  for (int i = 0; i < 8; i++) {
    if (names[i] == note) {
      playTone(tones[i], duration);
    }}}

void setup() {
  pinMode(speakerPin, OUTPUT);
}

void loop() {
  for (int i = 0;i < length;i++) {
    if (notes[i] == ' ') {
      delay(beats[i] * tempo); // rest
    } else {
      playNote(notes[i], beats[i] * tempo);
    }
    delay(tempo / 2); 
  }}
