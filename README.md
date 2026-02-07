# Vecna-sVictims
We can restore balance to a broken code. A hacker ... but for good ##conformityGate

Project Overview
This project is inspired by the iconic Lite Brite scene from Stranger Things Season 4, Episode 7, where Dustin, Erica, and Lucas communicate with Nancy, Steve, and the others in the Upside Down. Lite Brite Scene Stranger Things Season 4 - Episode 7 Clip 🔥
We created a hand-wired LED matrix (5 rows × 12 columns) where individual LEDs can be turned on based on finger movements detected by a camera. The concept allows users to “draw” messages in real-time using hand motion, similar to how the characters communicated in the show.

To Run Simulation (camera and digital representation of LEDs): Open main.py and run.
To Run Physical LED Matrix: contruct a 12x6 multiplexed LED matrix on a breadboard.

Features
•	5×12 LED matrix with multiplexing to control each LED individually.
•	Finger tracking via camera: Only detects a specific color (red in our implementation) to trigger LED activation.
•	Virtual matrix visualization: Allows you to see which LEDs would light up before activating the physical board.
•	Dynamic control: LEDs turn on one at a time based on the detected motion.

Hardware
•	ESP32 microcontroller
•	Hand-wired LED matrix (5 rows × 12 columns)
•	Jumper wires and breadboard for connections
•	USB cable for programming and power

Software
•	Arduino IDE / ESP32 C++ code: Controls the multiplexed LED matrix and listens for commands.
•	Python (VS Code):
o	Captures input from the computer camera
o	Applies a color mask to detect finger motion
o	Maps the detected position to the LED matrix
o	Sends commands to ESP32 via USB Serial
How It Works
1.	Camera Input: A computer camera tracks finger movement.
2.	Color Mask: Only red colors are detected to isolate the finger from the background.
3.	Virtual Matrix Mapping: The camera coordinates are translated to the corresponding LED in the 5×12 grid.
4.	LED Activation: The Python script sends a command over USB Serial to the ESP32, which turns on the corresponding LED.
5.	Multiplexing: Each LED is controlled individually using multiplexing, allowing one LED at a time to light up without requiring a dedicated pin for each LED.
