# 🌱 Smart Crop Rotation

## AI-Assisted Crop Rotation Planning for Sustainable Farming

Smart Crop Rotation is a **Streamlit-based agricultural decision-support application** that helps farmers choose suitable crops for their next cultivation cycle.

The system analyzes farm conditions such as **soil type, water availability, current crop, and previous crop** and generates a smart crop rotation recommendation. It also provides crop information, alternative recommendations, farm insights, multilingual support, and a downloadable farm report.

---

## 🚀 Features

* 🌱 Smart crop recommendation
* 🔄 Crop rotation planning
* 📊 Recommendation scoring system
* 🪴 Soil compatibility analysis
* 💧 Water availability analysis
* 🌾 Crop diversity suggestions
* 🌱 Soil health insights
* 📋 Alternative crop recommendations
* 🌍 Multilingual support
* 📥 Downloadable farm report
* 🎨 Modern and attractive Streamlit dashboard

---

## 🌾 Supported Crops

The application currently supports the following crops:

* Rice
* Wheat
* Maize
* Cotton
* Groundnut
* Soybean
* Chickpea
* Green Gram
* Black Gram
* Mustard
* Sorghum

Each crop contains information about:

* Water requirement
* Nutrient requirement
* Suitable soil type
* Growing season
* Recommended next crops
* Soil health benefits

---

## 🌍 Supported Languages

The application supports:

* 🇬🇧 English
* 🇮🇳 Kannada
* 🇮🇳 Hindi
* 🇮🇳 Telugu
* 🇮🇳 Tamil

The interface, crop names, soil types, water levels, recommendations, and farming insights are translated to make the application more accessible to farmers.

---

## 🪴 Supported Soil Types

* Loamy Soil
* Clay Soil
* Black Soil
* Sandy Soil
* Red Soil

---

## 💧 Water Availability Levels

The farmer can select:

* Low
* Medium
* High

The recommendation system considers the available water level while suggesting suitable crops.

---

## 🧠 How It Works

The application follows this workflow:

```text
Farmer Details
      ↓
Soil Type Selection
      ↓
Water Availability
      ↓
Current Crop Selection
      ↓
Previous Crop Analysis
      ↓
Crop Compatibility Analysis
      ↓
Recommendation Scoring
      ↓
Best Crop Recommendation
      ↓
Crop Rotation + Insights + Report
```

The recommendation system evaluates different crops based on compatibility with the selected farm conditions.

---

## 📊 Recommendation Factors

The crop recommendation is generated using factors such as:

* 💧 Water compatibility
* 🪴 Soil compatibility
* 🌱 Soil health benefit
* 🌾 Crop diversity
* 🔄 Crop rotation suitability

The system displays a recommendation score and score breakdown to help users understand the suggested crop.

---

## 🔄 Crop Rotation

Crop rotation helps improve sustainable farming practices by encouraging different types of crops in consecutive seasons.

For example:

```text
🌾 Rice
   ↓
🌱 Green Gram
   ↓
🌽 Maize
   ↓
🥜 Groundnut
```

Including legumes and pulses in crop rotation can help support soil fertility and crop diversity.

---

## 👨‍🌾 How to Use the Application

1. Select your preferred language.
2. Enter the farmer's name.
3. Enter the farm location.
4. Enter the land size in acres.
5. Select the soil type.
6. Select the available water level.
7. Select the current crop.
8. Select the previous crop if known.
9. Click **Generate Rotation Plan**.
10. View the recommended crop.
11. Check the recommendation score and score breakdown.
12. View the suggested crop rotation.
13. Explore alternative crop recommendations.
14. Read farm insights and recommendations.
15. Download the farm report.

---

## 🛠️ Technologies Used

| Technology    | Purpose                       |
| ------------- | ----------------------------- |
| 🐍 Python     | Core programming language     |
| 🎈 Streamlit  | Web application framework     |
| 🐼 Pandas     | Data processing               |
| 🌐 Requests   | HTTP requests                 |
| 🎨 HTML & CSS | Custom user interface styling |

---

## 📁 Project Structure

```text
smart-crop-rotation/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

The main application file contains:

* Streamlit interface
* Custom CSS styling
* Crop database
* Translation system
* Recommendation logic
* Crop scoring system
* Crop rotation planning
* Farm insights
* Report generation

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-crop-rotation.git
```

### 2. Open the Project Folder

```bash
cd smart-crop-rotation
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

Create a file named `requirements.txt` and add:

```text
streamlit
pandas
requests
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

After running the command, Streamlit will open the application in your browser.

---

## 📥 Farm Report

The application allows users to download a farm report containing:

* Farmer details
* Farm location
* Land size
* Soil type
* Water availability
* Current crop information
* Recommended next crop
* Recommendation score
* Suggested crop rotation
* General farming advice

---

## 💡 Farm Insights

The application provides useful farming insights based on the selected conditions.

### 💧 Low Water Availability

The system recommends crops that require less water, such as:

* Chickpea
* Green Gram
* Sorghum

### 🌱 Soil Health

Legume crops can help improve soil fertility by contributing to nitrogen fixation.

Examples include:

* Groundnut
* Soybean
* Chickpea
* Green Gram
* Black Gram

### 🌾 Crop Diversity

Crop rotation can help reduce dependency on a single crop and may help break certain pest and disease cycles.

---

## 🚀 Future Improvements

Future versions of the project can include:

### 🤖 Machine Learning

Use real agricultural datasets to train machine learning models for more accurate crop recommendations.

### 🌦️ Weather Integration

Integrate real-time data such as:

* Rainfall
* Temperature
* Humidity
* Weather forecasts

### 📍 Location-Based Recommendations

Provide crop suggestions based on:

* Region
* Climate
* Rainfall patterns
* Seasonal conditions

### 🧪 IoT Soil Monitoring

Integrate sensors to collect:

* Soil moisture
* Soil pH
* Temperature
* Humidity
* NPK values

### 📈 Market Price Integration

Consider current crop market prices to help farmers make economically beneficial decisions.

### 📱 Mobile Application

Develop a mobile-friendly version for easier access by farmers.

### 🌾 Expanded Crop Database

Add more:

* Crops
* Soil types
* Fertilizer recommendations
* Pest management information
* Regional farming practices

---

## ⚠️ Disclaimer

This application is designed as an **agricultural decision-support tool**.

The recommendations should be used as guidance. Actual crop selection should also consider:

* Local climate
* Rainfall
* Market prices
* Seed availability
* Irrigation facilities
* Pest and disease conditions
* Advice from agricultural experts

---



## 🌱 Project Goal

> **Helping farmers make smarter crop rotation decisions for healthier soil, efficient water management, and sustainable farming.**

---

### ⭐ If you like this project, consider giving the repository a star!
