# 🌿 PLANT PULSE — Smart Farming Assistant

<p align="center">
  <img src="PLANTPULSE-web-app/images/title.png" alt="Plant Pulse Logo" width="300"/>
</p>

<p align="center">
  <b>An AI-powered platform for smart, sustainable agriculture</b><br/>
  Crop Recommendations · Plant Disease Detection · Weather Forecasting · AI Chatbot
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/TensorFlow-2.16+-orange?logo=tensorflow" />
  <img src="https://img.shields.io/badge/Streamlit-1.23+-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Gemini-1.5Flash-green?logo=google" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

---

## 📖 Overview

**Plant Pulse** is a comprehensive AI-driven smart farming platform that empowers farmers with three intelligent tools:

- 🌾 **Crop Recommendation System** — Predicts the best crop to grow based on soil and climate data using Machine Learning
- 🔬 **Plant Disease Identification** — Detects plant diseases from leaf images using a deep learning CNN model
- 🌐 **CropCare Web Portal** — A full-featured website integrating weather forecasts, an AI chatbot, agriculture news, and crop guides

> 📄 This project is accompanied by an **IEEE Research Paper**:  
> *Smart Crop Recommendation System with Plant Disease Identification*

---

## 🗂️ Project Structure

```
PLANT PULSE/
├── 📂 CROP-RECOMMENDATION/          # ML-based crop prediction (Streamlit app)
│   ├── app.py                       # Main Streamlit app
│   ├── Crop_reccom(final).ipynb     # Model training notebook
│   ├── Crop_recommendation.csv      # Dataset (7 features, 22 crops)
│   ├── RandomForest.pkl             # Trained Random Forest model
│   ├── DecisionTree.pkl             # Trained Decision Tree model
│   ├── KNeighborsClassifier.pkl     # Trained KNN model
│   ├── NBClassifier.pkl             # Trained Naïve Bayes model
│   ├── XGBoost.pkl                  # Trained XGBoost model
│   └── requirements.txt
│
├── 📂 PLANT-DISEASE-IDENTIFICATION/ # CNN-based disease detection (Streamlit app)
│   ├── main.py                      # Main Streamlit app
│   ├── Train_plant_disease.ipynb    # CNN training notebook
│   ├── Test_plant_disease.ipynb     # Model evaluation notebook
│   ├── trained_plant_disease_model.keras  # Pre-trained CNN (~90MB)
│   ├── training_hist.json           # Training accuracy/loss history
│   ├── test/                        # Sample test images
│   └── requirements.txt
│
├── 📂 PLANTPULSE-web-app/           # Static CropCare web portal
│   ├── index.html                   # Main landing page
│   ├── css/style.css
│   ├── js/main.js
│   ├── chatbot/                     # AI chatbot (Gemini API)
│   ├── weather-forecast/            # Real-time weather (OpenWeatherMap)
│   ├── explore/                     # Crop parameter explorer
│   ├── guide/                       # Crop cultivation guide
│   ├── News/                        # Agriculture news
│   └── Contact/                     # Contact form
│
└── 📄 IEEE_Paper_Smart_Crop_Recommendation_System_with_Plant_Disease_Identification.pdf
```

---

## ✨ Features

### 🌾 1. Crop Recommendation System
- Input **7 soil & climate parameters**: Nitrogen, Phosphorus, Potassium, Temperature, Humidity, pH, Rainfall
- Get instant crop predictions using a **Random Forest ML model**
- Receive detailed **growing guidance** powered by **Google Gemini 1.5 Flash**
- View **latest agriculture news** via NewsAPI
- **Multilingual support**: English, Kannada, Hindi, Telugu, Tamil

### 🔬 2. Plant Disease Identification
- Upload a leaf image and detect diseases instantly
- Powered by a **TensorFlow/Keras CNN** trained on the PlantVillage dataset
- Classifies **38 disease/health classes** across 14 crop types:
  - Apple, Blueberry, Cherry, Corn, Grape, Orange, Peach, Pepper, Potato, Raspberry, Soybean, Squash, Strawberry, Tomato

### 🌐 3. CropCare Web Portal
| Feature | Description |
|---|---|
| 🤖 AI Chatbot | Farming Q&A powered by Gemini 1.5 Flash |
| 🌤️ Weather Forecast | Real-time weather via OpenWeatherMap API |
| 🌱 Crop Explorer | Browse soil/climate data for 22 crops |
| 📰 News | Latest agriculture news |
| 📋 Crop Guide | Step-by-step cultivation guide |
| 🌍 Multilingual | 5 language support via Google Translate |

---

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| **ML / AI** | scikit-learn, XGBoost, TensorFlow 2.x, Keras |
| **Backend** | Python 3.12, Streamlit |
| **Data** | NumPy, Pandas, Matplotlib, Seaborn |
| **Image Processing** | Pillow (PIL), OpenCV |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript, Bootstrap 5, Font Awesome, Axios |
| **External APIs** | Google Gemini 1.5 Flash, OpenWeatherMap, NewsAPI, Google Translate |
| **Dev Tools** | Jupyter Notebook, VS Code |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 – 3.12
- pip
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/suhasshetti02/Plant-Pulse.git
cd Plant-Pulse
```

### 2. Run the Crop Recommendation App
```bash
cd CROP-RECOMMENDATION
pip install -r requirements.txt
streamlit run app.py
```
> App runs at **http://localhost:8501**

### 3. Run the Plant Disease Detection App
```bash
cd PLANT-DISEASE-IDENTIFICATION
pip install -r requirements.txt
streamlit run main.py
```
> App runs at **http://localhost:8502**

### 4. Open the Web Portal
Simply open `PLANTPULSE-web-app/index.html` in your browser.  
*(Ensure both Streamlit apps are running for full functionality)*

---

## 📊 Dataset

**Crop Recommendation Dataset** (`Crop_recommendation.csv`)
- **2,200 records**, 22 crop classes
- Features: N, P, K, Temperature, Humidity, pH, Rainfall

**Plant Disease Dataset**
- Based on the [PlantVillage Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
- 38 classes, 14 crop types

---

## 🤖 ML Models

| Model | Task | Accuracy |
|---|---|---|
| Random Forest | Crop Recommendation | ~99% |
| Decision Tree | Crop Recommendation | ~98% |
| K-Nearest Neighbors | Crop Recommendation | ~97% |
| Naïve Bayes | Crop Recommendation | ~99% |
| XGBoost | Crop Recommendation | ~99% |
| CNN (Keras) | Disease Detection | ~95%+ |

---

## 🌍 Multilingual Support

The platform supports **5 languages**:

| Language | Code |
|---|---|
| English | `en` |
| Kannada | `kn` |
| Hindi | `hi` |
| Telugu | `te` |
| Tamil | `ta` |

---

## 📄 Research Paper

This project is backed by an IEEE research paper:

> **"Smart Crop Recommendation System with Plant Disease Identification"**  
> Presented as part of academic research in AI-driven precision agriculture.

📎 See: `IEEE_Paper_Smart_Crop_Recommendation_System_with_Plant_Disease_Identification.pdf`

---

## 👥 Team

**Team PlantPulse**  
Built with 💚 for sustainable smart farming.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  © 2024 Team PlantPulse — All Rights Reserved
</p>
