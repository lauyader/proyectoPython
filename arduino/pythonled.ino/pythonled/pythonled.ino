int i = 0;
#define leduno 4
#define leddos 5
#define ledtres 6
#define ledcuatro 7
#define led 13
 
// the setup routine runs once when you press reset:
void setup() {    
  Serial.begin(9600);
  for (i=4; i<=13; i++){
       pinMode(i, OUTPUT);        
  }
 
}
 
// the loop routine runs over and over again forever:
void loop() {
  if(Serial.available()) {
    char in = Serial.read();
 
    if(in == 'U'){
        digitalWrite(led, HIGH);
    }

      if(in == 'X'){
        digitalWrite(led, LOW);
    }
  }
}
 
