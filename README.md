
# Final Year Project: Home Automation and Security System

## Project Overview

This project consists of two main parts aimed at enhancing home security and automating home appliances using advanced technologies.

### Part 1: Home Security System

The Home Security System is designed using Raspberry Pi 4 and incorporates face recognition technology to ensure secure access to the home. Key features and technologies used in this part are:

- **Face Recognition Technology**: Utilizes the face recognition module, `dlib`, `Python3`, and `OpenCV`.
- **Electronic Door Lock**: The system opens the electronic door lock when a known person is detected.
- **Unknown Person Detection**: When an unknown person is detected, the system takes a snapshot and shares it with the admin via Telegram.
- **Technologies Used**: 
  - **Raspberry Pi 4**: The central processing unit of the system.
  - **dlib**: A modern C++ toolkit containing machine learning algorithms and tools.
  - **Python3**: The programming language used for developing the system.
  - **OpenCV**: An open-source computer vision and machine learning software library.

### Part 2: Home Appliance Control System

The second part of the project focuses on controlling home appliances remotely. This is achieved through the development of an application that communicates with IoT devices. Key features and technologies used in this part are:

- **Remote Control**: The system allows users to control home appliances when they are not at home.
- **Custom Application**: An application is developed to handle home appliances.
- **NodeMCU**: Used to connect and control home appliances over the internet.
- **IP Address Configuration**: To control the NodeMCU, users need to write the IP address of the NodeMCU in the application.
- **Technologies Used**: 
  - **IoT (Internet of Things)**: Enables the network of physical objects to exchange data.
  - **NodeMCU**: An open-source IoT platform.
  - **C++**: The programming language used for developing the control system.

## Project Setup and Usage

### Prerequisites

- Raspberry Pi 4
- Face recognition module
- Electronic door lock
- Telegram account for receiving notifications
- NodeMCU
- Home appliances compatible with IoT control
- Application for controlling appliances (developed as part of this project)

### Installation and Configuration

#### Home Security System

1. Set up the Raspberry Pi 4 with the required dependencies:
    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install python3-opencv
    sudo pip3 install dlib
    sudo pip3 install face_recognition
    ```

2. Connect the face recognition module and electronic door lock to the Raspberry Pi.

3. Configure the Telegram bot to send notifications:
    - Create a new bot on Telegram and get the API token.
    - Update the script with your API token and chat ID.

4. Run the face recognition script:
    ```bash
    python3 face_recognition_script.py
    ```

#### Home Appliance Control System

1. Set up the NodeMCU with the required firmware and libraries.

2. Connect the home appliances to the NodeMCU.

3. Develop and install the application on your device:
    - Ensure the application is configured with the NodeMCU's IP address.

4. Run the application and start controlling your appliances remotely.

## Repository Structure

```
|-- HomeSecuritySystem/
|   |-- face_recognition_script.py
|   |-- requirements.txt
|   |-- README.md
|
|-- HomeApplianceControl/
|   |-- application_code/
|   |-- nodemcu_firmware/
|   |-- README.md
|
|-- LICENSE
|-- README.md
```

## Contribution

Feel free to fork this repository and contribute by submitting pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# Security-system
