<p align="center">
  <img src="https://github.com/Atulya-Juyal/automated-irrigation/blob/main/pngtree-water-drop-logo-template-vector-image_220162.jpg" alt="logo" width="120"/>
  <br/>
</p>
<h1 align="center">Automated Irrigation System</h1>
<p align="center">
  An IoT-based solution that automatically waters plants when the soil gets dry, ensuring they get the right amount of water without manual intervention.
</p>

<p align="center">
  <a href="#"><img alt="Category" src="https://img.shields.io/badge/Category-IoT-orange?style=for-the-badge"></a>
  <a href="#"><img alt="Controller" src="https://img.shields.io/badge/Controller-Arduino-00979D?style=for-the-badge"></a>
  <a href="#"><img alt="Language" src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge"></a>
  <a href="#"><img alt="Status" src="https://img.shields.io/badge/Status-Prototype-green?style=for-the-badge"></a>
</p>

---

## 🚀 About The Project

This project addresses the common challenge of maintaining optimal soil moisture for plants. Forgetting to water plants or over-watering them can be harmful. This automated system uses a soil moisture sensor to constantly monitor the soil and activates a water pump only when necessary.

It serves as an excellent, practical introduction to IoT and hardware programming with Arduino.

### ✨ Features
* **Real-time Monitoring:** A soil moisture sensor continuously reads the moisture level of the soil.
* **Automatic Watering:** A water pump is automatically triggered when moisture levels fall below a predefined threshold.
* **Smart & Efficient:** Prevents over-watering and under-watering, promoting healthier plant growth and conserving water.
* **Plug and Play:** Simple to set up with common, low-cost hardware components.

---

## 🛠️ Hardware & Software

### Required Hardware
* **Microcontroller:** Arduino Uno (or any compatible board like Nano)
* **Sensor:** Soil Moisture Sensor Module (e.g., FC-28)
* **Actuator:** 5V DC Mini Water Pump
* **Driver:** L293D Motor Driver or a 5V Relay Module
* **Power:** 9V Battery or external power supply
* **Misc:** Jumper Wires, Small Water Pipe, Breadboard

### Required Software
* [Arduino IDE](https://www.arduino.cc/en/software)
* Project Code (`.ino` file from this repository)

---

## 📖 How It Works

The logic of the system is straightforward:
1.  The Arduino continuously reads the analog value from the soil moisture sensor.
2.  This value is compared against a `threshold` value set in the code.
3.  **If the soil is too dry** (sensor value is high), the Arduino sends a signal to activate the water pump.
4.  **If the soil has enough moisture** (sensor value is low), the pump remains off.
5.  This cycle repeats, ensuring the plant is always in an ideal environment.

---

## 📦 Installation Guide

1.  **Assemble the Hardware:** Connect all the components according to the circuit diagram above. Place the soil moisture sensor probe into the plant's soil.
2.  **Setup the Software:**
    * Download and install the [Arduino IDE](https://www.arduino.cc/en/software).
    * Connect your Arduino board to your computer via USB.
3.  **Upload the Code:**
    * Open the `.ino` project file from this repository in the Arduino IDE.
    * Select the correct Board (e.g., `Arduino Uno`) and Port from the `Tools` menu.
    * Click the `Upload` button to flash the code onto the Arduino.

✅ Your automated irrigation system is now ready to go!

---



> Made by Atulya Juyal
> 
> Check out my linkedin profile : https://www.linkedin.com/in/atulya-juyal-86a1a528a/
