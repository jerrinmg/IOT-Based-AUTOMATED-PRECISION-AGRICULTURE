
# Project Documentation

## Introduction

This document outlines the technical details and component descriptions for the agricultural monitoring and automated irrigation system.

## Block Diagram
The project’s block diagram features a power supply that drives the Raspberry Pi2B, camera module, and various sensors. The Raspberry Pi connects via Wi-Fi and cloud, enabling real-time data exchange and remote control. Sensors for temperature, humidity, and soil moisture provide crucial environmental insights. Additionally, a controller facilitates precise drip irrigation. This integrated system embodies a smart and efficient approach to modern agriculture.

![Block Diagram](https://github.com/jerrinmg/IOT-Based-AUTOMATED-PRECISION-AGRICULTURE/blob/e48eb2df02e44807e61e7777635c3f2b59479e5c/Documentation/Block%20Diagram.png)

## Circuit Diagram
In the setup, an IRFZ44N MOSFET is employed for controlling the mini motor pump, ensuring efficient irrigation. The 5V regulator IC serves to provide stable power to the assortment of components, including the soil moisture sensor and DHT11 sensor for environmental data collection. The GPIO control signals from the Raspberry Pi 2B facilitate seamless interaction with these sensors, enabling real-time data acquisition. The incorporation of a Raspberry Pi Camera Module (Rev 1.3) allows for image capture, specifically targeting plant leaves for disease detection. The synchronized connection of these elements, coupled with meticulous ground and power connections, forms the foundation of an integrated system poised for effective and automated precision agriculture.


![Circuit Diagram](https://github.com/jerrinmg/IOT-Based-AUTOMATED-PRECISION-AGRICULTURE/blob/e48eb2df02e44807e61e7777635c3f2b59479e5c/Documentation/Circuit%20Diagram.png)

## Component Descriptions

### Camera

- **Usage**: Used to capture images of the crops.
- **Connection**: Directly connected to the Raspberry Pi model via either USB port or the 15-pin header provided for the camera interface of the Raspberry Pi.

### Raspberry Pi

- **Description**: A small-sized module akin to a small computer.
- **Functionality**: Receives images captured by the camera, processes, and analyzes them using TensorFlow to detect specific features or conditions.

### Irrigation System

- **Functionality**: Utilizes data from the Raspberry Pi to determine the precise watering needs of plants or crops.
- **Automation**: Can be connected to a pump linked to a water reservoir for automated irrigation.

### Sensors

#### Soil Moisture Sensor

- **Functionality**: Measures the volume of water content in the soil, helping to estimate the volume of stored water in the soil range.
- **Usage**: Integrated into the irrigation system to optimize water scheduling and minimize excessive water use.

#### DHT11 and FC28

- **DHT11**: Measures temperature and humidity, providing essential data for assessing environmental conditions affecting crop health.
- **FC28**: A soil moisture sensor that aids in monitoring the water content in the soil, crucial for efficient irrigation practices.

### Results

- **Training the CNN Model**: The CNN model was constructed using the Keras Sequential API, which allowed foreasy stacking of layers. The architecture comprised several Conv2D layers, eachfollowed by a MaxPooling2D layer. These layers were instrumental in learningrelevant features from the input images and reducing the spatial dimensions of thedata, making the model more efficient.
- **Purpose**: Stores data from sensors and images for logging and further analysis.

## Circuit Diagram
In the setup, an IRFZ44N MOSFET is employed for controlling the mini motor pump, ensuring efficient irrigation. The 5V regulator IC serves to provide stable power to the assortment of components, including the soil moisture sensor and DHT11 sensor for environmental data collection. The GPIO control signals from the Raspberry Pi 2B facilitate seamless interaction with these sensors, enabling real-time data acquisition. The incorporation of a Raspberry Pi Camera Module (Rev 1.3) allows for image capture, specifically targeting plant leaves for disease detection. The synchronized connection of these elements, coupled with meticulous ground and power connections, forms the foundation of an integrated system poised for effective and automated precision agriculture.


![Circuit Diagram](https://github.com/jerrinmg/IOT-Based-AUTOMATED-PRECISION-AGRICULTURE/blob/e48eb2df02e44807e61e7777635c3f2b59479e5c/Documentation/Circuit%20Diagram.png)

## Conclusion

This document provides a comprehensive overview of the components and their functionalities in the agricultural monitoring and automated irrigation system. 
