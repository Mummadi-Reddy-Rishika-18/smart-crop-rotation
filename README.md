# smart-crop-rotation# 🌱 SmartCrop

## Optimal Crop Selection and Rotation Planning

SmartCrop is a machine-learning-based agricultural decision-support
prototype that recommends suitable crops based on soil and climate
conditions and generates a crop rotation plan.

---

## 🚜 Problem

Farmers may select crops based on habit or previous experience without
considering the current condition of the soil and climate.

This can contribute to:

- Poor crop suitability
- Inefficient nutrient usage
- Repeated cultivation of similar crops
- Reduced soil health
- Lower productivity

---

## 💡 Solution

SmartCrop analyzes:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Soil pH
- Temperature
- Humidity
- Rainfall

A Random Forest machine-learning model predicts a suitable crop.

A separate crop-rotation engine then suggests crops for subsequent
years.

---

## ✨ Features

### 🌱 Crop Recommendation

Predicts the most suitable crop based on field conditions.

### 📊 Suitability Score

Shows the model probability for the recommended crop.

### 🧪 Soil Health Score

Provides a simple prototype soil-health indicator.

### 🔄 Crop Rotation Planning

Generates a three-year crop rotation plan.

### 📈 Visual Dashboard

Displays crop probabilities and field parameters.

### 💡 Explainable Recommendation

Provides simple reasons behind the recommendation.

---

## 🧠 Machine Learning

The project uses:

**Random Forest Classifier**

Input features:

```text
N
P
K
Temperature
Humidity
pH
Rainfall