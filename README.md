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

# 📥 Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/OwenVision.git
cd OwenVision
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
Verify your camera setup:Ensure your webcam is connected and accessible through OpenCV.
Download and configure QwenLM:
- Follow the instructions to download QwenLM from the official repository or provider.
- Place the model in the models directory or configure the path in the project settings.

# Example Output

When pointing the camera at a scene where someone is walking a dog, OwenVision might generate a description like:
```
"A person is walking their dog along a pathway."
```
# Customization

- Model Tuning: You can fine-tune QwenLM for more specific scenarios or integrate additional datasets to enhance performance.

- Event Detection: Modify the OpenCV event detection logic in event_detector.py to adapt the system for specialized use cases (e.g., sports analysis, traffic monitoring).

# 🤝 Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a feature branch: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add some feature'.
4. Push to the branch: git push origin feature-name.
5. Create a pull request.

# 📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgments

- QwenLM Team: For providing a state-of-the-art language model.

- OpenCV Community: For making computer vision accessible and powerful.

- All contributors and supporters of OwenVision.

Start exploring the power of real-time event description with OwenVision today!
Made with ❤️ by [Prakhar Awasthi](https://github.com/prakhar105)
