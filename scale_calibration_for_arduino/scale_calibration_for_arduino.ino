
// Calibrating the load cell
#include "HX711.h"

// HX711 circuit wiring
const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

/*
for an object weighing 17.8oz (504.6215g)

-112996
-112289
-112335
-112529
-112304
avg: -112490.6
//calibration factor will be the (-112490.6)/(504.6215) = -222.921

340g
-72755
-72709
-72698
-72678
-72714
avg: -72711
//calibration factor will be the (-72711)/(340) = -213.856

//calibration factor will be the (reading)/(known weight)

*/

HX711 scale;

void setup() {
  Serial.begin(57600);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {

  if (scale.is_ready()) {
    scale.set_scale();    
    Serial.println("Tare... remove any weights from the scale.");
    delay(5000);
    scale.tare();
    Serial.println("Tare done...");
    Serial.print("Place a known weight on the scale...");
    delay(5000);
    long reading = scale.get_units(10);
    Serial.print("Result: ");
    Serial.println(reading);
  } 
  else {
    Serial.println("HX711 not found.");
  }
  delay(1000);
}

//calibration factor will be the (reading)/(known weight)