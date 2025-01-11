# OwenVision 
OwenVision is an innovative project that integrates QwenLM (a powerful vision large language model) with OpenCV to analyze live camera input and generate natural language descriptions of the events happening in real-time. This project is designed to showcase the seamless combination of computer vision and Generative AI to create intelligent systems capable of understanding and describing visual scenes.

# Features
- Live Event Description: Processes live camera input and provides a human-like description of ongoing events.
- QwenLM Integration: Utilizes QwenLM to generate high-quality, context-aware language descriptions.
- OpenCV Integration: Leverages OpenCV for real-time video capture and preprocessing.
- Plug-and-Play Design: Simple setup and operation for immediate usage.

# Requirements
To run OwenVision, you need the following:
Hardware: A computer with a webcam or an external camera.
Software:
- Python 3.8 or higher

Required libraries (install using requirements.txt):
- OpenCV
- Transformers (for QwenLM)
- NumPy
- Other dependencies (listed in requirements.txt)

# Installation
Clone the repository:
```
git clone https://github.com/yourusername/OwenVision.git
cd OwenVision
```
Install the required dependencies:
```
pip install -r requirements.txt
```
Verify your camera setup:
Ensure your webcam is connected and accessible through OpenCV.
Download and configure QwenLM:
- Follow the instructions to download QwenLM from the official repository or provider.
- Place the model in the models directory or configure the path in the project settings. 

# Usage
Run the following command to start OwenVision:
```
python main.py
```
The program will:
1. Access the camera feed via OpenCV.
2. Process each frame to detect key features or activities.
3. Use QwenLM to generate a descriptive narrative for the detected events.
4. Display the live camera feed with the event description overlaid.

# Installation
1. Clone the repository:
```
