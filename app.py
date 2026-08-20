import streamlit as st
import pandas as pd
import requests

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Smart Crop Rotation",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: #f5f8f2;
        font-family: 'Inter', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #064d2b 0%, #073b24 100%);
        border-right: 1px solid rgba(255,255,255,0.10);
    }

    /* Sidebar labels/headings stay white */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }

    /* Text inputs and number inputs: white box + dark text */
    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] [data-baseweb="input"] {
        background: #ffffff !important;
        border-color: #d7ded9 !important;
        color: #173622 !important;
        -webkit-text-fill-color: #173622 !important;
    }

    section[data-testid="stSidebar"] input::placeholder {
        color: #7b8790 !important;
        opacity: 1 !important;
        -webkit-text-fill-color: #7b8790 !important;
    }

    /* Select boxes: white closed box + dark selected value */
    section[data-testid="stSidebar"] [data-baseweb="select"] > div {
        background: #ffffff !important;
        border-color: #d7ded9 !important;
        color: #173622 !important;
    }

    section[data-testid="stSidebar"] [data-baseweb="select"] span,
    section[data-testid="stSidebar"] [data-baseweb="select"] input,
    section[data-testid="stSidebar"] [data-baseweb="select"] div {
        color: #173622 !important;
        -webkit-text-fill-color: #173622 !important;
    }

    /* Dropdown menu opens outside the sidebar DOM, so style it globally */
    [data-baseweb="popover"],
    [data-baseweb="menu"],
    [role="listbox"] {
        background: #ffffff !important;
    }

    [role="option"] {
        color: #173622 !important;
        background: #ffffff !important;
    }

    [role="option"] * {
        color: #173622 !important;
        -webkit-text-fill-color: #173622 !important;
    }

    [role="option"]:hover {
        background: #eaf4e5 !important;
    }

    /* Select arrow */
    section[data-testid="stSidebar"] [data-baseweb="select"] svg {
        fill: #173622 !important;
    }

    .brand {
        padding: 8px 4px 20px 4px;
        border-bottom: 1px solid rgba(255,255,255,0.15);
        margin-bottom: 18px;
    }
    .brand-title {
        font-size: 25px;
        font-weight: 800;
        line-height: 1.05;
    }
    .brand-sub {
        margin-top: 8px;
        font-size: 13px;
        color: #d9efc9 !important;
        line-height: 1.5;
    }

    .hero {
        min-height: 230px;
        border-radius: 24px;
        padding: 42px 46px;
        margin: 4px 0 22px 0;
        display: flex;
        align-items: center;
        position: relative;
        overflow: hidden;
        background: linear-gradient(90deg, rgba(236,246,222,0.97) 0%, rgba(236,246,222,0.91) 44%, rgba(236,246,222,0.35) 72%, rgba(236,246,222,0.05) 100%);
        box-shadow: 0 10px 30px rgba(42,74,36,0.10);
        border: 1px solid rgba(65,112,55,0.10);
    }
    .hero:after {
        content: '';
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: center right;
        opacity: 0.70;
        z-index: 0;
    }
    .hero-content {
        position: relative;
        z-index: 2;
        max-width: 720px;
    }
    .hero-kicker {
        display: inline-block;
        padding: 7px 13px;
        border-radius: 999px;
        background: #dff0cf;
        color: #17623b;
        font-weight: 700;
        font-size: 13px;
        margin-bottom: 12px;
    }
    .hero h1 {
        margin: 0;
        color: #083f27;
        font-size: 43px;
        line-height: 1.08;
        font-weight: 800;
    }
    .hero p {
        color: #36533e;
        font-size: 17px;
        margin: 10px 0 0 0;
        max-width: 690px;
    }

    .metric-card {
        background: #ffffff;
        border: 1px solid #e4e9df;
        border-radius: 18px;
        padding: 18px 18px 15px 18px;
        min-height: 112px;
        box-shadow: 0 6px 20px rgba(35,67,38,0.07);
        margin-bottom: 18px;
    }
    .metric-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .metric-icon {
        font-size: 28px;
    }
    .metric-label {
        color: #68756c;
        font-size: 13px;
        font-weight: 600;
        margin-top: 8px;
    }
    .metric-value {
        color: #13281b;
        font-size: 20px;
        font-weight: 800;
        margin-top: 4px;
    }

    .section-title {
        color: #10281a;
        font-size: 24px;
        font-weight: 800;
        margin: 8px 0 14px 0;
    }

    .panel {
        background: #ffffff;
        border: 1px solid #e5e9e1;
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 7px 24px rgba(35,67,38,0.07);
        height: 100%;
    }
    .recommendation-panel {
        background: linear-gradient(135deg, #f7fbef 0%, #eef7df 100%);
        border: 1px solid #dfeacc;
    }
    .recommendation-badge {
        display: inline-block;
        background: #e2f1cf;
        color: #24633b;
        border-radius: 999px;
        padding: 6px 11px;
        font-size: 12px;
        font-weight: 800;
        margin-bottom: 10px;
    }
    .crop-name {
        font-size: 31px;
        font-weight: 800;
        color: #17683a;
        margin: 0 0 8px 0;
    }
    .score {
        font-size: 18px;
        color: #4d5f52;
        font-weight: 600;
        margin-bottom: 14px;
    }
    .score strong {
        color: #16723b;
        font-size: 29px;
    }
    .feature-line {
        padding: 8px 0;
        color: #344b3b;
        font-size: 14px;
    }

    .crop-image {
        width: 100%;
        height: 255px;
        object-fit: cover;
        border-radius: 16px;
        display: block;
    }

    .rotation-card {
        background: #ffffff;
        border: 1px solid #e6eae4;
        border-radius: 18px;
        padding: 11px;
        text-align: center;
        box-shadow: 0 6px 18px rgba(35,67,38,0.06);
    }
    .rotation-card img {
        width: 100%;
        height: 115px;
        object-fit: cover;
        border-radius: 13px;
    }
    .rotation-year {
        color: #647166;
        font-size: 12px;
        font-weight: 700;
        margin-top: 9px;
    }
    .rotation-name {
        color: #153622;
        font-size: 15px;
        font-weight: 800;
        margin-top: 3px;
    }
    .arrow {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 27px;
        color: #317348;
        height: 160px;
    }

    .score-card {
        background: white;
        border: 1px solid #e5e9e1;
        border-radius: 18px;
        padding: 18px;
        box-shadow: 0 6px 18px rgba(35,67,38,0.06);
        min-height: 135px;
    }
    .score-card-title {
        color: #526158;
        font-size: 13px;
        font-weight: 700;
    }
    .score-card-value {
        color: #17683a;
        font-size: 28px;
        font-weight: 800;
        margin-top: 5px;
    }
    .progress {
        height: 7px;
        border-radius: 10px;
        background: #e9eee7;
        overflow: hidden;
        margin-top: 10px;
    }
    .progress > div {
        height: 100%;
        border-radius: 10px;
        background: linear-gradient(90deg, #277346, #79a950);
    }

    .insight {
        background: #f6faef;
        border: 1px solid #e1ebd4;
        border-radius: 16px;
        padding: 17px;
        min-height: 150px;
    }
    .insight h4 {
        margin: 0 0 8px 0;
        color: #174b2d;
        font-size: 16px;
    }
    .insight p {
        color: #526057;
        font-size: 14px;
        line-height: 1.55;
    }

    .summary-item {
        padding: 10px 0;
        border-bottom: 1px solid #edf0eb;
        color: #435046;
        font-size: 14px;
    }
    .summary-item:last-child { border-bottom: none; }

    .quote-card {
        background: linear-gradient(135deg, #eff5df, #f9fbf3);
        border-radius: 18px;
        padding: 22px;
        border: 1px solid #e1e9d1;
        height: 100%;
    }
    .quote-card h3 {
        color: #15462b;
        margin: 0;
    }
    .quote-card p {
        color: #5b685e;
        line-height: 1.6;
    }

    .footer {
        text-align: center;
        color: #758078;
        padding: 28px 0 10px 0;
        font-size: 13px;
    }

    div.stButton > button {
        border-radius: 12px;
        font-weight: 700;
        min-height: 45px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# CROP DATABASE
# =========================================================

crop_data = {
    "Rice": {
        "water": "High",
        "nutrient": "High",
        "soil": ["Clay", "Loamy"],
        "season": ["Kharif"],
        "next": ["Green Gram", "Black Gram", "Groundnut"],
        "legume": False,
        "benefit": "Legume crops after rice can help improve soil nitrogen and diversify the cropping system."
    },

    "Wheat": {
        "water": "Medium",
        "nutrient": "Medium",
        "soil": ["Loamy"],
        "season": ["Rabi"],
        "next": ["Chickpea", "Green Gram", "Mustard"],
        "legume": False,
        "benefit": "Rotating wheat with pulses can help maintain soil fertility and reduce pest pressure."
    },

    "Maize": {
        "water": "Medium",
        "nutrient": "High",
        "soil": ["Loamy", "Red Soil"],
        "season": ["Kharif", "Rabi"],
        "next": ["Soybean", "Green Gram", "Groundnut"],
        "legume": False,
        "benefit": "Following maize with a legume can help restore nitrogen used by the cereal crop."
    },

    "Cotton": {
        "water": "Medium",
        "nutrient": "High",
        "soil": ["Black Soil"],
        "season": ["Kharif"],
        "next": ["Chickpea", "Wheat", "Green Gram"],
        "legume": False,
        "benefit": "Rotating cotton with pulses can improve soil health and help break pest cycles."
    },

    "Groundnut": {
        "water": "Medium",
        "nutrient": "Medium",
        "soil": ["Sandy", "Loamy", "Red Soil"],
        "season": ["Kharif"],
        "next": ["Wheat", "Maize", "Sorghum"],
        "legume": True,
        "benefit": "Groundnut is a nitrogen-fixing crop and can benefit crops planted after it."
    },

    "Soybean": {
        "water": "Medium",
        "nutrient": "Medium",
        "soil": ["Loamy", "Black Soil"],
        "season": ["Kharif"],
        "next": ["Wheat", "Maize", "Sorghum"],
        "legume": True,
        "benefit": "Soybean fixes atmospheric nitrogen and can contribute to improved soil fertility."
    },

    "Chickpea": {
        "water": "Low",
        "nutrient": "Low",
        "soil": ["Loamy", "Black Soil"],
        "season": ["Rabi"],
        "next": ["Maize", "Cotton", "Sorghum"],
        "legume": True,
        "benefit": "Chickpea is a low-water pulse that can improve nitrogen availability for subsequent crops."
    },

    "Green Gram": {
        "water": "Low",
        "nutrient": "Low",
        "soil": ["Sandy", "Loamy", "Red Soil"],
        "season": ["Kharif", "Summer"],
        "next": ["Wheat", "Rice", "Maize"],
        "legume": True,
        "benefit": "Green gram is a nitrogen-fixing pulse requiring relatively little water."
    },

    "Black Gram": {
        "water": "Low",
        "nutrient": "Low",
        "soil": ["Loamy", "Black Soil"],
        "season": ["Kharif", "Rabi"],
        "next": ["Rice", "Wheat", "Maize"],
        "legume": True,
        "benefit": "Black gram contributes to nitrogen fixation and helps diversify the crop rotation."
    },

    "Mustard": {
        "water": "Low",
        "nutrient": "Medium",
        "soil": ["Loamy", "Black Soil"],
        "season": ["Rabi"],
        "next": ["Green Gram", "Maize", "Cotton"],
        "legume": False,
        "benefit": "Mustard provides crop diversification and can help break some pest and disease cycles."
    },

    "Sorghum": {
        "water": "Low",
        "nutrient": "Medium",
        "soil": ["Black Soil", "Loamy", "Red Soil"],
        "season": ["Kharif", "Rabi"],
        "next": ["Chickpea", "Groundnut", "Green Gram"],
        "legume": False,
        "benefit": "Sorghum is relatively drought tolerant and works well with pulse-based rotations."
    }
}

# =========================================================
# CROP BENEFIT ("WHY") TRANSLATIONS
# =========================================================
# Localized versions of each crop's crop_data[...]["benefit"] text,
# used anywhere that reason is shown to the farmer (rotation timeline,
# report). English falls back to crop_data itself via translated_benefit().

crop_benefit_translations = {
    "Kannada": {
        "Rice": "ಅಕ್ಕಿಯ ನಂತರ ದ್ವಿದಳ ಧಾನ್ಯ ಬೆಳೆಗಳು ಮಣ್ಣಿನ ಸಾರಜನಕವನ್ನು ಸುಧಾರಿಸಲು ಮತ್ತು ಬೆಳೆ ಪದ್ಧತಿಯನ್ನು ವೈವಿಧ್ಯಗೊಳಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತವೆ.",
        "Wheat": "ಗೋಧಿಯನ್ನು ಬೇಳೆಕಾಳುಗಳೊಂದಿಗೆ ಪರ್ಯಾಯವಾಗಿ ಬೆಳೆಯುವುದು ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಕಾಪಾಡಲು ಮತ್ತು ಕೀಟ ಒತ್ತಡ ಕಡಿಮೆ ಮಾಡಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "Maize": "ಮೆಕ್ಕೆಜೋಳದ ನಂತರ ದ್ವಿದಳ ಧಾನ್ಯ ಬೆಳೆಯುವುದು ಧಾನ್ಯ ಬೆಳೆ ಬಳಸಿದ ಸಾರಜನಕವನ್ನು ಮರುಸ್ಥಾಪಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "Cotton": "ಹತ್ತಿಯನ್ನು ಬೇಳೆಕಾಳುಗಳೊಂದಿಗೆ ಪರ್ಯಾಯವಾಗಿ ಬೆಳೆಯುವುದು ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಸುಧಾರಿಸಲು ಮತ್ತು ಕೀಟ ಚಕ್ರ ಮುರಿಯಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "Groundnut": "ಕಡಲೆಕಾಯಿ ಸಾರಜನಕ-ಸ್ಥಿರೀಕರಣ ಬೆಳೆಯಾಗಿದ್ದು, ನಂತರ ನೆಡುವ ಬೆಳೆಗಳಿಗೆ ಪ್ರಯೋಜನಕಾರಿಯಾಗಬಹುದು.",
        "Soybean": "ಸೋಯಾಬೀನ್ ವಾತಾವರಣದ ಸಾರಜನಕವನ್ನು ಸ್ಥಿರೀಕರಿಸುತ್ತದೆ ಮತ್ತು ಮಣ್ಣಿನ ಫಲವತ್ತತೆ ಸುಧಾರಿಸಲು ಕೊಡುಗೆ ನೀಡಬಹುದು.",
        "Chickpea": "ಕಡಲೆ ಕಡಿಮೆ ನೀರು ಬಯಸುವ ಬೇಳೆಯಾಗಿದ್ದು, ನಂತರದ ಬೆಳೆಗಳಿಗೆ ಸಾರಜನಕ ಲಭ್ಯತೆ ಸುಧಾರಿಸಬಹುದು.",
        "Green Gram": "ಹೆಸರುಕಾಳು ತುಲನಾತ್ಮಕವಾಗಿ ಕಡಿಮೆ ನೀರು ಬಯಸುವ ಸಾರಜನಕ-ಸ್ಥಿರೀಕರಣ ಬೇಳೆಯಾಗಿದೆ.",
        "Black Gram": "ಉದ್ದು ಸಾರಜನಕ ಸ್ಥಿರೀಕರಣಕ್ಕೆ ಕೊಡುಗೆ ನೀಡುತ್ತದೆ ಮತ್ತು ಬೆಳೆ ಪರ್ಯಾಯವನ್ನು ವೈವಿಧ್ಯಗೊಳಿಸಲು ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "Mustard": "ಸಾಸಿವೆ ಬೆಳೆ ವೈವಿಧ್ಯತೆ ನೀಡುತ್ತದೆ ಮತ್ತು ಕೆಲವು ಕೀಟ ಮತ್ತು ರೋಗ ಚಕ್ರಗಳನ್ನು ಮುರಿಯಲು ಸಹಾಯ ಮಾಡಬಹುದು.",
        "Sorghum": "ಜೋಳ ತುಲನಾತ್ಮಕವಾಗಿ ಬರ ಸಹಿಷ್ಣುವಾಗಿದ್ದು, ಬೇಳೆ ಆಧಾರಿತ ಪರ್ಯಾಯಗಳೊಂದಿಗೆ ಚೆನ್ನಾಗಿ ಕೆಲಸ ಮಾಡುತ್ತದೆ.",
    },
    "Hindi": {
        "Rice": "चावल के बाद दलहनी फसलें मिट्टी की नाइट्रोजन सुधारने और फसल प्रणाली में विविधता लाने में मदद कर सकती हैं।",
        "Wheat": "गेहूं को दलहन के साथ चक्रित करने से मिट्टी की उर्वरता बनाए रखने और कीट दबाव कम करने में मदद मिल सकती है।",
        "Maize": "मक्का के बाद दलहन उगाने से अनाज की फसल द्वारा उपयोग की गई नाइट्रोजन को पुनर्स्थापित करने में मदद मिल सकती है।",
        "Cotton": "कपास को दलहन के साथ चक्रित करने से मिट्टी का स्वास्थ्य सुधर सकता है और कीट चक्र टूट सकता है।",
        "Groundnut": "मूंगफली एक नाइट्रोजन-स्थिरीकरण फसल है और इसके बाद लगाई गई फसलों को लाभ पहुंचा सकती है।",
        "Soybean": "सोयाबीन वायुमंडलीय नाइट्रोजन को स्थिर करता है और मिट्टी की उर्वरता में सुधार कर सकता है।",
        "Chickpea": "चना कम पानी वाली दलहन है जो बाद की फसलों के लिए नाइट्रोजन उपलब्धता सुधार सकती है।",
        "Green Gram": "मूंग अपेक्षाकृत कम पानी चाहने वाली नाइट्रोजन-स्थिरीकरण दलहन है।",
        "Black Gram": "उड़द नाइट्रोजन स्थिरीकरण में योगदान देता है और फसल चक्र में विविधता लाने में मदद करता है।",
        "Mustard": "सरसों फसल विविधता प्रदान करती है और कुछ कीट व रोग चक्रों को तोड़ने में मदद कर सकती है।",
        "Sorghum": "ज्वार अपेक्षाकृत सूखा-सहिष्णु है और दलहन-आधारित चक्रों के साथ अच्छी तरह काम करता है।",
    },
    "Telugu": {
        "Rice": "వరి తర్వాత పప్పుధాన్య పంటలు నేల నత్రజనిని మెరుగుపరచడంలో మరియు పంట విధానాన్ని వైవిధ్యపరచడంలో సహాయపడతాయి.",
        "Wheat": "గోధుమను పప్పుధాన్యాలతో మార్చడం నేల సారాన్ని కాపాడటానికి మరియు తెగుళ్ల ఒత్తిడిని తగ్గించడానికి సహాయపడుతుంది.",
        "Maize": "మొక్కజొన్న తర్వాత పప్పుధాన్యం వేయడం ధాన్యపు పంట వాడిన నత్రజనిని పునరుద్ధరించడంలో సహాయపడుతుంది.",
        "Cotton": "పత్తిని పప్పుధాన్యాలతో మార్చడం నేల ఆరోగ్యాన్ని మెరుగుపరచి తెగుళ్ల చక్రాలను విచ్ఛిన్నం చేయడంలో సహాయపడుతుంది.",
        "Groundnut": "వేరుశెనగ నత్రజని-స్థిరీకరణ పంట, తర్వాత వేసే పంటలకు ప్రయోజనం చేకూరుస్తుంది.",
        "Soybean": "సోయాబీన్ వాతావరణ నత్రజనిని స్థిరీకరిస్తుంది మరియు నేల సారాన్ని మెరుగుపరచడానికి దోహదపడుతుంది.",
        "Chickpea": "శనగ తక్కువ నీటి అవసరమున్న పప్పుధాన్యం, తర్వాతి పంటలకు నత్రజని లభ్యతను మెరుగుపరచగలదు.",
        "Green Gram": "పెసలు తక్కువ నీరు అవసరమయ్యే నత్రజని-స్థిరీకరణ పప్పుధాన్యం.",
        "Black Gram": "మినుములు నత్రజని స్థిరీకరణకు దోహదపడతాయి మరియు పంట మార్పిడిని వైవిధ్యపరచడంలో సహాయపడతాయి.",
        "Mustard": "ఆవాలు పంట వైవిధ్యాన్ని అందిస్తాయి మరియు కొన్ని తెగుళ్లు మరియు వ్యాధి చక్రాలను విచ్ఛిన్నం చేయడంలో సహాయపడతాయి.",
        "Sorghum": "జొన్న సాపేక్షంగా కరువును తట్టుకుంటుంది మరియు పప్పుధాన్య ఆధారిత మార్పిడులతో బాగా పనిచేస్తుంది.",
    },
    "Tamil": {
        "Rice": "நெல்லுக்குப் பிறகு பருப்பு வகைப் பயிர்கள் மண் நைட்ரஜனை மேம்படுத்தவும் பயிர் முறையை பல்வகைப்படுத்தவும் உதவும்.",
        "Wheat": "கோதுமையை பருப்பு வகைகளுடன் சுழற்சி செய்வது மண் வளத்தை பராமரிக்கவும் பூச்சி அழுத்தத்தை குறைக்கவும் உதவும்.",
        "Maize": "மக்காச்சோளத்திற்குப் பிறகு பருப்பு வகை பயிரிடுவது தானியப் பயிர் பயன்படுத்திய நைட்ரஜனை மீட்டெடுக்க உதவும்.",
        "Cotton": "பருத்தியை பருப்பு வகைகளுடன் சுழற்சி செய்வது மண் ஆரோக்கியத்தை மேம்படுத்தி பூச்சி சுழற்சிகளை உடைக்க உதவும்.",
        "Groundnut": "நிலக்கடலை நைட்ரஜன்-நிலைப்படுத்தும் பயிராகும், பின்னர் நடப்படும் பயிர்களுக்கு நன்மை பயக்கும்.",
        "Soybean": "சோயாபீன் வளிமண்டல நைட்ரஜனை நிலைப்படுத்தி மண் வளத்தை மேம்படுத்த பங்களிக்கும்.",
        "Chickpea": "கொண்டைக்கடலை குறைந்த நீர் தேவைப்படும் பருப்பு வகையாகும், அடுத்த பயிர்களுக்கு நைட்ரஜன் கிடைப்பை மேம்படுத்தும்.",
        "Green Gram": "பச்சைப்பயறு ஒப்பீட்டளவில் குறைந்த நீர் தேவைப்படும் நைட்ரஜன்-நிலைப்படுத்தும் பருப்பு வகையாகும்.",
        "Black Gram": "உளுந்து நைட்ரஜன் நிலைப்படுத்தலுக்கு பங்களித்து பயிர் சுழற்சியை பல்வகைப்படுத்த உதவும்.",
        "Mustard": "கடுகு பயிர் பல்வகைமையை வழங்கி சில பூச்சி மற்றும் நோய் சுழற்சிகளை உடைக்க உதவும்.",
        "Sorghum": "சோளம் ஒப்பீட்டளவில் வறட்சியை தாங்கும் தன்மை கொண்டது மற்றும் பருப்பு அடிப்படையிலான சுழற்சிகளுடன் நன்றாக செயல்படும்.",
    },
}

# =========================================================
# CROP TRANSLATIONS
# =========================================================

crop_names = {
    "English": {
        "Rice": "Rice",
        "Wheat": "Wheat",
        "Maize": "Maize",
        "Cotton": "Cotton",
        "Groundnut": "Groundnut",
        "Soybean": "Soybean",
        "Chickpea": "Chickpea",
        "Green Gram": "Green Gram",
        "Black Gram": "Black Gram",
        "Mustard": "Mustard",
        "Sorghum": "Sorghum"
    },

    "Kannada": {
        "Rice": "ಅಕ್ಕಿ",
        "Wheat": "ಗೋಧಿ",
        "Maize": "ಮೆಕ್ಕೆಜೋಳ",
        "Cotton": "ಹತ್ತಿ",
        "Groundnut": "ಕಡಲೆಕಾಯಿ",
        "Soybean": "ಸೋಯಾಬೀನ್",
        "Chickpea": "ಕಡಲೆ",
        "Green Gram": "ಹೆಸರುಕಾಳು",
        "Black Gram": "ಉದ್ದು",
        "Mustard": "ಸಾಸಿವೆ",
        "Sorghum": "ಜೋಳ"
    },

    "Hindi": {
        "Rice": "चावल",
        "Wheat": "गेहूँ",
        "Maize": "मक्का",
        "Cotton": "कपास",
        "Groundnut": "मूंगफली",
        "Soybean": "सोयाबीन",
        "Chickpea": "चना",
        "Green Gram": "मूंग",
        "Black Gram": "उड़द",
        "Mustard": "सरसों",
        "Sorghum": "ज्वार"
    },

    "Telugu": {
        "Rice": "వరి",
        "Wheat": "గోధుమ",
        "Maize": "మొక్కజొన్న",
        "Cotton": "పత్తి",
        "Groundnut": "వేరుశెనగ",
        "Soybean": "సోయాబీన్",
        "Chickpea": "శనగ",
        "Green Gram": "పెసలు",
        "Black Gram": "మినుములు",
        "Mustard": "ఆవాలు",
        "Sorghum": "జొన్న"
    },

    "Tamil": {
        "Rice": "நெல்",
        "Wheat": "கோதுமை",
        "Maize": "மக்காச்சோளம்",
        "Cotton": "பருத்தி",
        "Groundnut": "நிலக்கடலை",
        "Soybean": "சோயாபீன்",
        "Chickpea": "கொண்டைக்கடலை",
        "Green Gram": "பச்சைப்பயறு",
        "Black Gram": "உளுந்து",
        "Mustard": "கடுகு",
        "Sorghum": "சோளம்"
    }
}

# =========================================================
# SOIL TRANSLATIONS
# =========================================================

soil_names = {
    "English": {
        "Loamy": "Loamy",
        "Clay": "Clay",
        "Black Soil": "Black Soil",
        "Sandy": "Sandy",
        "Red Soil": "Red Soil"
    },

    "Kannada": {
        "Loamy": "ಲೋಮಿ ಮಣ್ಣು",
        "Clay": "ಜೇಡಿ ಮಣ್ಣು",
        "Black Soil": "ಕಪ್ಪು ಮಣ್ಣು",
        "Sandy": "ಮರಳು ಮಣ್ಣು",
        "Red Soil": "ಕೆಂಪು ಮಣ್ಣು"
    },

    "Hindi": {
        "Loamy": "दोमट मिट्टी",
        "Clay": "चिकनी मिट्टी",
        "Black Soil": "काली मिट्टी",
        "Sandy": "रेतीली मिट्टी",
        "Red Soil": "लाल मिट्टी"
    },

    "Telugu": {
        "Loamy": "లోమీ నేల",
        "Clay": "బంకమట్టి",
        "Black Soil": "నల్ల నేల",
        "Sandy": "ఇసుక నేల",
        "Red Soil": "ఎర్ర నేల"
    },

    "Tamil": {
        "Loamy": "வண்டல் மண்",
        "Clay": "களிமண்",
        "Black Soil": "கரிசல் மண்",
        "Sandy": "மணல் மண்",
        "Red Soil": "செம்மண்"
    }
}

# =========================================================
# VALUE TRANSLATIONS
# =========================================================

value_names = {
    "English": {
        "Low": "Low",
        "Medium": "Medium",
        "High": "High",
        "Kharif": "Kharif",
        "Rabi": "Rabi",
        "Summer": "Summer"
    },

    "Kannada": {
        "Low": "ಕಡಿಮೆ",
        "Medium": "ಮಧ್ಯಮ",
        "High": "ಹೆಚ್ಚು",
        "Kharif": "ಖರೀಫ್",
        "Rabi": "ರಬಿ",
        "Summer": "ಬೇಸಿಗೆ"
    },

    "Hindi": {
        "Low": "कम",
        "Medium": "मध्यम",
        "High": "अधिक",
        "Kharif": "खरीफ",
        "Rabi": "रबी",
        "Summer": "ग्रीष्म"
    },

    "Telugu": {
        "Low": "తక్కువ",
        "Medium": "మధ్యస్థ",
        "High": "అధిక",
        "Kharif": "ఖరీఫ్",
        "Rabi": "రబీ",
        "Summer": "వేసవి"
    },

    "Tamil": {
        "Low": "குறைவு",
        "Medium": "மிதமான",
        "High": "அதிகம்",
        "Kharif": "கரீஃப்",
        "Rabi": "ரபி",
        "Summer": "கோடை"
    }
}

# =========================================================
# TRANSLATIONS
# =========================================================

translations = {
    "English": {
        "title": "🌱 Smart Crop Rotation",
        "subtitle": "AI-assisted crop rotation planning for healthier soil, better water management and sustainable farming.",
        "language": "🌐 Select Language",
        "farm_details": "🌾 Farm Details",
        "farmer_name": "Farmer Name",
        "farmer_placeholder": "Enter your name",
        "location": "Location",
        "location_placeholder": "Village / District",
        "land_size": "Land Size (acres)",
        "soil_type": "Soil Type",
        "water": "Water Availability",
        "current_crop": "Current Crop",
        "previous_crop": "Previous Crop",
        "none": "None",
        "generate": "🌱 Generate Rotation Plan",
        "soil_health": "Soil Health",
        "water_management": "Water Management",
        "crop_diversity": "Crop Diversity",
        "smart_recommendation": "Smart Recommendation",
        "crop_information": "🌾 Current Crop Information",
        "water_requirement": "Water Requirement",
        "nutrient_requirement": "Nutrient Requirement",
        "suitable_soil": "Suitable Soil",
        "growing_season": "Growing Season",
        "recommended": "🌱 Recommended Next Crop",
        "recommendation_score": "Recommendation Score",
        "score_breakdown": "📊 Recommendation Score Breakdown",
        "water_score": "💧 Water",
        "soil_score": "🪴 Soil",
        "soil_health_score": "🌱 Soil Health",
        "diversity_score": "🌾 Diversity",
        "rotation": "🔄 Suggested Crop Rotation",
        "current": "Current Crop",
        "season": "Season",
        "all_seasons": "All Seasons",
        "alternatives": "📋 Alternative Crop Recommendations",
        "reason": "Reason",
        "insights": "💡 Farm Insights",
        "water_saving": "💧 Water Saving Tip",
        "low_water_message": "Your farm has low water availability. Prefer drought-tolerant crops and pulses such as chickpea, green gram and sorghum.",
        "water_management_title": "💧 Water Management",
        "medium_water_message": "Medium water availability allows a balanced combination of cereals, pulses and oilseeds.",
        "water_availability_title": "💧 Water Availability",
        "high_water_message": "High water availability provides more crop choices, but efficient irrigation is still recommended to avoid unnecessary water use.",
        "soil_health_benefit": "🌱 Soil Health Benefit",
        "legume_message": "The recommended crop is a pulse/legume. Legume crops can contribute to nitrogen fixation and support long-term soil fertility.",
        "rotation_benefit": "🌍 Rotation Benefit",
        "rotation_message": "Crop diversification can help reduce dependence on a single crop and may help break certain pest and disease cycles.",
        "farm_summary": "📋 Farm Summary",
        "farmer_details": "👨‍🌾 Farmer Details",
        "crop_details": "🌾 Crop Details",
        "farmer": "Farmer",
        "land": "Land Size",
        "recommended_crop": "Recommended Crop",
        "farm_report": "📥 Farm Report",
        "download_report": "📥 Download Farm Report",
        "how_to_use": "👨‍🌾 How to Use the App",
        "step1": "Enter your farmer details in the sidebar.",
        "step2": "Select your soil type.",
        "step3": "Select the available water level.",
        "step4": "Select your current crop.",
        "step5": "Select the previous crop if known.",
        "step6": "Click Generate Rotation Plan.",
        "step7": "View the recommended crop, rotation plan, farm insights and downloadable report.",
        "not_provided": "Not provided",
        "no_recommendation": "No suitable crop recommendation was found. Please try different farm conditions.",
        "report_title": "SMART CROP ROTATION REPORT",
        "report_soil_water": "SOIL & WATER",
        "report_crop_info": "CROP INFORMATION",
        "report_recommended": "RECOMMENDED NEXT CROP",
        "report_rotation": "SUGGESTED ROTATION",
        "report_general": "GENERAL ADVICE",
        "report_advice": "Use crop rotation as a decision-support guide. Actual crop selection should also consider local climate, rainfall, market prices, seed availability, irrigation facilities and agricultural expert advice.",
        "footer": "🌱 Smart Crop Rotation | Sustainable Farming Decision Support System"
    },

    "Kannada": {
        "title": "🌱 ಸ್ಮಾರ್ಟ್ ಬೆಳೆ ಪರ್ಯಾಯ",
        "subtitle": "ಆರೋಗ್ಯಕರ ಮಣ್ಣು, ಉತ್ತಮ ನೀರಿನ ನಿರ್ವಹಣೆ ಮತ್ತು ಸುಸ್ಥಿರ ಕೃಷಿಗಾಗಿ AI ಆಧಾರಿತ ಬೆಳೆ ಪರ್ಯಾಯ ಯೋಜನೆ.",
        "language": "🌐 ಭಾಷೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "farm_details": "🌾 ಕೃಷಿ ವಿವರಗಳು",
        "farmer_name": "ರೈತರ ಹೆಸರು",
        "farmer_placeholder": "ನಿಮ್ಮ ಹೆಸರನ್ನು ನಮೂದಿಸಿ",
        "location": "ಸ್ಥಳ",
        "location_placeholder": "ಗ್ರಾಮ / ಜಿಲ್ಲೆ",
        "land_size": "ಜಮೀನಿನ ಗಾತ್ರ (ಎಕರೆ)",
        "soil_type": "ಮಣ್ಣಿನ ಪ್ರಕಾರ",
        "water": "ನೀರಿನ ಲಭ್ಯತೆ",
        "current_crop": "ಪ್ರಸ್ತುತ ಬೆಳೆ",
        "previous_crop": "ಹಿಂದಿನ ಬೆಳೆ",
        "none": "ಯಾವುದೂ ಇಲ್ಲ",
        "generate": "🌱 ಬೆಳೆ ಪರ್ಯಾಯ ಯೋಜನೆ ರಚಿಸಿ",
        "soil_health": "ಮಣ್ಣಿನ ಆರೋಗ್ಯ",
        "water_management": "ನೀರಿನ ನಿರ್ವಹಣೆ",
        "crop_diversity": "ಬೆಳೆ ವೈವಿಧ್ಯತೆ",
        "smart_recommendation": "ಸ್ಮಾರ್ಟ್ ಶಿಫಾರಸು",
        "crop_information": "🌾 ಪ್ರಸ್ತುತ ಬೆಳೆಯ ಮಾಹಿತಿ",
        "water_requirement": "ನೀರಿನ ಅವಶ್ಯಕತೆ",
        "nutrient_requirement": "ಪೋಷಕಾಂಶದ ಅವಶ್ಯಕತೆ",
        "suitable_soil": "ಸೂಕ್ತ ಮಣ್ಣು",
        "growing_season": "ಬೆಳೆಯುವ ಋತು",
        "recommended": "🌱 ಶಿಫಾರಸು ಮಾಡಲಾದ ಮುಂದಿನ ಬೆಳೆ",
        "recommendation_score": "ಶಿಫಾರಸು ಅಂಕ",
        "score_breakdown": "📊 ಶಿಫಾರಸು ಅಂಕಗಳ ವಿವರ",
        "water_score": "💧 ನೀರು",
        "soil_score": "🪴 ಮಣ್ಣು",
        "soil_health_score": "🌱 ಮಣ್ಣಿನ ಆರೋಗ್ಯ",
        "diversity_score": "🌾 ವೈವಿಧ್ಯತೆ",
        "rotation": "🔄 ಸೂಚಿಸಲಾದ ಬೆಳೆ ಪರ್ಯಾಯ",
        "current": "ಪ್ರಸ್ತುತ ಬೆಳೆ",
        "season": "ಋತು",
        "all_seasons": "ಎಲ್ಲಾ ಋತುಗಳು",
        "alternatives": "📋 ಪರ್ಯಾಯ ಬೆಳೆ ಶಿಫಾರಸುಗಳು",
        "reason": "ಕಾರಣ",
        "insights": "💡 ಕೃಷಿ ಮಾಹಿತಿ",
        "water_saving": "💧 ನೀರು ಉಳಿಸುವ ಸಲಹೆ",
        "low_water_message": "ನಿಮ್ಮ ಜಮೀನಿನಲ್ಲಿ ನೀರಿನ ಲಭ್ಯತೆ ಕಡಿಮೆ ಇದೆ. ಕಡಿಮೆ ನೀರು ಅಗತ್ಯವಿರುವ ಕಡಲೆ, ಹೆಸರುಕಾಳು ಮತ್ತು ಜೋಳದಂತಹ ಬೆಳೆಗಳನ್ನು ಆಯ್ಕೆ ಮಾಡುವುದು ಉತ್ತಮ.",
        "water_management_title": "💧 ನೀರಿನ ನಿರ್ವಹಣೆ",
        "medium_water_message": "ಮಧ್ಯಮ ನೀರಿನ ಲಭ್ಯತೆಯು ಧಾನ್ಯಗಳು, ಬೇಳೆಕಾಳುಗಳು ಮತ್ತು ಎಣ್ಣೆಕಾಳುಗಳ ಸಮತೋಲನದ ಸಂಯೋಜನೆಗೆ ಅನುಕೂಲಕರವಾಗಿದೆ.",
        "water_availability_title": "💧 ನೀರಿನ ಲಭ್ಯತೆ",
        "high_water_message": "ಹೆಚ್ಚಿನ ನೀರಿನ ಲಭ್ಯತೆಯು ಹೆಚ್ಚಿನ ಬೆಳೆ ಆಯ್ಕೆಗಳನ್ನು ನೀಡುತ್ತದೆ. ಆದರೆ ನೀರನ್ನು ವ್ಯರ್ಥ ಮಾಡದಂತೆ ಪರಿಣಾಮಕಾರಿ ನೀರಾವರಿ ಅಗತ್ಯ.",
        "soil_health_benefit": "🌱 ಮಣ್ಣಿನ ಆರೋಗ್ಯದ ಪ್ರಯೋಜನ",
        "legume_message": "ಶಿಫಾರಸು ಮಾಡಲಾದ ಬೆಳೆ ಬೇಳೆಕಾಳು/ದ್ವಿದಳ ಧಾನ್ಯವಾಗಿದೆ. ಇವು ಸಾರಜನಕ ಸ್ಥಿರೀಕರಣಕ್ಕೆ ಸಹಾಯ ಮಾಡಿ ಮಣ್ಣಿನ ಫಲವತ್ತತೆಯನ್ನು ಸುಧಾರಿಸಬಹುದು.",
        "rotation_benefit": "🌍 ಬೆಳೆ ಪರ್ಯಾಯದ ಪ್ರಯೋಜನ",
        "rotation_message": "ಬೆಳೆ ವೈವಿಧ್ಯತೆಯು ಒಂದೇ ಬೆಳೆಯ ಮೇಲಿನ ಅವಲಂಬನೆಯನ್ನು ಕಡಿಮೆ ಮಾಡಿ ಕೆಲವು ಕೀಟ ಮತ್ತು ರೋಗಗಳ ಚಕ್ರವನ್ನು ಮುರಿಯಲು ಸಹಾಯ ಮಾಡಬಹುದು.",
        "farm_summary": "📋 ಕೃಷಿ ಸಾರಾಂಶ",
        "farmer_details": "👨‍🌾 ರೈತರ ವಿವರಗಳು",
        "crop_details": "🌾 ಬೆಳೆ ವಿವರಗಳು",
        "farmer": "ರೈತ",
        "land": "ಜಮೀನಿನ ಗಾತ್ರ",
        "recommended_crop": "ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ",
        "farm_report": "📥 ಕೃಷಿ ವರದಿ",
        "download_report": "📥 ಕೃಷಿ ವರದಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "how_to_use": "👨‍🌾 ಅಪ್ಲಿಕೇಶನ್ ಬಳಸುವುದು ಹೇಗೆ",
        "step1": "ಸೈಡ್‌ಬಾರ್‌ನಲ್ಲಿ ರೈತರ ವಿವರಗಳನ್ನು ನಮೂದಿಸಿ.",
        "step2": "ನಿಮ್ಮ ಮಣ್ಣಿನ ಪ್ರಕಾರವನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "step3": "ನೀರಿನ ಲಭ್ಯತೆಯ ಮಟ್ಟವನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "step4": "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "step5": "ತಿಳಿದಿದ್ದರೆ ಹಿಂದಿನ ಬೆಳೆಯನ್ನು ಆಯ್ಕೆಮಾಡಿ.",
        "step6": "ಬೆಳೆ ಪರ್ಯಾಯ ಯೋಜನೆ ರಚಿಸಿ ಎಂಬ ಬಟನ್ ಒತ್ತಿರಿ.",
        "step7": "ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ, ಬೆಳೆ ಪರ್ಯಾಯ ಯೋಜನೆ, ಕೃಷಿ ಮಾಹಿತಿ ಮತ್ತು ವರದಿಯನ್ನು ವೀಕ್ಷಿಸಿ.",
        "not_provided": "ನಮೂದಿಸಲಾಗಿಲ್ಲ",
        "no_recommendation": "ಸೂಕ್ತವಾದ ಬೆಳೆ ಶಿಫಾರಸು ಕಂಡುಬಂದಿಲ್ಲ. ದಯವಿಟ್ಟು ಬೇರೆ ಕೃಷಿ ಪರಿಸ್ಥಿತಿಗಳನ್ನು ಪ್ರಯತ್ನಿಸಿ.",
        "report_title": "ಸ್ಮಾರ್ಟ್ ಬೆಳೆ ಪರ್ಯಾಯ ವರದಿ",
        "report_soil_water": "ಮಣ್ಣು ಮತ್ತು ನೀರು",
        "report_crop_info": "ಬೆಳೆ ಮಾಹಿತಿ",
        "report_recommended": "ಶಿಫಾರಸು ಮಾಡಿದ ಮುಂದಿನ ಬೆಳೆ",
        "report_rotation": "ಸೂಚಿಸಲಾದ ಬೆಳೆ ಪರ್ಯಾಯ",
        "report_general": "ಸಾಮಾನ್ಯ ಸಲಹೆ",
        "report_advice": "ಬೆಳೆ ಪರ್ಯಾಯವನ್ನು ನಿರ್ಧಾರ ಸಹಾಯಕ ಮಾರ್ಗದರ್ಶಿಯಾಗಿ ಬಳಸಿ. ನಿಜವಾದ ಬೆಳೆ ಆಯ್ಕೆಯಲ್ಲಿ ಸ್ಥಳೀಯ ಹವಾಮಾನ, ಮಳೆ, ಮಾರುಕಟ್ಟೆ ಬೆಲೆ, ಬೀಜ ಲಭ್ಯತೆ, ನೀರಾವರಿ ಸೌಲಭ್ಯ ಮತ್ತು ಕೃಷಿ ತಜ್ಞರ ಸಲಹೆಯನ್ನು ಪರಿಗಣಿಸಿ.",
        "footer": "🌱 ಸ್ಮಾರ್ಟ್ ಬೆಳೆ ಪರ್ಯಾಯ | ಸುಸ್ಥಿರ ಕೃಷಿ ನಿರ್ಧಾರ ಸಹಾಯಕ ವ್ಯವಸ್ಥೆ"
    },

    "Hindi": {
        "title": "🌱 स्मार्ट फसल चक्र",
        "subtitle": "स्वस्थ मिट्टी, बेहतर जल प्रबंधन और टिकाऊ खेती के लिए AI आधारित फसल चक्र योजना।",
        "language": "🌐 भाषा चुनें",
        "farm_details": "🌾 खेत की जानकारी",
        "farmer_name": "किसान का नाम",
        "farmer_placeholder": "अपना नाम दर्ज करें",
        "location": "स्थान",
        "location_placeholder": "गाँव / जिला",
        "land_size": "भूमि का आकार (एकड़)",
        "soil_type": "मिट्टी का प्रकार",
        "water": "पानी की उपलब्धता",
        "current_crop": "वर्तमान फसल",
        "previous_crop": "पिछली फसल",
        "none": "कोई नहीं",
        "generate": "🌱 फसल चक्र योजना बनाएं",
        "soil_health": "मिट्टी का स्वास्थ्य",
        "water_management": "जल प्रबंधन",
        "crop_diversity": "फसल विविधता",
        "smart_recommendation": "स्मार्ट सुझाव",
        "crop_information": "🌾 वर्तमान फसल की जानकारी",
        "water_requirement": "पानी की आवश्यकता",
        "nutrient_requirement": "पोषक तत्वों की आवश्यकता",
        "suitable_soil": "उपयुक्त मिट्टी",
        "growing_season": "बुवाई का मौसम",
        "recommended": "🌱 अगली अनुशंसित फसल",
        "recommendation_score": "अनुशंसा स्कोर",
        "score_breakdown": "📊 अनुशंसा स्कोर विवरण",
        "water_score": "💧 पानी",
        "soil_score": "🪴 मिट्टी",
        "soil_health_score": "🌱 मिट्टी का स्वास्थ्य",
        "diversity_score": "🌾 विविधता",
        "rotation": "🔄 सुझाया गया फसल चक्र",
        "current": "वर्तमान फसल",
        "season": "मौसम",
        "all_seasons": "सभी मौसम",
        "alternatives": "📋 वैकल्पिक फसल सुझाव",
        "reason": "कारण",
        "insights": "💡 खेती संबंधी जानकारी",
        "water_saving": "💧 पानी बचाने की सलाह",
        "low_water_message": "आपके खेत में पानी की उपलब्धता कम है। चना, मूंग और ज्वार जैसी कम पानी वाली फसलों को प्राथमिकता दें।",
        "water_management_title": "💧 जल प्रबंधन",
        "medium_water_message": "मध्यम पानी की उपलब्धता अनाज, दलहन और तिलहन के संतुलित संयोजन के लिए उपयुक्त है।",
        "water_availability_title": "💧 पानी की उपलब्धता",
        "high_water_message": "अधिक पानी की उपलब्धता से फसल के अधिक विकल्प मिलते हैं। फिर भी पानी का कुशल उपयोग आवश्यक है।",
        "soil_health_benefit": "🌱 मिट्टी के स्वास्थ्य का लाभ",
        "legume_message": "अनुशंसित फसल दलहन है। दलहनी फसलें नाइट्रोजन स्थिरीकरण में सहायता करके मिट्टी की उर्वरता को बढ़ा सकती हैं।",
        "rotation_benefit": "🌍 फसल चक्र का लाभ",
        "rotation_message": "फसल विविधता एक ही फसल पर निर्भरता कम कर सकती है और कुछ कीट एवं रोग चक्रों को तोड़ने में मदद कर सकती है।",
        "farm_summary": "📋 खेत का सारांश",
        "farmer_details": "👨‍🌾 किसान का विवरण",
        "crop_details": "🌾 फसल का विवरण",
        "farmer": "किसान",
        "land": "भूमि का आकार",
        "recommended_crop": "अनुशंसित फसल",
        "farm_report": "📥 खेत की रिपोर्ट",
        "download_report": "📥 खेत की रिपोर्ट डाउनलोड करें",
        "how_to_use": "👨‍🌾 ऐप का उपयोग कैसे करें",
        "step1": "साइडबार में किसान की जानकारी दर्ज करें।",
        "step2": "अपनी मिट्टी का प्रकार चुनें।",
        "step3": "पानी की उपलब्धता का स्तर चुनें।",
        "step4": "अपनी वर्तमान फसल चुनें।",
        "step5": "यदि पता हो तो पिछली फसल चुनें।",
        "step6": "फसल चक्र योजना बनाएं बटन दबाएं।",
        "step7": "अनुशंसित फसल, फसल चक्र, खेती की जानकारी और रिपोर्ट देखें।",
        "not_provided": "प्रदान नहीं किया गया",
        "no_recommendation": "कोई उपयुक्त फसल सुझाव नहीं मिला। कृपया अलग कृषि परिस्थितियों का प्रयास करें।",
        "report_title": "स्मार्ट फसल चक्र रिपोर्ट",
        "report_soil_water": "मिट्टी और पानी",
        "report_crop_info": "फसल की जानकारी",
        "report_recommended": "अनुशंसित अगली फसल",
        "report_rotation": "सुझाया गया फसल चक्र",
        "report_general": "सामान्य सलाह",
        "report_advice": "फसल चक्र को निर्णय सहायता के रूप में उपयोग करें। वास्तविक फसल चयन में स्थानीय जलवायु, वर्षा, बाजार मूल्य, बीज की उपलब्धता, सिंचाई सुविधाओं और कृषि विशेषज्ञों की सलाह को ध्यान में रखें।",
        "footer": "🌱 स्मार्ट फसल चक्र | टिकाऊ खेती निर्णय सहायता प्रणाली"
    },

    "Telugu": {
        "title": "🌱 స్మార్ట్ పంట మార్పిడి",
        "subtitle": "ఆరోగ్యకరమైన నేల, మెరుగైన నీటి నిర్వహణ మరియు స్థిరమైన వ్యవసాయం కోసం AI ఆధారిత పంట మార్పిడి ప్రణాళిక.",
        "language": "🌐 భాషను ఎంచుకోండి",
        "farm_details": "🌾 వ్యవసాయ వివరాలు",
        "farmer_name": "రైతు పేరు",
        "farmer_placeholder": "మీ పేరు నమోదు చేయండి",
        "location": "ప్రాంతం",
        "location_placeholder": "గ్రామం / జిల్లా",
        "land_size": "భూమి పరిమాణం (ఎకరాలు)",
        "soil_type": "నేల రకం",
        "water": "నీటి లభ్యత",
        "current_crop": "ప్రస్తుత పంట",
        "previous_crop": "మునుపటి పంట",
        "none": "ఏదీ లేదు",
        "generate": "🌱 పంట మార్పిడి ప్రణాళిక రూపొందించండి",
        "soil_health": "నేల ఆరోగ్యం",
        "water_management": "నీటి నిర్వహణ",
        "crop_diversity": "పంట వైవిధ్యం",
        "smart_recommendation": "స్మార్ట్ సిఫార్సు",
        "crop_information": "🌾 ప్రస్తుత పంట సమాచారం",
        "water_requirement": "నీటి అవసరం",
        "nutrient_requirement": "పోషకాల అవసరం",
        "suitable_soil": "అనుకూలమైన నేల",
        "growing_season": "పంట కాలం",
        "recommended": "🌱 సిఫార్సు చేసిన తదుపరి పంట",
        "recommendation_score": "సిఫార్సు స్కోర్",
        "score_breakdown": "📊 సిఫార్సు స్కోర్ వివరాలు",
        "water_score": "💧 నీరు",
        "soil_score": "🪴 నేల",
        "soil_health_score": "🌱 నేల ఆరోగ్యం",
        "diversity_score": "🌾 వైవిధ్యం",
        "rotation": "🔄 సూచించిన పంట మార్పిడి",
        "current": "ప్రస్తుత పంట",
        "season": "కాలం",
        "all_seasons": "అన్ని కాలాలు",
        "alternatives": "📋 ప్రత్యామ్నాయ పంట సిఫార్సులు",
        "reason": "కారణం",
        "insights": "💡 వ్యవసాయ సమాచారం",
        "water_saving": "💧 నీటి పొదుపు సూచన",
        "low_water_message": "మీ పొలంలో నీటి లభ్యత తక్కువగా ఉంది. శనగ, పెసలు మరియు జొన్న వంటి తక్కువ నీటి అవసరమున్న పంటలకు ప్రాధాన్యత ఇవ్వండి.",
        "water_management_title": "💧 నీటి నిర్వహణ",
        "medium_water_message": "మధ్యస్థ నీటి లభ్యత ధాన్యాలు, పప్పుధాన్యాలు మరియు నూనెగింజల సమతుల్య కలయికకు అనుకూలంగా ఉంటుంది.",
        "water_availability_title": "💧 నీటి లభ్యత",
        "high_water_message": "అధిక నీటి లభ్యత ఎక్కువ పంట ఎంపికలను అందిస్తుంది. అయితే నీటిని సమర్థవంతంగా ఉపయోగించడం అవసరం.",
        "soil_health_benefit": "🌱 నేల ఆరోగ్య ప్రయోజనం",
        "legume_message": "సిఫార్సు చేసిన పంట పప్పుధాన్యం. పప్పుధాన్యాలు నత్రజని స్థిరీకరణకు సహాయపడుతూ నేల సారాన్ని మెరుగుపరచగలవు.",
        "rotation_benefit": "🌍 పంట మార్పిడి ప్రయోజనం",
        "rotation_message": "పంట వైవిధ్యం ఒకే పంటపై ఆధారపడటాన్ని తగ్గించి కొన్ని కీటకాలు మరియు వ్యాధుల చక్రాలను తగ్గించడంలో సహాయపడుతుంది.",
        "farm_summary": "📋 వ్యవసాయ సారాంశం",
        "farmer_details": "👨‍🌾 రైతు వివరాలు",
        "crop_details": "🌾 పంట వివరాలు",
        "farmer": "రైతు",
        "land": "భూమి పరిమాణం",
        "recommended_crop": "సిఫార్సు చేసిన పంట",
        "farm_report": "📥 వ్యవసాయ నివేదిక",
        "download_report": "📥 వ్యవసాయ నివేదికను డౌన్‌లోడ్ చేయండి",
        "how_to_use": "👨‍🌾 యాప్‌ను ఎలా ఉపయోగించాలి",
        "step1": "సైడ్‌బార్‌లో రైతు వివరాలను నమోదు చేయండి.",
        "step2": "మీ నేల రకాన్ని ఎంచుకోండి.",
        "step3": "నీటి లభ్యత స్థాయిని ఎంచుకోండి.",
        "step4": "మీ ప్రస్తుత పంటను ఎంచుకోండి.",
        "step5": "తెలిస్తే మునుపటి పంటను ఎంచుకోండి.",
        "step6": "పంట మార్పిడి ప్రణాళిక రూపొందించండి బటన్‌ను క్లిక్ చేయండి.",
        "step7": "సిఫార్సు చేసిన పంట, పంట మార్పిడి, వ్యవసాయ సమాచారం మరియు నివేదికను చూడండి.",
        "not_provided": "అందించలేదు",
        "no_recommendation": "తగిన పంట సిఫార్సు కనుగొనబడలేదు. దయచేసి వేరే వ్యవసాయ పరిస్థితులను ప్రయత్నించండి.",
        "report_title": "స్మార్ట్ పంట మార్పిడి నివేదిక",
        "report_soil_water": "నేల మరియు నీరు",
        "report_crop_info": "పంట సమాచారం",
        "report_recommended": "సిఫార్సు చేసిన తదుపరి పంట",
        "report_rotation": "సూచించిన పంట మార్పిడి",
        "report_general": "సాధారణ సలహా",
        "report_advice": "పంట మార్పిడిని నిర్ణయ సహాయక మార్గదర్శిగా ఉపయోగించండి. నిజమైన పంట ఎంపికలో స్థానిక వాతావరణం, వర్షపాతం, మార్కెట్ ధరలు, విత్తనాల లభ్యత, నీటిపారుదల సౌకర్యాలు మరియు వ్యవసాయ నిపుణుల సలహాలను పరిగణించండి.",
        "footer": "🌱 స్మార్ట్ పంట మార్పిడి | స్థిరమైన వ్యవసాయ నిర్ణయ సహాయక వ్యవస్థ"
    },

    "Tamil": {
        "title": "🌱 ஸ்மார்ட் பயிர் சுழற்சி",
        "subtitle": "ஆரோக்கியமான மண், சிறந்த நீர் மேலாண்மை மற்றும் நிலையான விவசாயத்திற்கான AI அடிப்படையிலான பயிர் சுழற்சி திட்டம்.",
        "language": "🌐 மொழியைத் தேர்ந்தெடுக்கவும்",
        "farm_details": "🌾 பண்ணை விவரங்கள்",
        "farmer_name": "விவசாயி பெயர்",
        "farmer_placeholder": "உங்கள் பெயரை உள்ளிடவும்",
        "location": "இடம்",
        "location_placeholder": "கிராமம் / மாவட்டம்",
        "land_size": "நில அளவு (ஏக்கர்)",
        "soil_type": "மண் வகை",
        "water": "நீர் கிடைக்கும் அளவு",
        "current_crop": "தற்போதைய பயிர்",
        "previous_crop": "முந்தைய பயிர்",
        "none": "எதுவும் இல்லை",
        "generate": "🌱 பயிர் சுழற்சி திட்டத்தை உருவாக்கவும்",
        "soil_health": "மண் ஆரோக்கியம்",
        "water_management": "நீர் மேலாண்மை",
        "crop_diversity": "பயிர் பல்வகைமை",
        "smart_recommendation": "ஸ்மார்ட் பரிந்துரை",
        "crop_information": "🌾 தற்போதைய பயிர் தகவல்",
        "water_requirement": "நீர் தேவை",
        "nutrient_requirement": "ஊட்டச்சத்து தேவை",
        "suitable_soil": "பொருத்தமான மண்",
        "growing_season": "வளரும் பருவம்",
        "recommended": "🌱 பரிந்துரைக்கப்பட்ட அடுத்த பயிர்",
        "recommendation_score": "பரிந்துரை மதிப்பெண்",
        "score_breakdown": "📊 பரிந்துரை மதிப்பெண் விவரம்",
        "water_score": "💧 நீர்",
        "soil_score": "🪴 மண்",
        "soil_health_score": "🌱 மண் ஆரோக்கியம்",
        "diversity_score": "🌾 பல்வகைமை",
        "rotation": "🔄 பரிந்துரைக்கப்பட்ட பயிர் சுழற்சி",
        "current": "தற்போதைய பயிர்",
        "season": "பருவம்",
        "all_seasons": "அனைத்து பருவங்களும்",
        "alternatives": "📋 மாற்று பயிர் பரிந்துரைகள்",
        "reason": "காரணம்",
        "insights": "💡 விவசாய தகவல்கள்",
        "water_saving": "💧 நீர் சேமிப்பு குறிப்பு",
        "low_water_message": "உங்கள் பண்ணையில் நீர் கிடைக்கும் அளவு குறைவாக உள்ளது. கொண்டைக்கடலை, பச்சைப்பயறு மற்றும் சோளம் போன்ற குறைந்த நீர் தேவைப்படும் பயிர்களை தேர்வு செய்யவும்.",
        "water_management_title": "💧 நீர் மேலாண்மை",
        "medium_water_message": "மிதமான நீர் கிடைக்கும் நிலையில் தானியங்கள், பருப்பு வகைகள் மற்றும் எண்ணெய் வித்துக்களின் சமநிலையான கலவையை வளர்க்கலாம்.",
        "water_availability_title": "💧 நீர் கிடைக்கும் அளவு",
        "high_water_message": "அதிக நீர் கிடைக்கும் நிலையில் அதிக பயிர்களை தேர்வு செய்யலாம். ஆனால் நீரை திறமையாக பயன்படுத்துவது அவசியம்.",
        "soil_health_benefit": "🌱 மண் ஆரோக்கிய நன்மை",
        "legume_message": "பரிந்துரைக்கப்பட்ட பயிர் ஒரு பருப்பு வகையாகும். பருப்பு வகைகள் நைட்ரஜன் நிலைப்படுத்தலுக்கு உதவி செய்து மண்ணின் வளத்தை மேம்படுத்தலாம்.",
        "rotation_benefit": "🌍 பயிர் சுழற்சியின் நன்மை",
        "rotation_message": "பயிர் பல்வகைமை ஒரே பயிரை சார்ந்திருப்பதை குறைத்து சில பூச்சி மற்றும் நோய் சுழற்சிகளை கட்டுப்படுத்த உதவும்.",
        "farm_summary": "📋 பண்ணை சுருக்கம்",
        "farmer_details": "👨‍🌾 விவசாயி விவரங்கள்",
        "crop_details": "🌾 பயிர் விவரங்கள்",
        "farmer": "விவசாயி",
        "land": "நில அளவு",
        "recommended_crop": "பரிந்துரைக்கப்பட்ட பயிர்",
        "farm_report": "📥 பண்ணை அறிக்கை",
        "download_report": "📥 பண்ணை அறிக்கையை பதிவிறக்கவும்",
        "how_to_use": "👨‍🌾 பயன்பாட்டை எப்படி பயன்படுத்துவது",
        "step1": "பக்கப்பட்டியில் விவசாயி விவரங்களை உள்ளிடவும்.",
        "step2": "உங்கள் மண் வகையைத் தேர்ந்தெடுக்கவும்.",
        "step3": "நீர் கிடைக்கும் அளவைத் தேர்ந்தெடுக்கவும்.",
        "step4": "உங்கள் தற்போதைய பயிரைத் தேர்ந்தெடுக்கவும்.",
        "step5": "தெரிந்திருந்தால் முந்தைய பயிரைத் தேர்ந்தெடுக்கவும்.",
        "step6": "பயிர் சுழற்சி திட்டத்தை உருவாக்கவும் என்பதை கிளிக் செய்யவும்.",
        "step7": "பரிந்துரைக்கப்பட்ட பயிர், பயிர் சுழற்சி, விவசாய தகவல்கள் மற்றும் அறிக்கையைப் பார்க்கவும்.",
        "not_provided": "வழங்கப்படவில்லை",
        "no_recommendation": "பொருத்தமான பயிர் பரிந்துரை கிடைக்கவில்லை. வேறு விவசாய நிலைமைகளை முயற்சிக்கவும்.",
        "report_title": "ஸ்மார்ட் பயிர் சுழற்சி அறிக்கை",
        "report_soil_water": "மண் மற்றும் நீர்",
        "report_crop_info": "பயிர் தகவல்",
        "report_recommended": "பரிந்துரைக்கப்பட்ட அடுத்த பயிர்",
        "report_rotation": "பரிந்துரைக்கப்பட்ட பயிர் சுழற்சி",
        "report_general": "பொதுவான ஆலோசனை",
        "report_advice": "பயிர் சுழற்சியை முடிவு எடுப்பதற்கான வழிகாட்டியாக பயன்படுத்தவும். உண்மையான பயிர் தேர்வில் உள்ளூர் காலநிலை, மழைப்பொழிவு, சந்தை விலைகள், விதை கிடைக்கும் தன்மை, நீர்ப்பாசன வசதிகள் மற்றும் வேளாண் நிபுணர்களின் ஆலோசனைகளை கருத்தில் கொள்ளவும்.",
        "footer": "🌱 ஸ்மார்ட் பயிர் சுழற்சி | நிலையான விவசாய முடிவு ஆதரவு அமைப்பு"
    }
}

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def translated_crop(crop, language):
    return crop_names.get(language, {}).get(crop, crop)


def translated_soil(soil, language):
    return soil_names.get(language, {}).get(soil, soil)


def translated_value(value, language):
    return value_names.get(language, {}).get(value, value)


def translated_soil_list(soils, language):
    return ", ".join(
        translated_soil(soil, language)
        for soil in soils
    )


def translated_season_list(seasons, language):
    return ", ".join(
        translated_value(season, language)
        for season in seasons
    )


def translated_benefit(crop, language):
    return crop_benefit_translations.get(language, {}).get(
        crop, crop_data.get(crop, {}).get("benefit", "")
    )


# =========================================================
# SCORING FUNCTIONS
# =========================================================

def water_score(available_water, crop_water):
    scores = {
        "Low": {
            "Low": 5,
            "Medium": 2,
            "High": 0
        },
        "Medium": {
            "Low": 4,
            "Medium": 5,
            "High": 3
        },
        "High": {
            "Low": 3,
            "Medium": 5,
            "High": 5
        }
    }

    return scores.get(
        available_water,
        {}
    ).get(
        crop_water,
        0
    )


def rainfall_score(rainfall_level, crop_water):
    """
    Extra (0-3) contribution based on expected rainfall vs a crop's
    water need. This is a simple heuristic, not a weather model —
    it works alongside water_score() so 'climate conditions' covers
    more than just the live temperature reading.
    """
    scores = {
        "Low": {"Low": 3, "Medium": 1, "High": 0},
        "Medium": {"Low": 2, "Medium": 3, "High": 2},
        "High": {"Low": 2, "Medium": 3, "High": 3},
    }

    return scores.get(
        rainfall_level,
        {}
    ).get(
        crop_water,
        0
    )


def soil_score(selected_soil, suitable_soils):

    if selected_soil in suitable_soils:
        return 5

    if selected_soil == "Clay" and "Loamy" in suitable_soils:
        return 2

    if selected_soil == "Sandy" and "Loamy" in suitable_soils:
        return 2

    if selected_soil == "Red Soil" and "Loamy" in suitable_soils:
        return 3

    if selected_soil == "Black Soil" and "Loamy" in suitable_soils:
        return 3

    return 0


def calculate_recommendations(
    current_crop,
    previous_crop,
    soil_type,
    water_availability,
    preferred_season=None,
    rainfall_availability="Medium"
):

    current_info = crop_data[current_crop]

    recommendations = []

    for crop in current_info["next"]:

        info = crop_data[crop]

        # -------------------------
        # WATER SCORE
        # -------------------------

        w_score = water_score(
            water_availability,
            info["water"]
        )

        # -------------------------
        # RAINFALL SCORE
        # -------------------------

        r_score = rainfall_score(
            rainfall_availability,
            info["water"]
        )

        # -------------------------
        # SOIL SCORE
        # -------------------------

        s_score = soil_score(
            soil_type,
            info["soil"]
        )

        # -------------------------
        # LEGUME BONUS
        # -------------------------

        legume_score = 3 if info["legume"] else 0

        # -------------------------
        # SEASON MATCH BONUS
        # -------------------------

        season_score = (
            3 if preferred_season and preferred_season in info["season"] else 0
        )

        # -------------------------
        # PREVIOUS CROP PENALTY
        # -------------------------

        previous_penalty = 4 if crop == previous_crop else 0

        # -------------------------
        # SAME CROP PENALTY
        # -------------------------

        same_crop_penalty = 6 if crop == current_crop else 0

        # -------------------------
        # DIVERSIFICATION
        # -------------------------

        diversification_score = 2

        # -------------------------
        # TOTAL SCORE
        # -------------------------

        score = (
            w_score
            + r_score
            + s_score
            + legume_score
            + season_score
            + diversification_score
            - previous_penalty
            - same_crop_penalty
        )

        recommendations.append({
            "Crop": crop,
            "Score": score,
            "Water Score": w_score,
            "Rainfall Score": r_score,
            "Soil Score": s_score,
            "Soil Health": legume_score,
            "Season Score": season_score,
            "Diversification": diversification_score,
            "Water Requirement": info["water"],
            "Suitable Soil": info["soil"],
            "Season": info["season"],
            "Reason": info["benefit"]
        })

    recommendations.sort(
        key=lambda x: x["Score"],
        reverse=True
    )

    return recommendations


def calculate_repeat_score(
    current_crop,
    soil_type,
    water_availability,
    preferred_season=None,
    rainfall_availability="Medium"
):
    """
    Scores what happens if the farmer plants the SAME crop again
    instead of rotating — the 'habit' baseline. Uses the same
    scoring components as calculate_recommendations() but with no
    diversification credit and the full same-crop penalty, so it can
    be compared directly against the top rotation recommendation.
    """

    info = crop_data[current_crop]

    w_score = water_score(water_availability, info["water"])
    r_score = rainfall_score(rainfall_availability, info["water"])
    s_score = soil_score(soil_type, info["soil"])
    legume_score = 3 if info["legume"] else 0
    season_score = (
        3 if preferred_season and preferred_season in info["season"] else 0
    )
    diversification_score = 0
    same_crop_penalty = 6

    score = (
        w_score
        + r_score
        + s_score
        + legume_score
        + season_score
        + diversification_score
        - same_crop_penalty
    )

    return {
        "Crop": current_crop,
        "Score": score,
        "Water Score": w_score,
        "Rainfall Score": r_score,
        "Soil Score": s_score,
        "Soil Health": legume_score,
        "Season Score": season_score,
        "Diversification": diversification_score,
    }


def yield_risk_label(suitability_pct):
    """
    Simple heuristic label ('Low' / 'Medium' / 'High' risk) that
    stands in for a real yield/soil-depletion estimate. This is NOT
    measured yield data — it's a labeled interpretation of the
    suitability score, and should be presented to judges as a
    heuristic, not a validated forecast.
    """
    if suitability_pct >= 70:
        return "Low"
    elif suitability_pct >= 40:
        return "Medium"
    else:
        return "High"


# =========================================================
# SIDEBAR + LANGUAGE + ASSETS
# =========================================================

from pathlib import Path
import base64

ASSET_DIR = Path(__file__).parent / "smart_crop_rotation_assets"

def asset_data_uri(filename):
    path = ASSET_DIR / filename
    if not path.exists():
        return ""
    suffix = path.suffix.lower()
    mime = "image/png" if suffix == ".png" else "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"

# Real crop photographs from Wikimedia Commons.
# These are used first so the dashboard never shows the generic seedling
# placeholder for a known crop. The URLs point to the corresponding
# Commons files; if the internet is unavailable, the local asset is used.
CROP_PHOTO_URLS = {
    "Rice": "https://commons.wikimedia.org/wiki/Special:FilePath/Rice%20plant%20%28Oryza%20sativa%29.jpg",
    "Green Gram": "https://commons.wikimedia.org/wiki/Special:FilePath/Mung%20Bean%20plant.jpg",
    "Black Gram": "https://commons.wikimedia.org/wiki/Special:FilePath/Black%20gram%20plant.jpg",
    "Groundnut": "https://commons.wikimedia.org/wiki/Special:FilePath/Groundnut%20plants.jpg",
    "Wheat": "https://commons.wikimedia.org/wiki/Special:FilePath/Wheat%20plant.jpg",
    "Maize": "https://commons.wikimedia.org/wiki/Special:FilePath/Plant%20Maize.jpg",
    "Chickpea": "https://commons.wikimedia.org/wiki/Special:FilePath/Chickpeas%20Plant.jpg",
    "Soybean": "https://commons.wikimedia.org/wiki/Special:FilePath/Soybean.jpg",
    "Mustard": "https://commons.wikimedia.org/wiki/Special:FilePath/Mustard%20plant.jpg",
    "Cotton": "https://commons.wikimedia.org/wiki/Special:FilePath/Cotton%20plant.jpg",
    "Sorghum": "https://commons.wikimedia.org/wiki/Special:FilePath/Sorghum%20plant.jpg",
}

LOCAL_CROP_FILES = {
    "Rice": "rice.png",
    "Wheat": "wheat.png",
    "Maize": "maize.png",
    "Cotton": "cotton.png",
    "Groundnut": "groundnut.png",
    "Soybean": "soybean.png",
    "Chickpea": "chickpea.png",
    "Green Gram": "green_gram.png",
    "Black Gram": "black_gram.png",
    "Mustard": "mustard.png",
    "Sorghum": "sorghum.png",
}

def crop_asset(crop):
    """Return a crop-specific photo URL, with a local-file fallback."""
    crop = str(crop).strip()

    # Exact crop name
    if crop in CROP_PHOTO_URLS:
        return CROP_PHOTO_URLS[crop]

    # Common name variations
    aliases = {
        "paddy": "Rice",
        "rice": "Rice",
        "mung bean": "Green Gram",
        "moong": "Green Gram",
        "green gram": "Green Gram",
        "urad": "Black Gram",
        "urad dal": "Black Gram",
        "black gram": "Black Gram",
        "peanut": "Groundnut",
        "ground nut": "Groundnut",
        "groundnut": "Groundnut",
        "corn": "Maize",
        "maize": "Maize",
        "bengal gram": "Chickpea",
        "gram": "Chickpea",
        "chickpea": "Chickpea",
        "soy bean": "Soybean",
        "soybean": "Soybean",
        "mustard": "Mustard",
        "cotton": "Cotton",
        "sorghum": "Sorghum",
        "wheat": "Wheat",
    }

    matched = aliases.get(crop.lower())
    if matched in CROP_PHOTO_URLS:
        return CROP_PHOTO_URLS[matched]

    # Local fallback only when no web photo is mapped.
    filename = LOCAL_CROP_FILES.get(matched or crop)
    if filename:
        path = ASSET_DIR / filename
        if path.exists():
            return str(path)

    return None


# =========================================================
# DASHBOARD OVERRIDE CSS
# =========================================================
st.markdown("""
<style>
.main-title,.subtitle{display:none!important}
section[data-testid="stSidebar"]{background:linear-gradient(180deg,#064d2b,#063c24)!important}
section[data-testid="stSidebar"] label,section[data-testid="stSidebar"] .stMarkdown,section[data-testid="stSidebar"] h1,section[data-testid="stSidebar"] h2,section[data-testid="stSidebar"] h3,section[data-testid="stSidebar"] p{color:#fff!important}
section[data-testid="stSidebar"] input{background:#fff!important;color:#173622!important;-webkit-text-fill-color:#173622!important}
section[data-testid="stSidebar"] input::placeholder{color:#7b8790!important;-webkit-text-fill-color:#7b8790!important}
section[data-testid="stSidebar"] [data-baseweb="select"]>div{background:#fff!important;border:1px solid #d7ded9!important}
section[data-testid="stSidebar"] [data-baseweb="select"] *{color:#173622!important;-webkit-text-fill-color:#173622!important}
[data-baseweb="popover"],[data-baseweb="menu"],[role="listbox"]{background:#fff!important}
[role="option"],[role="option"] *{color:#173622!important;-webkit-text-fill-color:#173622!important}
.brand-wrap{padding:5px 4px 18px}.brand-row{display:flex;align-items:center;gap:12px}.brand-leaf{font-size:42px}.brand-title{font-size:24px;font-weight:800;line-height:1.08;color:#fff!important}.brand-sub{margin:10px 0 0 45px;color:#d9efc9!important;font-size:13px;line-height:1.45}
.hero-exact{min-height:245px;border-radius:0 0 18px 18px;overflow:hidden;position:relative;display:flex;align-items:center;margin:-1rem -.5rem 18px -.5rem;background-position:center;background-size:cover;box-shadow:0 8px 24px rgba(31,68,35,.12)}
.crop-rotation-image img{width:100%;height:150px;object-fit:cover;border-radius:14px;display:block}
.rotation-img{width:100%;height:110px;object-fit:cover;border-radius:12px;display:block;margin:0 auto}
.rotation-fallback{width:100%;height:110px;border-radius:12px;background:#edf4e5;display:flex;align-items:center;justify-content:center;font-size:42px}
.featured-img{width:100%;height:300px;object-fit:cover;border-radius:15px;display:block}
.featured-crop-name{text-align:center;color:#10251a;font-size:24px;font-weight:850;margin:10px 0 2px}
.rotation-year{min-height:22px;text-align:center;color:#617067;font-size:12px;font-weight:700;margin-top:8px}
.rotation-title{text-align:center;color:#10251a;font-weight:800;margin-top:6px;min-height:42px;display:flex;align-items:flex-start;justify-content:center}
.rotation-reason{text-align:center;color:#5b6b60;font-size:11px;line-height:1.35;margin-top:4px;padding:0 4px;min-height:30px}
.rot-arrow{display:flex;align-items:center;justify-content:center;height:150px;font-size:32px;color:#1c6739}
.hero-exact:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(245,249,237,.94),rgba(245,249,237,.78) 38%,rgba(245,249,237,.25) 70%,rgba(245,249,237,.03))}.hero-exact-content{position:relative;z-index:2;width:100%;text-align:center;padding:28px}.hero-exact h1{margin:0;color:#063d24;font-size:48px;font-weight:850}.hero-exact p{margin:8px 0 0;color:#173b27;font-size:18px}
.top-card{background:#fff;border:1px solid #e5e9e1;border-radius:16px;padding:14px 14px 12px;min-height:118px;box-shadow:0 5px 18px rgba(35,67,38,.08);display:flex;flex-direction:column}.top-icon{font-size:26px;line-height:1;margin-bottom:8px}.top-label{color:#466052;font-size:12px;line-height:1.35;min-height:32px}.top-value{color:#10251a;font-size:15px;font-weight:800;margin-top:6px;white-space:normal;overflow:visible;word-break:break-word;line-height:1.25}
.dash-panel{background:#fff;border:1px solid #e5e9e1;border-radius:18px;padding:18px;box-shadow:0 6px 20px rgba(35,67,38,.07);height:100%}.rec-panel{background:linear-gradient(135deg,#f8fbf1,#eef7df)}.rec-badge{display:inline-block;padding:6px 10px;border-radius:999px;background:#e4f1d1;color:#285e38;font-size:12px;font-weight:800}.rec-title{color:#10251a;font-size:24px;font-weight:800;margin-top:16px}.rec-crop{color:#16723b;font-size:34px;font-weight:850;line-height:1.05;margin:3px 0 12px}.rec-line{color:#334b3c;font-size:14px;margin:10px 0}.crop-photo{width:100%;height:300px;object-fit:cover;border-radius:15px}.rotation-year{text-align:center;color:#617067;font-size:12px;font-weight:700;margin-top:8px}.rotation-title{text-align:center;color:#10251a;font-weight:800;margin-top:6px;word-break:normal}.rot-arrow{display:flex;align-items:center;justify-content:center;height:165px;font-size:32px;color:#1c6739}
.kpi-card{background:#fff;border:1px solid #e5e9e1;border-radius:17px;padding:18px;min-height:165px;box-shadow:0 6px 18px rgba(35,67,38,.06)}.kpi-label{color:#526158;font-size:13px;font-weight:700}.kpi-value{color:#17683a;font-size:28px;font-weight:850;margin-top:8px}.kpi-sub{color:#68756c;font-size:12px;margin-top:4px}.kpi-bar{height:7px;background:#e9eee7;border-radius:10px;margin-top:14px;overflow:hidden}.kpi-fill{height:100%;background:linear-gradient(90deg,#277346,#79a950);border-radius:10px}.insight-card{background:#f8fbf3;border:1px solid #e0e9d4;border-radius:16px;padding:17px;min-height:150px}.insight-card h4{color:#174b2d;margin:0 0 8px;font-size:16px}.insight-card p{color:#526057;font-size:14px;line-height:1.55;margin:0}.report-card{background:#fff;border:1px solid #e5e9e1;border-radius:18px;padding:20px;min-height:175px;box-shadow:0 6px 18px rgba(35,67,38,.06)}.report-card h3{color:#174b2d;margin:0 0 8px}.report-card p{color:#59675e;line-height:1.55}.quote-farmer{background:#eef4dc;border-radius:18px;overflow:hidden;min-height:175px}.quote-farmer img{width:48%;height:175px;object-fit:cover;float:left}.quote-text{padding:24px;color:#31513b;font-size:17px;line-height:1.55}.section-head{color:#10281a;font-size:23px;font-weight:850;margin:20px 0 12px}
</style>""",unsafe_allow_html=True)


# =========================================================
# LOCATION-BASED LIVE TEMPERATURE
# =========================================================
# Uses Open-Meteo's free geocoding + weather APIs.
# No API key is required.
#
# The user enters a village / district / city in the sidebar.
# We first convert that place name to latitude/longitude and
# then request the current temperature for those coordinates.

@st.cache_data(ttl=600, show_spinner=False)
def get_location_temperature(location_text):
    """
    Return (temperature_celsius, resolved_location).

    Examples:
        Bengaluru, Karnataka -> (current temperature, Bengaluru)
        Mysuru -> (current temperature, Mysuru)
        Hyderabad -> (current temperature, Hyderabad)

    If the location cannot be found or the weather service is
    temporarily unavailable, return (None, None).
    """
    query = (location_text or "").strip()

    # Keep the screenshot/demo behaviour when no location is entered.
    if not query:
        query = "Bengaluru, Karnataka"

    try:
        # -----------------------------------------------------
        # STEP 1: Convert place name -> latitude/longitude
        # -----------------------------------------------------
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"
        geo_params = {
            "name": query,
            "count": 1,
            "language": "en",
            "format": "json",
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=8,
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        results = geo_data.get("results", [])

        # If "Bengaluru, KA" or another combined query is not
        # understood, try the text after the last comma.
        if not results and "," in query:
            fallback_query = query.split(",")[-1].strip()
            if fallback_query:
                geo_params["name"] = fallback_query
                geo_response = requests.get(
                    geo_url,
                    params=geo_params,
                    timeout=8,
                )
                geo_response.raise_for_status()
                geo_data = geo_response.json()
                results = geo_data.get("results", [])

        if not results:
            return None, None

        place = results[0]
        latitude = place["latitude"]
        longitude = place["longitude"]

        resolved_name = place.get("name", query)
        admin1 = place.get("admin1", "")
        country = place.get("country", "")

        location_parts = [
            str(x).strip()
            for x in [resolved_name, admin1, country]
            if x
        ]
        resolved_location = ", ".join(location_parts)

        # -----------------------------------------------------
        # STEP 2: Get current weather at those coordinates
        # -----------------------------------------------------
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m",
            "timezone": "auto",
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=8,
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data.get("current", {})
        temperature = current.get("temperature_2m")

        if temperature is None:
            return None, resolved_location

        return float(temperature), resolved_location

    except (requests.RequestException, ValueError, KeyError, TypeError):
        return None, None


def temperature_display(location_text):
    """
    Create the temperature shown in the top dashboard card.
    """
    temperature, resolved_location = get_location_temperature(location_text)

    if temperature is None:
        return "—", None

    return f"{temperature:.1f}°C", resolved_location


# =========================================================
# SIDEBAR — ONE AND ONLY ONE SET OF WIDGETS
# =========================================================
# =========================================================
# =========================================================

st.sidebar.markdown("""
<div class="brand-wrap">
  <div class="brand-row">
    <div class="brand-leaf">🌱</div>
    <div class="brand-title">Smart Crop<br>Rotation</div>
  </div>
  <div class="brand-sub">Sustainable Farming<br>Better Tomorrow</div>
</div>
""", unsafe_allow_html=True)

language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "Kannada", "Hindi", "Telugu", "Tamil"],
    key="language_select_final"
)
t = translations[language]

# Extra dashboard translations used by the visual dashboard.
# These are kept separate so the existing recommendation logic remains unchanged.
DASHBOARD_TRANSLATIONS = {
    "English": {
        "rotation_plan": "Crop Rotation Plan (4 Years)",
        "year": "Year",
        "rotation_message": "🌱 This rotation supports soil health, crop diversity and better resource management.",
        "temperature": "Temperature",
        "ai_recommendation": "✨ AI RECOMMENDATION",
        "recommended_crop_label": "Recommended Crop",
        "suitability_score": "Suitability Score",
        "farm_performance": "📊 Farm Performance",
        "water_usage": "Water Usage",
        "current_rotation": "Current Rotation",
        "soil_health_label": "Soil Health",
        "current_status": "Current Status",
        "expected_yield": "Expected Yield",
        "estimated_per_acre": "Estimated per acre",
        "sustainability_score": "Sustainability Score",
        "overall": "Overall",
        "smart_insights": "💡 Smart Insights",
        "recommendation": "Recommendation",
        "highest_ranked": "is the highest-ranked next crop under the selected farm conditions.",
        "generate_download": "📄 Generate & Download Report",
        "report_description": "Get a detailed report containing your farm conditions, recommendation, score and crop rotation plan.",
        "download_report_button": "⬇️ Download Report",
        "quote": "Smart Farming<br>for a Better<br>Tomorrow",
        "alternative": "📋 View Alternative Crop Recommendations",
    },
    "Kannada": {
        "rotation_plan": "ಬೆಳೆ ಪರ್ಯಾಯ ಯೋಜನೆ (4 ವರ್ಷಗಳು)", "year": "ವರ್ಷ",
        "rotation_message": "🌱 ಈ ಬೆಳೆ ಪರ್ಯಾಯವು ಮಣ್ಣಿನ ಆರೋಗ್ಯ, ಬೆಳೆ ವೈವಿಧ್ಯತೆ ಮತ್ತು ಉತ್ತಮ ಸಂಪನ್ಮೂಲ ನಿರ್ವಹಣೆಗೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
        "temperature": "ತಾಪಮಾನ", "ai_recommendation": "✨ AI ಶಿಫಾರಸು", "recommended_crop_label": "ಶಿಫಾರಸು ಮಾಡಿದ ಬೆಳೆ",
        "suitability_score": "ಸೂಕ್ತತಾ ಅಂಕ", "farm_performance": "📊 ಕೃಷಿ ಕಾರ್ಯಕ್ಷಮತೆ", "water_usage": "ನೀರಿನ ಬಳಕೆ",
        "current_rotation": "ಪ್ರಸ್ತುತ ಪರ್ಯಾಯ", "soil_health_label": "ಮಣ್ಣಿನ ಆರೋಗ್ಯ", "current_status": "ಪ್ರಸ್ತುತ ಸ್ಥಿತಿ",
        "expected_yield": "ನಿರೀಕ್ಷಿತ ಇಳುವರಿ", "estimated_per_acre": "ಪ್ರತಿ ಎಕರೆಗೆ ಅಂದಾಜು", "sustainability_score": "ಸುಸ್ಥಿರತೆ ಅಂಕ", "overall": "ಒಟ್ಟು",
        "smart_insights": "💡 ಸ್ಮಾರ್ಟ್ ಕೃಷಿ ಮಾಹಿತಿ", "recommendation": "ಶಿಫಾರಸು", "highest_ranked": "ಆಯ್ಕೆ ಮಾಡಿದ ಕೃಷಿ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಅತ್ಯುತ್ತಮ ಸ್ಥಾನ ಪಡೆದ ಮುಂದಿನ ಬೆಳೆ.",
        "generate_download": "📄 ವರದಿ ರಚಿಸಿ ಮತ್ತು ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ", "report_description": "ನಿಮ್ಮ ಕೃಷಿ ಪರಿಸ್ಥಿತಿಗಳು, ಶಿಫಾರಸು, ಅಂಕ ಮತ್ತು ಬೆಳೆ ಪರ್ಯಾಯ ಯೋಜನೆಯನ್ನು ಒಳಗೊಂಡ ವಿವರವಾದ ವರದಿಯನ್ನು ಪಡೆಯಿರಿ.",
        "download_report_button": "⬇️ ವರದಿ ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ", "quote": "ಸ್ಮಾರ್ಟ್ ಕೃಷಿ<br>ಉತ್ತಮ<br>ನಾಳೆಗಾಗಿ", "alternative": "📋 ಪರ್ಯಾಯ ಬೆಳೆ ಶಿಫಾರಸುಗಳನ್ನು ವೀಕ್ಷಿಸಿ",
    },
    "Hindi": {
        "rotation_plan": "फसल चक्र योजना (4 वर्ष)", "year": "वर्ष",
        "rotation_message": "🌱 यह फसल चक्र मिट्टी के स्वास्थ्य, फसल विविधता और बेहतर संसाधन प्रबंधन में सहायता करता है।",
        "temperature": "तापमान", "ai_recommendation": "✨ AI सुझाव", "recommended_crop_label": "अनुशंसित फसल",
        "suitability_score": "उपयुक्तता स्कोर", "farm_performance": "📊 खेत का प्रदर्शन", "water_usage": "पानी का उपयोग",
        "current_rotation": "वर्तमान चक्र", "soil_health_label": "मिट्टी का स्वास्थ्य", "current_status": "वर्तमान स्थिति",
        "expected_yield": "अनुमानित उपज", "estimated_per_acre": "प्रति एकड़ अनुमानित", "sustainability_score": "स्थिरता स्कोर", "overall": "कुल",
        "smart_insights": "💡 स्मार्ट जानकारी", "recommendation": "सुझाव", "highest_ranked": "चयनित खेत की परिस्थितियों में सबसे उच्च रैंक वाली अगली फसल है।",
        "generate_download": "📄 रिपोर्ट बनाएं और डाउनलोड करें", "report_description": "अपने खेत की परिस्थितियों, सुझाव, स्कोर और फसल चक्र योजना की विस्तृत रिपोर्ट प्राप्त करें।",
        "download_report_button": "⬇️ रिपोर्ट डाउनलोड करें", "quote": "स्मार्ट खेती<br>बेहतर<br>कल के लिए", "alternative": "📋 वैकल्पिक फसल सुझाव देखें",
    },
    "Telugu": {
        "rotation_plan": "పంట మార్పిడి ప్రణాళిక (4 సంవత్సరాలు)", "year": "సంవత్సరం",
        "rotation_message": "🌱 ఈ పంట మార్పిడి నేల ఆరోగ్యం, పంట వైవిధ్యం మరియు మెరుగైన వనరుల నిర్వహణకు సహాయపడుతుంది.",
        "temperature": "ఉష్ణోగ్రత", "ai_recommendation": "✨ AI సిఫార్సు", "recommended_crop_label": "సిఫార్సు చేసిన పంట",
        "suitability_score": "అనుకూలత స్కోర్", "farm_performance": "📊 వ్యవసాయ పనితీరు", "water_usage": "నీటి వినియోగం",
        "current_rotation": "ప్రస్తుత మార్పిడి", "soil_health_label": "నేల ఆరోగ్యం", "current_status": "ప్రస్తుత స్థితి",
        "expected_yield": "అంచనా దిగుబడి", "estimated_per_acre": "ఎకరాకు అంచనా", "sustainability_score": "స్థిరత్వ స్కోర్", "overall": "మొత్తం",
        "smart_insights": "💡 స్మార్ట్ సమాచారం", "recommendation": "సిఫార్సు", "highest_ranked": "ఎంచుకున్న వ్యవసాయ పరిస్థితుల్లో అత్యధిక ర్యాంక్ పొందిన తదుపరి పంట.",
        "generate_download": "📄 నివేదికను రూపొందించి డౌన్‌లోడ్ చేయండి", "report_description": "మీ వ్యవసాయ పరిస్థితులు, సిఫార్సు, స్కోర్ మరియు పంట మార్పిడి ప్రణాళికతో కూడిన నివేదికను పొందండి.",
        "download_report_button": "⬇️ నివేదికను డౌన్‌లోడ్ చేయండి", "quote": "స్మార్ట్ వ్యవసాయం<br>మెరుగైన<br>రేపటి కోసం", "alternative": "📋 ప్రత్యామ్నాయ పంట సిఫార్సులను చూడండి",
    },
    "Tamil": {
        "rotation_plan": "பயிர் சுழற்சி திட்டம் (4 ஆண்டுகள்)", "year": "ஆண்டு",
        "rotation_message": "🌱 இந்த பயிர் சுழற்சி மண் ஆரோக்கியம், பயிர் பன்முகத்தன்மை மற்றும் சிறந்த வள மேலாண்மைக்கு உதவுகிறது.",
        "temperature": "வெப்பநிலை", "ai_recommendation": "✨ AI பரிந்துரை", "recommended_crop_label": "பரிந்துரைக்கப்பட்ட பயிர்",
        "suitability_score": "பொருத்த மதிப்பெண்", "farm_performance": "📊 பண்ணை செயல்திறன்", "water_usage": "நீர் பயன்பாடு",
        "current_rotation": "தற்போதைய சுழற்சி", "soil_health_label": "மண் ஆரோக்கியம்", "current_status": "தற்போதைய நிலை",
        "expected_yield": "எதிர்பார்க்கப்படும் விளைச்சல்", "estimated_per_acre": "ஒரு ஏக்கருக்கான மதிப்பீடு", "sustainability_score": "நிலைத்தன்மை மதிப்பெண்", "overall": "மொத்தம்",
        "smart_insights": "💡 ஸ்மார்ட் தகவல்கள்", "recommendation": "பரிந்துரை", "highest_ranked": "தேர்ந்தெடுக்கப்பட்ட பண்ணை நிலைமைகளில் அதிக மதிப்பெண் பெற்ற அடுத்த பயிராகும்.",
        "generate_download": "📄 அறிக்கையை உருவாக்கி பதிவிறக்கவும்", "report_description": "உங்கள் பண்ணை நிலைமைகள், பரிந்துரை, மதிப்பெண் மற்றும் பயிர் சுழற்சி திட்டத்தை கொண்ட விரிவான அறிக்கையைப் பெறுங்கள்.",
        "download_report_button": "⬇️ அறிக்கையைப் பதிவிறக்கவும்", "quote": "ஸ்மார்ட் விவசாயம்<br>சிறந்த<br>நாளைக்காக", "alternative": "📋 மாற்று பயிர் பரிந்துரைகளைக் காண்க",
    },
}
ui = DASHBOARD_TRANSLATIONS[language]

st.sidebar.markdown("---")
st.sidebar.markdown(f"### 🌾 {t['farm_details']}")

farmer_name = st.sidebar.text_input(
    t["farmer_name"],
    placeholder=t["farmer_placeholder"],
    key="farmer_name_final"
)
location = st.sidebar.text_input(
    t["location"],
    placeholder=t["location_placeholder"],
    key="location_final"
)
land_size = st.sidebar.number_input(
    t["land_size"], min_value=0.1, max_value=10000.0,
    value=1.0, step=0.5, key="land_size_final"
)

soil_options = ["Loamy", "Clay", "Black Soil", "Sandy", "Red Soil"]
soil_display_options = [translated_soil(x, language) for x in soil_options]
soil_type_display = st.sidebar.selectbox(
    t["soil_type"], soil_display_options, key="soil_type_final"
)
soil_type = soil_options[soil_display_options.index(soil_type_display)]

water_options = ["Low", "Medium", "High"]
water_display_options = [translated_value(x, language) for x in water_options]
water_display = st.sidebar.selectbox(
    t["water"], water_display_options, key="water_final"
)
water_availability = water_options[water_display_options.index(water_display)]

rainfall_options = ["Low", "Medium", "High"]
rainfall_display_options = [translated_value(x, language) for x in rainfall_options]
rainfall_display = st.sidebar.selectbox(
    "🌧️ Expected Rainfall",
    rainfall_display_options,
    index=1,
    key="rainfall_final"
)
rainfall_availability = rainfall_options[rainfall_display_options.index(rainfall_display)]

season_options = ["Kharif", "Rabi", "Summer"]
season_display_options = [t["all_seasons"]] + [translated_value(x, language) for x in season_options]
season_display = st.sidebar.selectbox(
    f"🗓️ {t['season']}", season_display_options, key="season_final"
)
selected_season = (
    None
    if season_display == t["all_seasons"]
    else season_options[season_display_options.index(season_display) - 1]
)

crop_options_all = list(crop_data.keys())
if selected_season:
    crop_options = [
        crop for crop in crop_options_all
        if selected_season in crop_data[crop]["season"]
    ]
    if not crop_options:
        crop_options = crop_options_all
else:
    crop_options = crop_options_all

crop_display_options = [translated_crop(x, language) for x in crop_options]
current_crop_display = st.sidebar.selectbox(
    t["current_crop"], crop_display_options, key="current_crop_final"
)
current_crop = crop_options[crop_display_options.index(current_crop_display)]

previous_display_options = [t["none"]] + crop_display_options
previous_crop_display = st.sidebar.selectbox(
    t["previous_crop"], previous_display_options, key="previous_crop_final"
)
previous_crop = "None" if previous_crop_display == t["none"] else crop_options[crop_display_options.index(previous_crop_display)]

generate = st.sidebar.button(
    t["generate"], use_container_width=True, type="primary", key="generate_final"
)

# =========================================================
# SESSION STATE
# =========================================================

if "recommendations_final" not in st.session_state:
    st.session_state.recommendations_final = None

if generate:
    st.session_state.recommendations_final = calculate_recommendations(
        current_crop=current_crop,
        previous_crop=previous_crop,
        soil_type=soil_type,
        water_availability=water_availability,
        preferred_season=selected_season,
        rainfall_availability=rainfall_availability,
    )

recommendations = st.session_state.recommendations_final

# Show a useful dashboard immediately. The recommendation values update when Generate is pressed.
if not recommendations:
    recommendations = calculate_recommendations(
        current_crop=current_crop,
        previous_crop=previous_crop,
        soil_type=soil_type,
        water_availability=water_availability,
        preferred_season=selected_season,
        rainfall_availability=rainfall_availability,
    )

best = recommendations[0]
best_crop = best["Crop"]
best_crop_display = translated_crop(best_crop, language)
max_possible_score = 21  # 18 original + 3 possible from rainfall_score
suitability = max(0, min(100, round(best["Score"] / max_possible_score * 100)))

# ---------------------------------------------------------
# HABIT BASELINE — what if the farmer repeats the same crop?
# ---------------------------------------------------------
repeat = calculate_repeat_score(
    current_crop=current_crop,
    soil_type=soil_type,
    water_availability=water_availability,
    preferred_season=selected_season,
    rainfall_availability=rainfall_availability,
)
repeat_suitability = max(0, min(100, round(repeat["Score"] / max_possible_score * 100)))

recommended_risk = yield_risk_label(suitability)
repeat_risk = yield_risk_label(repeat_suitability)
suitability_gap = suitability - repeat_suitability

RISK_COLORS = {"Low": "#1c7a3f", "Medium": "#b8860b", "High": "#c0392b"}
RISK_TEXT = {
    "English": {"Low": "Low risk", "Medium": "Medium risk", "High": "High risk"},
    "Kannada": {"Low": "ಕಡಿಮೆ ಅಪಾಯ", "Medium": "ಮಧ್ಯಮ ಅಪಾಯ", "High": "ಹೆಚ್ಚಿನ ಅಪಾಯ"},
    "Hindi": {"Low": "कम जोखिम", "Medium": "मध्यम जोखिम", "High": "अधिक जोखिम"},
    "Telugu": {"Low": "తక్కువ ప్రమాదం", "Medium": "మధ్యస్థ ప్రమాదం", "High": "అధిక ప్రమాదం"},
    "Tamil": {"Low": "குறைந்த ஆபத்து", "Medium": "நடுத்தர ஆபத்து", "High": "அதிக ஆபத்து"},
}[language]

HABIT_TEXT = {
    "English": {
        "title": "🔁 Habit vs. Recommended",
        "sub": "What repeating the same crop looks like next to the AI recommendation.",
        "repeat_label": "If you grow the same crop again",
        "rec_label": "If you follow the recommendation",
        "risk_of": "risk of declining yield / soil health if repeated",
        "gap_note": "Repeating the same crop scores lower mainly because it skips crop diversification and carries a same-crop penalty in the model — not because the crop itself is bad.",
        "model_note": "This scoring engine is rule-based. The same recommendation can also be produced by SmartCrop, a Random Forest model trained on soil and climate features — Furrow is the decision-support interface, SmartCrop is the ML layer behind it.",
    },
    "Kannada": {
        "title": "🔁 ಅಭ್ಯಾಸ vs ಶಿಫಾರಸು",
        "sub": "ಅದೇ ಬೆಳೆಯನ್ನು ಮತ್ತೆ ಬೆಳೆದರೆ ಏನಾಗುತ್ತದೆ ಎಂಬುದನ್ನು AI ಶಿಫಾರಸಿನೊಂದಿಗೆ ಹೋಲಿಸಿ.",
        "repeat_label": "ಅದೇ ಬೆಳೆಯನ್ನು ಮತ್ತೆ ಬೆಳೆದರೆ",
        "rec_label": "ಶಿಫಾರಸನ್ನು ಅನುಸರಿಸಿದರೆ",
        "risk_of": "ಪುನರಾವರ್ತಿಸಿದರೆ ಇಳುವರಿ/ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಕುಸಿಯುವ ಅಪಾಯ",
        "gap_note": "ಅದೇ ಬೆಳೆಯ ಪುನರಾವರ್ತನೆ ಕಡಿಮೆ ಅಂಕ ಪಡೆಯುತ್ತದೆ ಏಕೆಂದರೆ ಇದು ಬೆಳೆ ವೈವಿಧ್ಯತೆಯನ್ನು ಬಿಟ್ಟುಬಿಡುತ್ತದೆ ಮತ್ತು ಮಾದರಿಯಲ್ಲಿ ದಂಡವನ್ನು ಹೊಂದಿದೆ — ಬೆಳೆ ಸ್ವತಃ ಕೆಟ್ಟದ್ದಲ್ಲ.",
        "model_note": "ಈ ಸ್ಕೋರಿಂಗ್ ಎಂಜಿನ್ ನಿಯಮ ಆಧಾರಿತವಾಗಿದೆ. ಇದೇ ಶಿಫಾರಸನ್ನು ಮಣ್ಣು ಮತ್ತು ಹವಾಮಾನ ಆಧಾರಿತ SmartCrop Random Forest ಮಾದರಿಯಿಂದಲೂ ಪಡೆಯಬಹುದು — Furrow ನಿರ್ಧಾರ-ಸಹಾಯಕ ಇಂಟರ್ಫೇಸ್, SmartCrop ಅದರ ಹಿಂದಿನ ML ಪದರ.",
    },
    "Hindi": {
        "title": "🔁 आदत बनाम सुझाव",
        "sub": "वही फसल दोबारा उगाने पर क्या होगा, AI सुझाव के मुकाबले।",
        "repeat_label": "यदि आप वही फसल फिर से उगाते हैं",
        "rec_label": "यदि आप सुझाव अपनाते हैं",
        "risk_of": "दोहराने पर उपज/मिट्टी स्वास्थ्य घटने का जोखिम",
        "gap_note": "वही फसल दोहराने पर स्कोर कम आता है क्योंकि इसमें फसल विविधता नहीं है और मॉडल में समान-फसल दंड लगता है — फसल खुद खराब नहीं है।",
        "model_note": "यह स्कोरिंग इंजन नियम-आधारित है। यही सुझाव मिट्टी और जलवायु सुविधाओं पर प्रशिक्षित SmartCrop Random Forest मॉडल से भी मिल सकता है — Furrow निर्णय-सहायता इंटरफ़ेस है, SmartCrop उसके पीछे का ML स्तर है।",
    },
    "Telugu": {
        "title": "🔁 అలవాటు vs సిఫార్సు",
        "sub": "అదే పంటను మళ్ళీ వేస్తే ఏమవుతుందో AI సిఫార్సుతో పోల్చండి.",
        "repeat_label": "అదే పంటను మళ్ళీ వేస్తే",
        "rec_label": "సిఫార్సును అనుసరిస్తే",
        "risk_of": "పునరావృతం చేస్తే దిగుబడి/నేల ఆరోగ్యం తగ్గే ప్రమాదం",
        "gap_note": "అదే పంటను పునరావృతం చేయడం తక్కువ స్కోర్ పొందుతుంది ఎందుకంటే ఇది పంట వైవిధ్యాన్ని వదిలివేస్తుంది మరియు మోడల్‌లో అదే-పంట పెనాల్టీ ఉంటుంది — పంట స్వయంగా చెడ్డది కాదు.",
        "model_note": "ఈ స్కోరింగ్ ఇంజిన్ నియమ-ఆధారితమైనది. ఇదే సిఫార్సును నేల మరియు వాతావరణ లక్షణాలపై శిక్షణ పొందిన SmartCrop Random Forest మోడల్ కూడా ఇవ్వగలదు — Furrow నిర్ణయ-సహాయక ఇంటర్‌ఫేస్, SmartCrop దాని వెనుక ఉన్న ML లేయర్.",
    },
    "Tamil": {
        "title": "🔁 பழக்கம் vs பரிந்துரை",
        "sub": "அதே பயிரை மீண்டும் வளர்த்தால் என்ன நடக்கும் என்பதை AI பரிந்துரையுடன் ஒப்பிடுங்கள்.",
        "repeat_label": "அதே பயிரை மீண்டும் வளர்த்தால்",
        "rec_label": "பரிந்துரையை பின்பற்றினால்",
        "risk_of": "மீண்டும் செய்தால் விளைச்சல்/மண் ஆரோக்கியம் குறையும் ஆபத்து",
        "gap_note": "அதே பயிரை மீண்டும் செய்வது குறைந்த மதிப்பெண் பெறுகிறது, ஏனெனில் இது பயிர் பல்வகைமையை தவிர்க்கிறது மற்றும் மாதிரியில் அதே-பயிர் அபராதம் உள்ளது — பயிர் தானாகவே மோசமானது அல்ல.",
        "model_note": "இந்த மதிப்பீட்டு இயந்திரம் விதி அடிப்படையிலானது. இதே பரிந்துரையை மண் மற்றும் காலநிலை அம்சங்களில் பயிற்சி பெற்ற SmartCrop Random Forest மாதிரியும் தரலாம் — Furrow முடிவு-ஆதரவு இடைமுகம், SmartCrop அதற்குப் பின்னால் உள்ள ML அடுக்கு.",
    },
}[language]

# =========================================================
# HERO
# =========================================================

hero_bg = asset_data_uri("hero_field.png")
hero_style = f"background-image:url('{hero_bg}');" if hero_bg else ""

st.markdown(f"""
<div class="hero-exact" style="{hero_style}">
  <div class="hero-exact-content">
    <h1>🌱 Smart Crop Rotation</h1>
    <p>Most farmers repeat the same crop out of habit — Furrow shows what soil- and climate-matched rotation looks like instead.</p>
  </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# TOP CARDS
# =========================================================

location_value = location if location else "Bengaluru, Karnataka"

# ---------------------------------------------------------
# LIVE TEMPERATURE FOR THE SELECTED LOCATION
# ---------------------------------------------------------
temperature_value, resolved_location = temperature_display(location_value)

# If Open-Meteo resolves the location, use its official place
# name in the card. Otherwise keep exactly what the farmer typed.
if resolved_location:
    location_card_value = resolved_location
else:
    location_card_value = location_value

season_card_value = t["all_seasons"] if not selected_season else translated_value(selected_season, language)

top_cards = [
    ("🌱", t["soil_type"], translated_soil(soil_type, language)),
    ("💧", t["water"], translated_value(water_availability, language)),
    ("🌧️", "Rainfall", translated_value(rainfall_availability, language)),
    ("🗓️", t["season"], season_card_value),
    ("🌤️", ui["temperature"], temperature_value),
    ("📍", t["location"], location_card_value),
]

cols = st.columns(6, gap="medium")
for col, (icon, label, value) in zip(cols, top_cards):
    with col:
        st.markdown(f"""
        <div class="top-card">
          <span class="top-icon">{icon}</span>
          <div class="top-label">{label}</div>
          <div class="top-value">{value}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# RECOMMENDATION + ROTATION
# =========================================================

st.markdown(f"<div class='section-head'>🌱 {t['recommended']}</div>", unsafe_allow_html=True)

left, right = st.columns([1.12, 1.15], gap="medium")

with left:
    image_path = crop_asset(best_crop)
    if image_path:
        st.markdown(
            f"<img src='{image_path}' class='featured-img'>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='dash-panel' style='height:300px;display:flex;"
            "align-items:center;justify-content:center;font-size:80px'>🌱</div>",
            unsafe_allow_html=True
        )

    # Crop name directly below the left-side image.
    st.markdown(
        f"<div class='featured-crop-name'>{best_crop_display}</div>",
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="dash-panel rec-panel" style="margin-top:10px">
      <div class="rec-badge">✨ AI RECOMMENDATION</div>
      <div class="rec-title">Recommended Crop</div>
      <div class="rec-crop">{best_crop_display}</div>
      <div class="rec-line">🎯 <b>Suitability Score:</b> {suitability}%</div>
      <div class="rec-line">💧 <b>{t['water_requirement']}:</b> {translated_value(best['Water Requirement'], language)}</div>
      <div class="rec-line">🌱 <b>{t['suitable_soil']}:</b> {translated_soil_list(best['Suitable Soil'], language)}</div>
      <div class="rec-line">♻️ <b>{t['soil_health']}:</b> {best['Soil Health']} / 3</div>
      <div class="rec-line">💰 <b>{t['growing_season']}:</b> {translated_season_list(best['Season'], language)}</div>
      <div class="rec-line">🗓️ <b>{t['season']} {t['recommendation_score']}:</b> {best['Season Score']} / 3</div>
    </div>
    """, unsafe_allow_html=True)

with right:
    rotation = [current_crop]
    if best_crop not in rotation:
        rotation.append(best_crop)
    for recommendation in recommendations:
        crop = recommendation["Crop"]
        if crop not in rotation:
            rotation.append(crop)
        if len(rotation) >= 4:
            break

    # IMPORTANT: use a real Streamlit container instead of opening/closing
    # an HTML div around Streamlit widgets. HTML divs cannot wrap separate
    # Streamlit elements, which was causing the large empty card.
    with st.container(border=True):
        st.markdown(
            f"<h2 style='color:#10251a;margin:0 0 18px'>{ui['rotation_plan']}</h2>",
            unsafe_allow_html=True
        )

        rcols = st.columns(len(rotation) * 2 - 1)

        for i, crop in enumerate(rotation):
            with rcols[i * 2]:
                p = crop_asset(crop)

                if p:
                    st.markdown(
                        f"<img src='{p}' class='rotation-img'>",
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        "<div class='rotation-fallback'>🌱</div>",
                        unsafe_allow_html=True
                    )

                # Year 1 is explicitly marked as the current year.
                year_label = (
                    f"{ui['year']} 1 (Current Year)"
                    if i == 0
                    else f"{ui['year']} {i + 1}"
                )

                # Crop name is always shown directly below its image.
                # For every crop after Year 1, add a short "why" line pulled
                # from the crop's benefit text so the timeline reads as an
                # explained plan, not just a list of names.
                reason_html = ""
                if i > 0:
                    reason_text = translated_benefit(crop, language)
                    if len(reason_text) > 70:
                        reason_text = reason_text[:67].rsplit(" ", 1)[0] + "…"
                    reason_html = f"<div class='rotation-reason'>{reason_text}</div>"

                st.markdown(
                    f"<div class='rotation-year'>{year_label}</div>"
                    f"<div class='rotation-title'>{translated_crop(crop, language)}</div>"
                    f"{reason_html}",
                    unsafe_allow_html=True
                )

            if i < len(rotation) - 1:
                with rcols[i * 2 + 1]:
                    st.markdown(
                        "<div class='rot-arrow'>→</div>",
                        unsafe_allow_html=True
                    )

        st.markdown(
            f"<div style='margin-top:18px;background:#eef5df;border-radius:14px;"
            f"padding:14px;color:#35503b;font-size:13px'>{ui['rotation_message']}</div>",
            unsafe_allow_html=True
        )

# =========================================================
# HABIT VS RECOMMENDED
# =========================================================

st.markdown(f"<div class='section-head'>{HABIT_TEXT['title']}</div>", unsafe_allow_html=True)
st.markdown(
    f"<div style='color:#4d5f52;font-size:14px;margin:-8px 0 14px'>{HABIT_TEXT['sub']}</div>",
    unsafe_allow_html=True
)

# Headline number — the single stat worth quoting out loud.
if suitability_gap > 0:
    headline_stat = f"+{suitability_gap} points"
    headline_sub = f"better suitability than repeating {translated_crop(current_crop, language)}"
elif suitability_gap < 0:
    headline_stat = f"{suitability_gap} points"
    headline_sub = f"lower than repeating {translated_crop(current_crop, language)} for this combination"
else:
    headline_stat = "No gap"
    headline_sub = "this recommendation ties the habit baseline for this combination"

st.markdown(f"""
<div style='background:linear-gradient(135deg,#16723b,#1c8a48);border-radius:18px;
padding:20px 24px;margin-bottom:14px;display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;
box-shadow:0 8px 22px rgba(22,114,59,.25)'>
  <div style='color:#ffffff;font-size:38px;font-weight:850;line-height:1'>{headline_stat}</div>
  <div style='color:#e3f3d8;font-size:14px'>{headline_sub}</div>
</div>
""", unsafe_allow_html=True)

habit_col, rec_col = st.columns(2, gap="medium")

with habit_col:
    st.markdown(f"""
    <div class='dash-panel' style='border-left:5px solid {RISK_COLORS[repeat_risk]}'>
      <div class='top-label' style='margin-bottom:6px'>{HABIT_TEXT['repeat_label']}</div>
      <div class='rec-crop' style='font-size:26px;margin-bottom:6px'>{translated_crop(current_crop, language)}</div>
      <div class='rec-line'>🎯 <b>{ui['suitability_score']}:</b> {repeat_suitability}%</div>
      <div class='rec-line' style='color:{RISK_COLORS[repeat_risk]};font-weight:800'>⚠️ {RISK_TEXT[repeat_risk]} — {HABIT_TEXT['risk_of']}</div>
      <div class='progress'><div style='width:{repeat_suitability}%;background:{RISK_COLORS[repeat_risk]}'></div></div>
    </div>
    """, unsafe_allow_html=True)

with rec_col:
    st.markdown(f"""
    <div class='dash-panel rec-panel' style='border-left:5px solid {RISK_COLORS[recommended_risk]}'>
      <div class='top-label' style='margin-bottom:6px'>{HABIT_TEXT['rec_label']}</div>
      <div class='rec-crop' style='font-size:26px;margin-bottom:6px'>{best_crop_display}</div>
      <div class='rec-line'>🎯 <b>{ui['suitability_score']}:</b> {suitability}%</div>
      <div class='rec-line' style='color:{RISK_COLORS[recommended_risk]};font-weight:800'>✅ {RISK_TEXT[recommended_risk]} — {HABIT_TEXT['risk_of']}</div>
      <div class='progress'><div style='width:{suitability}%;background:{RISK_COLORS[recommended_risk]}'></div></div>
    </div>
    """, unsafe_allow_html=True)

gap_word = "+" if suitability_gap >= 0 else ""
st.markdown(
    f"<div style='margin-top:14px;background:#eef5df;border-radius:14px;padding:14px;"
    f"color:#35503b;font-size:13px'>📈 <b>{gap_word}{suitability_gap} points</b> — {HABIT_TEXT['gap_note']}"
    f"<br><span style='opacity:0.85'>🤖 {HABIT_TEXT['model_note']}</span></div>",
    unsafe_allow_html=True
)

# =========================================================
# KPI ROW
# =========================================================

st.markdown("<div class='section-head'>📊 Farm Performance</div>", unsafe_allow_html=True)

water_usage = {"Low": 90, "Medium": 65, "High": 45}[water_availability]
soil_health = max(40, min(95, 55 + best["Soil Score"] * 4 + best["Soil Health"] * 5))
expected_yield = max(12, round(12 + suitability * 0.11, 1))
sustainability = max(45, min(98, round((suitability * 0.65) + (best["Soil Health"] / 3 * 35))))

kpis = [
    ("💧", "Water Usage", f"{water_usage}%", "Current Rotation", water_usage),
    ("🌱", "Soil Health", f"{soil_health}%", "Current Status", soil_health),
    ("📈", "Expected Yield", f"{expected_yield} Q", f"{RISK_TEXT[recommended_risk]} of decline (est.)", min(100, int(expected_yield / 35 * 100))),
    ("♻️", "Sustainability Score", f"{sustainability}/100", "Overall", sustainability),
]

kcols = st.columns(4, gap="medium")
for col, (icon, label, value, sub, pct) in zip(kcols, kpis):
    with col:
        st.markdown(f"""
        <div class='kpi-card'>
          <div class='kpi-label'>{icon} {label}</div>
          <div class='kpi-value'>{value}</div>
          <div class='kpi-sub'>{sub}</div>
          <div class='kpi-bar'><div class='kpi-fill' style='width:{pct}%'></div></div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# MULTI-YEAR SOIL HEALTH TREND
# =========================================================
# Light version of a "cumulative soil health" view: reuse the same
# soil_score()/legume-bonus logic already used for the single-crop
# soil_health KPI, applied per year of the rotation, so a rotation
# with 2+ legumes visibly trends upward instead of only showing one
# point-in-time score.

TREND_TEXT = {
    "English": {"title": "📈 4-Year Soil Health Trend", "sub": "Estimated soil-health score for each year of this rotation (heuristic, not measured data).", "legumes": "legume year(s) in this plan"},
    "Kannada": {"title": "📈 4-ವರ್ಷದ ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಪ್ರವೃತ್ತಿ", "sub": "ಈ ಪರ್ಯಾಯದ ಪ್ರತಿ ವರ್ಷಕ್ಕೂ ಅಂದಾಜು ಮಣ್ಣಿನ ಆರೋಗ್ಯ ಅಂಕ (ಅಳತೆ ಮಾಡಿದ ಡೇಟಾ ಅಲ್ಲ).", "legumes": "ದ್ವಿದಳ ಧಾನ್ಯ ವರ್ಷ(ಗಳು)"},
    "Hindi": {"title": "📈 4-वर्षीय मिट्टी स्वास्थ्य रुझान", "sub": "इस चक्र के प्रत्येक वर्ष के लिए अनुमानित मिट्टी स्वास्थ्य स्कोर (मापा गया डेटा नहीं)।", "legumes": "दलहनी वर्ष"},
    "Telugu": {"title": "📈 4-సంవత్సరాల నేల ఆరోగ్య ధోరణి", "sub": "ఈ మార్పిడిలో ప్రతి సంవత్సరానికి అంచనా నేల ఆరోగ్య స్కోర్ (కొలిచిన డేటా కాదు).", "legumes": "పప్పుధాన్య సంవత్సరం(లు)"},
    "Tamil": {"title": "📈 4-ஆண்டு மண் ஆரோக்கிய போக்கு", "sub": "இந்த சுழற்சியின் ஒவ்வொரு ஆண்டிற்கும் மதிப்பிடப்பட்ட மண் ஆரோக்கிய மதிப்பெண் (அளவிடப்பட்ட தரவு அல்ல).", "legumes": "பருப்பு ஆண்டு(கள்)"},
}[language]

st.markdown(f"<div class='section-head'>{TREND_TEXT['title']}</div>", unsafe_allow_html=True)
st.markdown(
    f"<div style='color:#4d5f52;font-size:13px;margin:-8px 0 14px'>{TREND_TEXT['sub']}</div>",
    unsafe_allow_html=True
)

trend_scores = []
legume_years = 0
for crop in rotation:
    c_info = crop_data[crop]
    c_soil_score = soil_score(soil_type, c_info["soil"])
    c_legume_bonus = 3 if c_info["legume"] else 0
    if c_info["legume"]:
        legume_years += 1
    year_health = max(40, min(95, 55 + c_soil_score * 4 + c_legume_bonus * 5))
    trend_scores.append(year_health)

trend_df = pd.DataFrame(
    {"Soil Health %": trend_scores},
    index=[f"{ui['year']} {i+1}" for i in range(len(rotation))]
)
st.bar_chart(trend_df, color="#277346", use_container_width=True)

st.markdown(
    f"<div style='color:#526158;font-size:13px;margin-top:-6px'>🌱 {legume_years} {TREND_TEXT['legumes']} in this 4-year plan.</div>",
    unsafe_allow_html=True
)

# =========================================================
# SMART INSIGHTS + FARMER IMAGE
# =========================================================

st.markdown("<div class='section-head'>💡 Smart Insights</div>", unsafe_allow_html=True)

ins1, ins2, ins3, ins4 = st.columns(4, gap="medium")
if water_availability == "Low":
    water_message = t["low_water_message"]
elif water_availability == "Medium":
    water_message = t["medium_water_message"]
else:
    water_message = t["high_water_message"]

with ins1:
    st.markdown(f"<div class='insight-card'><h4>💧 Water Management</h4><p>{water_message}</p></div>", unsafe_allow_html=True)
with ins2:
    if crop_data[best_crop]["legume"]:
        msg = t["legume_message"]
    else:
        msg = t["rotation_message"]
    st.markdown(f"<div class='insight-card'><h4>🌱 Soil Health</h4><p>{msg}</p></div>", unsafe_allow_html=True)
with ins3:
    st.markdown(f"<div class='insight-card'><h4>🎯 Recommendation</h4><p><b>{best_crop_display}</b> is the highest-ranked next crop under the selected farm conditions.</p></div>", unsafe_allow_html=True)
with ins4:
    st.markdown(f"<div class='insight-card'><h4>🤖 Model</h4><p>{HABIT_TEXT['model_note']}</p></div>", unsafe_allow_html=True)

# =========================================================
# REPORT + FARMER IMAGE
# =========================================================

report_left, report_right = st.columns([1.15, 1], gap="medium")

farmer_img = asset_data_uri("farmer.png")
with report_left:
    st.markdown("""
    <div class='report-card'>
      <h3>📄 Generate & Download Report</h3>
      <p>Get a detailed report containing your farm conditions, recommendation, score and crop rotation plan.</p>
    </div>
    """, unsafe_allow_html=True)

    farmer_display = farmer_name if farmer_name else "Not provided"
    previous_display = t["none"] if previous_crop == "None" else translated_crop(previous_crop, language)
    report_lines = [
        "SMART CROP ROTATION REPORT", "=" * 40,
        f"Farmer: {farmer_display}", f"Location: {location_card_value}", f"Temperature: {temperature_value}", f"Land Size: {land_size} acres",
        f"Soil Type: {translated_soil(soil_type, language)}", f"Water Availability: {translated_value(water_availability, language)}",
        f"Expected Rainfall: {translated_value(rainfall_availability, language)}",
        f"Season: {season_card_value}",
        f"Current Crop: {translated_crop(current_crop, language)}", f"Previous Crop: {previous_display}", "",
        f"Recommended Crop: {best_crop_display}", f"Suitability Score: {suitability}%",
        f"Water Requirement: {translated_value(best['Water Requirement'], language)}",
        f"Suitable Soil: {translated_soil_list(best['Suitable Soil'], language)}",
        f"Growing Season: {translated_season_list(best['Season'], language)}", f"Reason: {translated_benefit(best_crop, language)}", "",
        "HABIT VS RECOMMENDED", "-" * 40,
        f"If you repeat {translated_crop(current_crop, language)}: {repeat_suitability}% suitability ({RISK_TEXT[repeat_risk]} of declining yield/soil health)",
        f"If you follow the recommendation ({best_crop_display}): {suitability}% suitability ({RISK_TEXT[recommended_risk]} of declining yield/soil health)",
        f"Gap: {gap_word}{suitability_gap} points in favor of the recommendation" if suitability_gap != 0 else "Gap: no difference for this combination",
        "", "MODEL NOTE", "-" * 40,
        "This report uses a rule-based scoring engine (Furrow). The same",
        "recommendation can also be produced by SmartCrop, a Random Forest",
        "model trained on soil and climate features, as an ML-backed",
        "alternative to this rule-based engine.",
        "",
        "4-YEAR ROTATION PLAN"
    ]
    for i, crop in enumerate(rotation):
        report_lines.append(f"Year 1 (Current Year): {translated_crop(crop, language)}" if i == 0 else f"Year {i+1}: {translated_crop(crop, language)}")
    report_lines += [
        "",
        "NOTE ON ESTIMATES: Suitability scores and risk labels are heuristic,",
        "derived from soil/water/rainfall/season matching rules — they are not",
        "measured yield data or a validated agronomic forecast.",
        "",
        "This report is decision-support information for crop planning."
    ]
    report = "\n".join(report_lines)
    st.download_button("⬇️ Download Report", data=report, file_name="smart_crop_rotation_report.txt", mime="text/plain", use_container_width=True, key="download_report_final")

with report_right:
    if farmer_img:
        st.markdown(f"""
        <div class='quote-farmer'>
          <img src="{farmer_img}">
          <div class='quote-text'><b>“</b><br>Smart Farming<br>for a Better<br>Tomorrow<br><span style='font-size:25px'>🌱</span></div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("<div class='quote-farmer'><div class='quote-text'>Smart Farming<br>for a Better Tomorrow 🌱</div></div>", unsafe_allow_html=True)

# =========================================================
# ALTERNATIVE RECOMMENDATIONS
# =========================================================

with st.expander("📋 View Alternative Crop Recommendations"):
    rows = []
    for r in recommendations:
        rows.append({
            "Crop": translated_crop(r["Crop"], language),
            "Score": r["Score"],
            "Water": translated_value(r["Water Requirement"], language),
            "Rainfall Fit": r.get("Rainfall Score", 0),
            "Suitable Soil": translated_soil_list(r["Suitable Soil"], language),
            "Season": translated_season_list(r["Season"], language),
            "Season Match": "✅" if r["Season Score"] > 0 else "—",
        })
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
<<<<<<< Updated upstream
st.markdown(f"<div class='footer'>{t['footer']}</div>", unsafe_allow_html=True)
=======
st.markdown(f"<div class='footer'>{t['footer']}</div>", unsafe_allow_html=True)
>>>>>>> Stashed changes
