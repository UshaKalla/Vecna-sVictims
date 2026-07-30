# Vecna-sVictims: Interactive Lite-Brite LED Matrix

> **Note:** "We can restore balance to a broken code. A hacker... but for good." 
> This project is inspired by the iconic Lite-Brite communication scene from *Stranger Things* Season 4, allowing users to draw messages in real-time using hand motion and computer vision.

---

### Project Summary
* **Inspiration:** Recreates the communication method from *Stranger Things* Season 4, Episode 7, where characters use light and color to communicate across realms.
* **Core Purpose:** To track hand gestures via webcam, isolate a specific color (red) to follow finger movement, and light up corresponding LEDs on a physical matrix or virtual simulator.

---

### Key Features & Components
* **5×12 LED Matrix:** Hand-wired matrix utilizing multiplexing to control individual LEDs without needing a dedicated pin for every single light.
* **Color-Based Finger Tracking:** Python-based camera tracking that uses a color mask to isolate a red indicator on the user's finger.
* **Virtual Matrix Visualization:** Test and view the grid layout digitally before running the physical hardware.
* **USB Serial Communication:** Translates camera screen coordinates into hardware commands sent from Python to an ESP32 microcontroller.

---

### Hardware Requirements
* ESP32 microcontroller
* Hand-wired LED matrix (5 rows × 12 columns)
* Breadboard and jumper wires
* USB cable for programming and serial communication

---

### Software Architecture & Execution
* **Full Simulation & Camera:** Open and run `main.py`
* **LED-Only Simulation:** Open and run `main-ledsim.py`
* **Camera-Only Tracking:** Open and run `main-cam.py`
* **Physical Setup:** Construct a multiplexed LED matrix on a breadboard and wire it to the ESP32 using the C++ Arduino code.

---

### How It Works
1. **Camera Input:** The computer webcam tracks real-time hand and finger motion.
2. **Color Masking:** Filters out the background by isolating target red objects.
3. **Coordinate Mapping:** Translates camera screen coordinates to fit the 5×12 grid layout.
4. **Hardware Command:** Sends serial signals over USB to the ESP32 to activate the specific LED coordinate.
