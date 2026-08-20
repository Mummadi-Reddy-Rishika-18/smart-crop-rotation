🌱 Smart Crop Rotation
Optimal Crop Selection and Rotation Planning

Smart Crop Rotation is a data-driven crop planning and decision-support application designed to help farmers select suitable crops and plan crop rotations based on farm conditions.

Instead of repeatedly growing the same crop based only on habit, the application evaluates factors such as soil type, water availability, rainfall availability, season, current crop, and previous crop to recommend a suitable next crop and generate a 4-year crop rotation plan.

🎯 Problem Statement

Farmers often choose crops based on traditional practices or habit rather than considering current soil and environmental conditions. This can affect crop diversity, resource management, and long-term soil health.

Our Solution

Smart Crop Rotation provides a simple interface where farmers can enter their farm conditions and receive:

🌱 Recommended next crop
📊 Crop suitability score
💧 Water suitability
🌧️ Rainfall suitability
🪴 Soil suitability
🌱 Soil-health contribution
🌾 Crop-diversification score
🔄 4-year crop rotation plan
📈 Soil-health trend
💡 Farming insights
📄 Downloadable farm report
✨ Key Features
🌱 1. Crop Recommendation

The application evaluates candidate crops using a scoring system based on:

Water availability
Rainfall availability
Soil type
Season
Soil-health contribution
Crop diversification
Previous crop
Current crop repetition

Crops are ranked according to their total suitability score, and the highest-ranked crop is recommended.

🔄 2. Four-Year Crop Rotation

The application generates a 4-year crop rotation plan rather than recommending only a single crop.

The rotation encourages:

Crop diversity
Reduced repeated cropping
Inclusion of legume crops
Better resource management
Long-term soil-health awareness

The application also displays a soil-health trend for the four-year rotation.

Note: The soil-health trend is a heuristic estimate and is not a replacement for actual soil testing.

🌦️ 3. Location-Based Temperature

Farmers can enter a village, district, or city.

The application:

Converts the location into latitude and longitude using Open-Meteo's geocoding service.
Retrieves the current temperature.
Displays the temperature in the application dashboard.

No API key is required for this implementation.

🪴 4. Soil and Water Analysis

The application considers different soil conditions and water availability levels.

Water availability:

Low
Medium
High

Soil types include:

Loamy Soil
Clay Soil
Black Soil
Sandy Soil
Red Soil

These conditions contribute to the crop suitability score.

🌱 5. Soil Health and Legume Rotation

Legume crops receive a soil-health contribution in the scoring system.

The application uses crop diversification and legume information when evaluating rotations.

This helps encourage rotations containing crops such as pulses and legumes.

📊 6. Farm Performance Dashboard

The dashboard displays estimated indicators including:

💧 Water Usage
🌱 Soil Health
📈 Expected Yield
♻️ Sustainability Score

These are calculated using the application's scoring and heuristic formulas. They should be treated as decision-support indicators, not guaranteed agricultural predictions.

🌍 7. Multilingual Support

The application supports five languages:

🇬🇧 English
🇮🇳 Kannada
🇮🇳 Hindi
🇮🇳 Telugu
🇮🇳 Tamil

This helps make the application more accessible to farmers from different language backgrounds.

📄 8. Downloadable Farm Report

Users can generate a report containing:

Farmer details
Farm location
Temperature
Land size
Soil type
Water availability
Crop information
Recommended crop
Recommendation score
Rotation plan
General farming advice

🧠 Recommendation Method

The application uses a rule-based scoring approach.

The overall crop score is calculated from multiple factors:

Total Score =
    Water Score
  + Rainfall Score
  + Soil Score
  + Soil Health Score
  + Season Score
  + Diversification Score
  - Previous Crop Penalty
  - Same Crop Penalty

The candidate crops are then sorted according to their scores.

The highest-ranked crop becomes the recommended next crop.

🔄 How the Application Works
             FARM DETAILS
                  │
                  ▼
          Location & Temperature
                  │
                  ▼
        Soil + Water Conditions
                  │
                  ▼
       Current & Previous Crop
                  │
                  ▼
       Crop Suitability Scoring
                  │
                  ▼
        Rank Candidate Crops
                  │
                  ▼
       Recommended Next Crop
                  │
                  ▼
          4-Year Rotation
                  │
                  ▼
      Soil Health & Farm Insights
                  │
                  ▼
          Downloadable Report
🛠️ Technologies Used
Programming Language
Python
Framework
Streamlit
Libraries
Pandas
Requests
APIs
Open-Meteo Geocoding API
Open-Meteo Weather API
Core Approach
Rule-based crop suitability scoring
Crop rotation planning
Soil-health heuristics
Water compatibility scoring
Rainfall compatibility scoring
Crop diversification scoring
📦 Installation
1. Clone the repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
2. Install dependencies
pip install streamlit pandas requests
3. Run the application
streamlit run app.py
👨‍🌾 How to Use
Enter the farmer's name.
Enter the farm location.
Enter the land size.
Select the soil type.
Select water availability.
Select the current crop.
Select the previous crop if known.
Click Generate Rotation Plan.
View the recommended crop.
Check the suitability score and score breakdown.
View the 4-year rotation.
Review farm insights.
Download the farm report.

These steps are also reflected in the application's built-in instructions.

🌾 Expected Impact

Smart Crop Rotation aims to support farmers in making more informed crop-planning decisions.

Potential benefits
Better crop selection
Improved crop diversity
Better water-resource awareness
More structured crop rotation
Improved awareness of soil health
Reduced dependence on repeated cropping
More sustainable farm planning
⚠️ Disclaimer

Smart Crop Rotation is a decision-support application.

Its crop recommendations, soil-health scores, sustainability scores, and yield estimates are based on the application's crop data and heuristic scoring methods.

They should not be considered guaranteed predictions.

Farmers should also consider:

Local climate
Actual rainfall
Market prices
Seed availability
Irrigation facilities
Pest and disease conditions
Local farming practices
Advice from agricultural experts
🔮 Future Enhancements

Future versions could include:

🧪 Real-time NPK/soil sensor integration
🌧️ Detailed weather forecasting
🛰️ Satellite-based crop monitoring
🤖 Machine-learning-based prediction
💰 Live crop-market price integration
🐛 Pest and disease prediction
📍 Region-specific crop recommendations
📱 Mobile application
🗣️ Voice-based farmer assistance
📈 Historical farm data and analytics
🏆 Problem Statement Alignment
Problem Requirement	Smart Crop Rotation
Optimal crop selection	✅
Consider soil conditions	✅
Consider environmental conditions	✅
Crop rotation planning	✅
Improve crop diversity	✅
Consider water availability	✅
Support soil health	✅
Farmer-friendly interface	✅
Multi-language support	✅
Report generation	✅
Conclusion

Smart Crop Rotation directly addresses the problem of optimal crop selection and rotation planning by combining farm-condition inputs with a transparent crop-scoring system and multi-year rotation planning.

🌱 Vision

Smart Farming for a Better Tomorrow

Helping farmers make better-informed, sustainable crop-planning decisions through simple and accessible technology.
