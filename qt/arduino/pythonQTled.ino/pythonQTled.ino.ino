int i = 0;
#define leduno 4
#define leddos 5
#define ledtres 6
#define lednueve 9
#define led 13


 
int brightness = 0;    // how bright the LED is
int fadeAmount = 5;    // how many points to fade the LED by
 
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
    int in = Serial.read();
    
    in = in-48;
    Serial.println(in);
    analogWrite(lednueve, in );


    
    if(in == 37){
        digitalWrite(led, HIGH);
    }

    if(in == 40){
        digitalWrite(led, LOW);
    }

    if(in == 'B' ){
        int data = Serial.read();
        //Serial.println(data);
        analogWrite(lednueve, brightness);
        // change the brightness for next time through the loop:
        if ( brightness > 0) {
          brightness = brightness + fadeAmount;
        } 
         
         if ( brightness <= 5) {
          brightness =  brightness + 1;
          
        }        
         //Serial.println(brightness );
        if ( brightness >= 45) {
        //fadeAmount = -fadeAmount ;
        brightness = fadeAmount - brightness   ;
        //Serial.println("fade: "+fadeAmount);
         }
        
    }

    

 
   
   
  }
}
 
