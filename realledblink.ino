/*
    Use this code for testing the 5x12 multiplexed LED array.
*/


int colPins[12] = {23, 22, 21, 19, 18, 5, 4, 2, 15, 13, 32, 33};

// Rows (6 pins)
int rowPins[6] = {25, 26, 27, 14, 12, 15};

void setup() {
  // Initialize column pins
  for (int i = 0; i < 12; i++) {
    pinMode(colPins[i], OUTPUT);
    digitalWrite(colPins[i], LOW); // Columns OFF initially
  }

  // Initialize row pins
  for (int i = 0; i < 6; i++) {
    pinMode(rowPins[i], OUTPUT);
    digitalWrite(rowPins[i], HIGH); // Rows OFF initially (active LOW)
  }
}

void loop() {
  // Loop through each row
  for (int row = 0; row < 6; row++) {
    // Loop through each column
    for (int col = 0; col < 12; col++) {

      // Turn off all rows
      for (int r = 0; r < 6; r++) {
        digitalWrite(rowPins[r], HIGH);
      }

      // Turn off all columns
      for (int c = 0; c < 12; c++) {
        digitalWrite(colPins[c], LOW);
      }

      // Activate current row and column
      digitalWrite(rowPins[row], LOW);   // Active row
      digitalWrite(colPins[col], HIGH);  // LED ON

      delay(100); // 0.1s per LED, adjust as needed
    }
  }
}

/*
  6x12 LED Matrix - Turn All LEDs ON
  Rows = active LOW
  Columns = active HIGH
*/