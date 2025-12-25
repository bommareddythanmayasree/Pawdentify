# 🐾 Pawdentify  
### AI-Powered Dog Breed Identification & Insight System

Pawdentify is an **AI-driven dog breed identification system** that leverages **deep learning (CNNs + transfer learning)** to classify dog breeds from images and provide meaningful breed insights such as **temperament, grooming needs, health risks, and training difficulty** through a simple and intuitive interface.

---

## 🚀 Why Pawdentify?

Identifying a dog’s breed helps owners better understand:

- 🧠 Behavior and temperament  
- ✂️ Grooming and care needs  
- 🩺 Potential health risks  
- 🎓 Training requirements  

**Pawdentify bridges this gap using computer vision and AI**, making breed identification **fast, accurate, and informative**.

---

## ✨ Key Features

- 🐕 Dog breed prediction from uploaded images  
- 🧠 CNN-based deep learning model with transfer learning  
- 📊 Detailed breed insights, including:
  - Temperament  
  - Grooming needs  
  - Common health risks  
  - Training difficulty  
- ⚡ Fast and lightweight backend inference  
- 🧩 Clean, modular, and scalable project structure  

---

## 🧠 How It Works

1. User uploads a dog image  
2. Image is preprocessed and passed to a trained CNN model  
3. Model predicts the most likely dog breed  
4. Breed-specific information is fetched and displayed to the user  

---

## 🛠️ Tech Stack

### 🔹 Core Technologies
- Python  
- TensorFlow / Keras  
- Convolutional Neural Networks (CNN)  
- Transfer Learning (MobileNetV2 / NASNet)

### 🔹 Backend
- Flask / FastAPI  
- REST APIs  

### 🔹 Data & Utilities
- NumPy  
- OpenCV / PIL  
- JSON-based metadata storage  

---

## 📁 Project Structure

Pawdentify/
│
├── api.py                         # Backend API server
├── prepare.py                     # Data preprocessing
├── step2-NasNetLarge-Model.py     # Model training script
├── mobilenetv2-dog-breed-model.h5 # Trained model
├── requirements.txt               # Dependencies
├── static/                        # UI assets (if applicable)
├── templates/                     # Frontend templates
└── README.md                      # Project documentation

---

## ⚙️ Installation & Setup

### 🔹 Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### 🔹 Clone the Repository

git clone https://github.com/bommareddythanmayasree/Pawdentify.git
cd Pawdentify
🔹 Create Virtual Environment (Optional)


python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
🔹 Install Dependencies

pip install -r requirements.txt

### ▶️ Running the Application
Start the backend server:

python api.py
Then open your browser and visit:

http://localhost:5000
Upload a dog image to get the predicted breed and detailed insights.

### 🧪 Model Details
Architecture: CNN with Transfer Learning

Base Models: MobileNetV2 / NASNet

Input: Dog image

Output: Breed classification

###  📦 Model File

mobilenetv2-dog-breed-model.h5
You can retrain or fine-tune the model using the provided training scripts.

###  🔌 API Endpoints
Endpoint	Method	Description
/predict	POST	Upload image and get breed prediction
/breed/<name>	GET	Retrieve breed details

###  📈 Use Cases
🐾 Pet owners identifying unknown dog breeds

🏥 Veterinary and pet-care platforms

🎓 AI & ML learning projects

📄 Resume-worthy deep learning application

###  🤝 Contributing
Contributions are welcome!

Fork the repository

Create a feature branch

Commit your changes

Push to your fork

Open a Pull Request

Please follow clean coding standards and write clear commit messages.
