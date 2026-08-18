import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SmartCrop",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# LANGUAGE DATA
# ============================================================

LANG = {
    "English": {
        "tag": "— Soil-first planning",
        "title": "Grow what your <em>ground</em> is telling you.",
        "description": (
            "Tell SmartCrop your soil, water, and climate — it scores "
            "crops against those conditions instead of habit, and lays "
            "out a rotation that helps keep the field's nutrients in "
            "balance across seasons."
        ),
        "field": "Field conditions",
        "inputs": "01 — inputs",
        "soil": "Soil type",
        "ph": "Soil pH",
        "water": "Water availability",
        "climate": "Climate zone",
        "season": "Starting season",
        "length": "Rotation length",
        "last": "Last crop grown here (optional)",
        "none": "None / left fallow",
        "help": "Used to avoid repeating the same crop family and to plan nutrient recovery.",
        "advanced": "Advanced soil & climate data",
        "nitrogen": "Nitrogen (N)",
        "phosphorus": "Phosphorus (P)",
        "potassium": "Potassium (K)",
        "rainfall": "Annual rainfall (mm)",
        "temperature": "Average temperature (°C)",
        "organic": "Organic matter (%)",
        "button": "Chart my rotation →",
        "plan": "Your crop plan",
        "recommendations": "02 — recommendations",
        "recommendation": "Recommendation",
        "score": "Field fit score",
        "rotation": "Suggested rotation",
        "rotation_number": "03 — seasons",
        "footer": "SMARTCROP · SOIL-FIRST CROP PLANNING · ML-ASSISTED DECISION SUPPORT",
        "soil_options": ["Loamy", "Clay", "Sandy", "Silty", "Black soil", "Red soil"],
        "water_options": [
            "Rainfed (low)",
            "Partial irrigation (medium)",
            "Good irrigation (high)"
        ],
        "climate_options": [
            "Semi-arid",
            "Tropical",
            "Sub-tropical",
            "Temperate",
            "Arid"
        ],
        "season_options": [
            "Kharif (monsoon, Jun–Oct)",
            "Rabi (winter, Nov–Mar)",
            "Zaid (summer, Mar–Jun)"
        ],
        "rotation_options": ["3 seasons", "4 seasons", "6 seasons"],
        "crop_options": [
            "None / left fallow",
            "Rice",
            "Wheat",
            "Maize",
            "Cotton",
            "Groundnut",
            "Chickpea",
            "Millet"
        ],
        "season_label": "Season"
    },

    "ಕನ್ನಡ": {
        "tag": "— ಮಣ್ಣು ಆಧಾರಿತ ಯೋಜನೆ",
        "title": "ನಿಮ್ಮ <em>ಮಣ್ಣು</em> ಹೇಳುವುದನ್ನು ಬೆಳೆಸಿ.",
        "description": (
            "ನಿಮ್ಮ ಮಣ್ಣು, ನೀರು ಮತ್ತು ಹವಾಮಾನದ ಮಾಹಿತಿಯನ್ನು SmartCrop ಗೆ ನೀಡಿ. "
            "ನಿಮ್ಮ ಪರಿಸ್ಥಿತಿಗೆ ಸೂಕ್ತವಾದ ಬೆಳೆಗಳನ್ನು ಗುರುತಿಸಿ ಬೆಳೆ ಪರಿವರ್ತನೆ "
            "ಯೋಜನೆಯನ್ನು ನೀಡುತ್ತದೆ."
        ),
        "field": "ಹೊಲದ ಪರಿಸ್ಥಿತಿಗಳು",
        "inputs": "01 — ಮಾಹಿತಿ",
        "soil": "ಮಣ್ಣಿನ ಪ್ರಕಾರ",
        "ph": "ಮಣ್ಣಿನ pH",
        "water": "ನೀರಿನ ಲಭ್ಯತೆ",
        "climate": "ಹವಾಮಾನ ವಲಯ",
        "season": "ಪ್ರಾರಂಭದ ಋತು",
        "length": "ಬೆಳೆ ಪರಿವರ್ತನೆ ಅವಧಿ",
        "last": "ಕೊನೆಯ ಬೆಳೆ",
        "none": "ಯಾವುದೂ ಇಲ್ಲ / ಖಾಲಿ",
        "help": "ಅದೇ ಬೆಳೆ ಕುಟುಂಬವನ್ನು ಪುನರಾವರ್ತಿಸುವುದನ್ನು ತಪ್ಪಿಸಲು ಮತ್ತು ಪೋಷಕಾಂಶಗಳ ಪುನಃಪೂರಣಕ್ಕೆ.",
        "advanced": "ಹೆಚ್ಚುವರಿ ಮಣ್ಣು ಮತ್ತು ಹವಾಮಾನ ಮಾಹಿತಿ",
        "nitrogen": "ನೈಟ್ರೋಜನ್ (N)",
        "phosphorus": "ಫಾಸ್ಫರಸ್ (P)",
        "potassium": "ಪೊಟ್ಯಾಸಿಯಂ (K)",
        "rainfall": "ವಾರ್ಷಿಕ ಮಳೆ (mm)",
        "temperature": "ಸರಾಸರಿ ತಾಪಮಾನ (°C)",
        "organic": "ಸಾವಯವ ಪದಾರ್ಥ (%)",
        "button": "ನನ್ನ ಬೆಳೆ ಪರಿವರ್ತನೆಯನ್ನು ಯೋಜಿಸಿ →",
        "plan": "ನಿಮ್ಮ ಬೆಳೆ ಯೋಜನೆ",
        "recommendations": "02 — ಶಿಫಾರಸುಗಳು",
        "recommendation": "ಶಿಫಾರಸು",
        "score": "ಹೊಲ ಹೊಂದಾಣಿಕೆ",
        "rotation": "ಸೂಚಿಸಲಾದ ಬೆಳೆ ಪರಿವರ್ತನೆ",
        "rotation_number": "03 — ಋತುಗಳು",
        "footer": "SMARTCROP · ಮಣ್ಣು ಆಧಾರಿತ ಬೆಳೆ ಯೋಜನೆ · ML ನಿರ್ಧಾರ ಸಹಾಯ",
        "soil_options": ["ಲೋಮಿ", "ಜೇಡಿಮಣ್ಣು", "ಮರಳು ಮಣ್ಣು", "ಸಿಲ್ಟ್ ಮಣ್ಣು", "ಕಪ್ಪು ಮಣ್ಣು", "ಕೆಂಪು ಮಣ್ಣು"],
        "water_options": ["ಮಳೆ ಆಧಾರಿತ (ಕಡಿಮೆ)", "ಭಾಗಶಃ ನೀರಾವರಿ (ಮಧ್ಯಮ)", "ಉತ್ತಮ ನೀರಾವರಿ (ಹೆಚ್ಚು)"],
        "climate_options": ["ಅರೆ-ಶುಷ್ಕ", "ಉಷ್ಣವಲಯ", "ಉಪ-ಉಷ್ಣವಲಯ", "ಸಮಶೀತೋಷ್ಣ", "ಶುಷ್ಕ"],
        "season_options": ["ಖರೀಫ್ (ಮುಂಗಾರು, ಜೂನ್–ಅಕ್ಟೋಬರ್)", "ರಬಿ (ಚಳಿಗಾಲ, ನವೆಂಬರ್–ಮಾರ್ಚ್)", "ಜೈದ್ (ಬೇಸಿಗೆ, ಮಾರ್ಚ್–ಜೂನ್)"],
        "rotation_options": ["3 ಋತುಗಳು", "4 ಋತುಗಳು", "6 ಋತುಗಳು"],
        "crop_options": ["ಯಾವುದೂ ಇಲ್ಲ / ಖಾಲಿ", "ಅಕ್ಕಿ", "ಗೋಧಿ", "ಮೆಕ್ಕೆಜೋಳ", "ಹತ್ತಿ", "ನೆಲಗಡಲೆ", "ಕಡಲೆ", "ಸಿರಿಧಾನ್ಯ"],
        "season_label": "ಋತು"
    },

    "हिन्दी": {
        "tag": "— मिट्टी आधारित योजना",
        "title": "वही उगाएँ जो आपकी <em>मिट्टी</em> कह रही है।",
        "description": (
            "अपनी मिट्टी, पानी और जलवायु की जानकारी दें। SmartCrop "
            "परिस्थितियों के अनुसार फसलों का मूल्यांकन करता है और "
            "फसल चक्र तैयार करता है।"
        ),
        "field": "खेत की स्थिति",
        "inputs": "01 — जानकारी",
        "soil": "मिट्टी का प्रकार",
        "ph": "मिट्टी का pH",
        "water": "पानी की उपलब्धता",
        "climate": "जलवायु क्षेत्र",
        "season": "शुरुआती मौसम",
        "length": "फसल चक्र अवधि",
        "last": "पिछली फसल",
        "none": "कोई नहीं / खाली",
        "help": "एक ही फसल परिवार को बार-बार लगाने से बचने और पोषक तत्वों की पुनर्प्राप्ति के लिए।",
        "advanced": "उन्नत मिट्टी और जलवायु जानकारी",
        "nitrogen": "नाइट्रोजन (N)",
        "phosphorus": "फॉस्फोरस (P)",
        "potassium": "पोटैशियम (K)",
        "rainfall": "वार्षिक वर्षा (mm)",
        "temperature": "औसत तापमान (°C)",
        "organic": "जैविक पदार्थ (%)",
        "button": "मेरा फसल चक्र बनाएँ →",
        "plan": "आपकी फसल योजना",
        "recommendations": "02 — सिफारिशें",
        "recommendation": "सिफारिश",
        "score": "खेत अनुकूलता",
        "rotation": "सुझाया गया फसल चक्र",
        "rotation_number": "03 — मौसम",
        "footer": "SMARTCROP · मिट्टी आधारित फसल योजना · ML निर्णय सहायता",
        "soil_options": ["दोमट", "चिकनी मिट्टी", "बलुई मिट्टी", "गाद वाली मिट्टी", "काली मिट्टी", "लाल मिट्टी"],
        "water_options": ["वर्षा आधारित (कम)", "आंशिक सिंचाई (मध्यम)", "अच्छी सिंचाई (अधिक)"],
        "climate_options": ["अर्ध-शुष्क", "उष्णकटिबंधीय", "उपोष्णकटिबंधीय", "समशीतोष्ण", "शुष्क"],
        "season_options": ["खरीफ (मानसून, जून–अक्टूबर)", "रबी (सर्दी, नवंबर–मार्च)", "जायद (गर्मी, मार्च–जून)"],
        "rotation_options": ["3 मौसम", "4 मौसम", "6 मौसम"],
        "crop_options": ["कोई नहीं / खाली", "चावल", "गेहूँ", "मक्का", "कपास", "मूंगफली", "चना", "बाजरा"],
        "season_label": "मौसम"
    },

    "తెలుగు": {
        "tag": "— నేల ఆధారిత ప్రణాళిక",
        "title": "మీ <em>నేల</em> చెప్పేది పండించండి.",
        "description": (
            "మీ నేల, నీరు మరియు వాతావరణ వివరాలను SmartCrop కు ఇవ్వండి. "
            "మీ పరిస్థితులకు సరిపోయే పంటలను సూచించి పంట మార్పిడి "
            "ప్రణాళికను రూపొందిస్తుంది."
        ),
        "field": "పొలం పరిస్థితులు",
        "inputs": "01 — వివరాలు",
        "soil": "నేల రకం",
        "ph": "నేల pH",
        "water": "నీటి లభ్యత",
        "climate": "వాతావరణ మండలం",
        "season": "ప్రారంభ కాలం",
        "length": "పంట మార్పిడి కాలం",
        "last": "చివరిగా పండించిన పంట",
        "none": "ఏదీ లేదు / ఖాళీ",
        "help": "ఒకే పంట కుటుంబాన్ని వరుసగా పండించకుండా ఉండటానికి.",
        "advanced": "అధునాతన నేల మరియు వాతావరణ సమాచారం",
        "nitrogen": "నైట్రోజన్ (N)",
        "phosphorus": "ఫాస్ఫరస్ (P)",
        "potassium": "పొటాషియం (K)",
        "rainfall": "వార్షిక వర్షపాతం (mm)",
        "temperature": "సగటు ఉష్ణోగ్రత (°C)",
        "organic": "సేంద్రీయ పదార్థం (%)",
        "button": "నా పంట మార్పిడిని రూపొందించండి →",
        "plan": "మీ పంట ప్రణాళిక",
        "recommendations": "02 — సిఫార్సులు",
        "recommendation": "సిఫార్సు",
        "score": "పొలం అనుకూలత",
        "rotation": "సూచించిన పంట మార్పిడి",
        "rotation_number": "03 — కాలాలు",
        "footer": "SMARTCROP · నేల ఆధారిత పంట ప్రణాళిక · ML నిర్ణయ సహాయం",
        "soil_options": ["లోమీ", "బంకమట్టి", "ఇసుక నేల", "సిల్ట్ నేల", "నల్ల నేల", "ఎర్ర నేల"],
        "water_options": ["వర్షాధారిత (తక్కువ)", "పాక్షిక నీటిపారుదల (మధ్యస్థ)", "మంచి నీటిపారుదల (ఎక్కువ)"],
        "climate_options": ["అర్ధ-శుష్క", "ఉష్ణమండల", "ఉప-ఉష్ణమండల", "సమశీతోష్ణ", "శుష్క"],
        "season_options": ["ఖరీఫ్ (వర్షాకాలం, జూన్–అక్టోబర్)", "రబీ (చలికాలం, నవంబర్–మార్చి)", "జైద్ (వేసవి, మార్చి–జూన్)"],
        "rotation_options": ["3 కాలాలు", "4 కాలాలు", "6 కాలాలు"],
        "crop_options": ["ఏదీ లేదు / ఖాళీ", "వరి", "గోధుమ", "మొక్కజొన్న", "పత్తి", "వేరుశెనగ", "శనగ", "సిరిధాన్యం"],
        "season_label": "కాలం"
    },

    "தமிழ்": {
        "tag": "— மண் சார்ந்த திட்டமிடல்",
        "title": "உங்கள் <em>மண்</em> சொல்வதைப் பயிரிடுங்கள்.",
        "description": (
            "உங்கள் மண், நீர் மற்றும் காலநிலை தகவல்களை SmartCrop-க்கு "
            "வழங்குங்கள். அதற்கேற்ற பயிர்களை பரிந்துரைத்து பயிர் சுழற்சி "
            "திட்டத்தை உருவாக்கும்."
        ),
        "field": "வயல் நிலை",
        "inputs": "01 — தகவல்கள்",
        "soil": "மண் வகை",
        "ph": "மண் pH",
        "water": "நீர் கிடைக்கும் நிலை",
        "climate": "காலநிலை பகுதி",
        "season": "தொடக்க பருவம்",
        "length": "பயிர் சுழற்சி காலம்",
        "last": "கடைசியாக பயிரிட்டது",
        "none": "எதுவும் இல்லை / தரிசு",
        "help": "ஒரே பயிர் குடும்பத்தை தொடர்ந்து பயிரிடுவதைத் தவிர்க்க உதவும்.",
        "advanced": "மேம்பட்ட மண் மற்றும் காலநிலை தகவல்",
        "nitrogen": "நைட்ரஜன் (N)",
        "phosphorus": "பாஸ்பரஸ் (P)",
        "potassium": "பொட்டாசியம் (K)",
        "rainfall": "ஆண்டு மழைப்பொழிவு (mm)",
        "temperature": "சராசரி வெப்பநிலை (°C)",
        "organic": "கரிமப் பொருள் (%)",
        "button": "எனது பயிர் சுழற்சியை உருவாக்கு →",
        "plan": "உங்கள் பயிர் திட்டம்",
        "recommendations": "02 — பரிந்துரைகள்",
        "recommendation": "பரிந்துரை",
        "score": "வயல் பொருத்தம்",
        "rotation": "பரிந்துரைக்கப்பட்ட பயிர் சுழற்சி",
        "rotation_number": "03 — பருவங்கள்",
        "footer": "SMARTCROP · மண் சார்ந்த பயிர் திட்டமிடல் · ML முடிவு ஆதரவு",
        "soil_options": ["வண்டல் மண்", "களிமண்", "மணல் மண்", "வண்டல் கலந்த மண்", "கரிசல் மண்", "செம்மண்"],
        "water_options": ["மழை சார்ந்த (குறைவு)", "பகுதி பாசனம் (நடுத்தரம்)", "நல்ல பாசனம் (அதிகம்)"],
        "climate_options": ["அரை வறண்ட", "வெப்பமண்டல", "துணை வெப்பமண்டல", "மிதவெப்ப", "வறண்ட"],
        "season_options": ["கரீஃப் (பருவமழை, ஜூன்–அக்டோபர்)", "ரபி (குளிர்காலம், நவம்பர்–மார்ச்)", "சைத் (கோடை, மார்ச்–ஜூன்)"],
        "rotation_options": ["3 பருவங்கள்", "4 பருவங்கள்", "6 பருவங்கள்"],
        "crop_options": ["எதுவும் இல்லை / தரிசு", "நெல்", "கோதுமை", "மக்காச்சோளம்", "பருத்தி", "நிலக்கடலை", "கொண்டைக்கடலை", "சிறுதானியம்"],
        "season_label": "பருவம்"
    }
}

# ============================================================
# INTERNAL VALUES
# ============================================================

CROP_KEYS = [
    "Rice",
    "Wheat",
    "Maize",
    "Cotton",
    "Groundnut",
    "Chickpea",
    "Millet"
]

CROP_NAMES = {
    "English": {
        "Rice": "Rice",
        "Wheat": "Wheat",
        "Maize": "Maize",
        "Cotton": "Cotton",
        "Groundnut": "Groundnut",
        "Chickpea": "Chickpea",
        "Millet": "Millet"
    },
    "ಕನ್ನಡ": {
        "Rice": "ಅಕ್ಕಿ",
        "Wheat": "ಗೋಧಿ",
        "Maize": "ಮೆಕ್ಕೆಜೋಳ",
        "Cotton": "ಹತ್ತಿ",
        "Groundnut": "ನೆಲಗಡಲೆ",
        "Chickpea": "ಕಡಲೆ",
        "Millet": "ಸಿರಿಧಾನ್ಯ"
    },
    "हिन्दी": {
        "Rice": "चावल",
        "Wheat": "गेहूँ",
        "Maize": "मक्का",
        "Cotton": "कपास",
        "Groundnut": "मूंगफली",
        "Chickpea": "चना",
        "Millet": "बाजरा"
    },
    "తెలుగు": {
        "Rice": "వరి",
        "Wheat": "గోధుమ",
        "Maize": "మొక్కజొన్న",
        "Cotton": "పత్తి",
        "Groundnut": "వేరుశెనగ",
        "Chickpea": "శనగ",
        "Millet": "సిరిధాన్యం"
    },
    "தமிழ்": {
        "Rice": "நெல்",
        "Wheat": "கோதுமை",
        "Maize": "மக்காச்சோளம்",
        "Cotton": "பருத்தி",
        "Groundnut": "நிலக்கடலை",
        "Chickpea": "கொண்டைக்கடலை",
        "Millet": "சிறுதானியம்"
    }
}

# ============================================================
# LANGUAGE SELECTOR
# ============================================================

language = st.selectbox(
    "Language",
    list(LANG.keys()),
    index=0,
    key="language_selector"
)

T = LANG[language]

# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,500;1,500&display=swap');

    .stApp {
        background: #eef0df;
        color: #182018;
    }

    .block-container {
        max-width: 1400px !important;
        padding: 0 !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    .element-container {
        margin-bottom: 0 !important;
    }

    .hero-wrapper {
        min-height: 650px;
        padding: 105px 10%;
        position: relative;
        overflow: hidden;
        border-bottom: 1px solid #d5d8c7;
        box-sizing: border-box;
    }

    .hero-content {
        width: 620px;
        max-width: 70%;
        position: relative;
        z-index: 10;
    }

    .eyebrow {
        font-family: "DM Mono", monospace;
        font-size: 13px;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #315f39;
        margin-bottom: 28px;
    }

    .hero-title {
        font-family: "Playfair Display", Georgia, serif;
        font-size: 72px;
        line-height: 1.03;
        font-weight: 500;
        letter-spacing: -2px;
        margin: 0;
        color: #171d17;
    }

    .hero-title em {
        color: #3e7746;
        font-style: italic;
    }

    .hero-description {
        margin-top: 32px;
        max-width: 570px;
        font-family: Arial, sans-serif;
        font-size: 18px;
        line-height: 1.75;
        color: #465044;
    }

    .hero-lines {
        position: absolute;
        right: -180px;
        top: -150px;
        width: 750px;
        height: 900px;
        opacity: 0.72;
        pointer-events: none;
    }

    .hero-lines .line {
        position: absolute;
        width: 620px;
        height: 980px;
        border: 4px solid #d0cfbd;
        border-left: none;
        border-radius: 50%;
    }

    .hero-lines .line:nth-child(1) { right: 0; }
    .hero-lines .line:nth-child(2) { right: 90px; }
    .hero-lines .line:nth-child(3) { right: 180px; }
    .hero-lines .line:nth-child(4) { right: 270px; }
    .hero-lines .line:nth-child(5) { right: 360px; }

    .section-wrapper {
        padding: 65px 8%;
    }

    .section-heading {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 30px;
    }

    .section-heading h2 {
        font-family: "Playfair Display", Georgia, serif;
        font-size: 36px;
        font-weight: 500;
        margin: 0;
        color: #182018;
    }

    .section-number {
        font-family: "DM Mono", monospace;
        font-size: 13px;
        letter-spacing: 2px;
        color: #182018;
    }

    .input-area {
        margin-left: 8%;
        margin-right: 8%;
        background: #fbfaf4;
        border: 1px solid #d6d8c7;
        border-radius: 20px;
        padding: 35px;
        margin-bottom: 20px;
    }

    label {
        font-family: "DM Mono", monospace !important;
        font-size: 12px !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: #315f39 !important;
    }

    div[data-baseweb="select"] > div {
        background: #f2f3f5 !important;
        border: 1px solid transparent !important;
        border-radius: 9px !important;
        min-height: 50px !important;
    }

    div[data-baseweb="select"] > div:hover {
        border: 1px solid #3e7746 !important;
    }

    div[data-baseweb="input"] > div {
        background: #f2f3f5 !important;
        border: 1px solid transparent !important;
        border-radius: 9px !important;
        min-height: 50px !important;
    }

    div[data-baseweb="input"] > div:hover {
        border: 1px solid #3e7746 !important;
    }

    .stButton > button {
        width: 100%;
        min-height: 55px;
        border-radius: 10px;
        border: none;
        background: #3e7746;
        color: white;
        font-size: 16px;
        font-weight: 600;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #315f39;
        color: white;
        transform: translateY(-1px);
    }

    .stCaption {
        color: #687064 !important;
    }

    div[data-testid="stExpander"] {
        border: 1px solid #cfd2c1 !important;
        border-radius: 10px !important;
        background: transparent !important;
    }

    .result-card {
        background: #fbfaf4;
        border: 1px solid #d6d8c7;
        border-radius: 20px;
        padding: 30px;
        min-height: 190px;
    }

    .result-number {
        font-family: "DM Mono", monospace;
        font-size: 12px;
        letter-spacing: 2px;
        color: #315f39;
        text-transform: uppercase;
    }

    .result-crop {
        font-family: "Playfair Display", Georgia, serif;
        font-size: 36px;
        color: #3e7746;
        margin-top: 15px;
    }

    .result-score {
        margin-top: 12px;
        font-family: Arial, sans-serif;
        color: #465044;
        font-size: 16px;
    }

    .rotation-card {
        background: #fbfaf4;
        border: 1px solid #d6d8c7;
        border-radius: 20px;
        padding: 30px;
        margin-top: 25px;
    }

    .rotation-season {
        font-family: "DM Mono", monospace;
        font-size: 12px;
        letter-spacing: 2px;
        color: #315f39;
        text-transform: uppercase;
    }

    .rotation-crop {
        font-family: "Playfair Display", Georgia, serif;
        font-size: 30px;
        color: #182018;
        margin-top: 8px;
    }

    .rotation-reason {
        color: #687064;
        margin-top: 8px;
        line-height: 1.6;
    }

    .footer {
        margin: 20px 8% 35px;
        padding: 25px;
        text-align: center;
        background: #f7f8f2;
        border-top: 1px solid #d6d8c7;
        font-family: "DM Mono", monospace;
        font-size: 12px;
        letter-spacing: 2px;
        color: #465044;
    }

    @media (max-width: 800px) {

        .hero-wrapper {
            padding: 75px 7%;
            min-height: 600px;
        }

        .hero-content {
            max-width: 100%;
            width: auto;
        }

        .hero-title {
            font-size: 50px;
        }

        .hero-description {
            font-size: 16px;
        }

        .hero-lines {
            opacity: 0.2;
            right: -350px;
        }

        .section-wrapper {
            padding: 45px 6%;
        }

        .input-area {
            margin-left: 6%;
            margin-right: 6%;
            padding: 20px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.html(
    f"""
    <section class="hero-wrapper">

        <div class="hero-content">

            <div class="eyebrow">
                {T["tag"]}
            </div>

            <h1 class="hero-title">
                {T["title"]}
            </h1>

            <div class="hero-description">
                {T["description"]}
            </div>

        </div>

        <div class="hero-lines">
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
            <div class="line"></div>
        </div>

    </section>
    """
)

# ============================================================
# FIELD CONDITIONS
# ============================================================

st.html(
    f"""
    <div class="section-wrapper">

        <div class="section-heading">

            <h2>{T["field"]}</h2>

            <span class="section-number">
                {T["inputs"]}
            </span>

        </div>

    </div>
    """
)

# ============================================================
# FORM AREA
# ============================================================

st.markdown(
    """
    <div class="input-area">
    """,
    unsafe_allow_html=True
)

# ============================================================
# FIRST ROW
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    soil_type = st.selectbox(
        T["soil"],
        T["soil_options"],
        key="soil_type"
    )

with col2:
    soil_ph = st.number_input(
        T["ph"],
        min_value=3.0,
        max_value=10.0,
        value=6.5,
        step=0.1,
        format="%.2f",
        key="soil_ph"
    )

with col3:
    water = st.selectbox(
        T["water"],
        T["water_options"],
        key="water"
    )

# ============================================================
# SECOND ROW
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    climate = st.selectbox(
        T["climate"],
        T["climate_options"],
        key="climate"
    )

with col2:
    season = st.selectbox(
        T["season"],
        T["season_options"],
        key="season"
    )

with col3:
    rotation_length = st.selectbox(
        T["length"],
        T["rotation_options"],
        key="rotation_length"
    )

# ============================================================
# LAST CROP
# ============================================================

last_crop_display = st.selectbox(
    T["last"],
    T["crop_options"],
    key="last_crop"
)

st.caption(T["help"])

# ============================================================
# CONVERT DISPLAY VALUES TO INTERNAL VALUES
# ============================================================

# Map displayed values to internal English values
display_to_internal = {}

for lang_name, data in LANG.items():

    display_to_internal[lang_name] = {}

    for index, display_value in enumerate(data["soil_options"]):
        display_to_internal[lang_name][("soil", display_value)] = [
            "Loamy",
            "Clay",
            "Sandy",
            "Silty",
            "Black soil",
            "Red soil"
        ][index]

    for index, display_value in enumerate(data["water_options"]):
        display_to_internal[lang_name][("water", display_value)] = [
            "Rainfed (low)",
            "Partial irrigation (medium)",
            "Good irrigation (high)"
        ][index]

    for index, display_value in enumerate(data["climate_options"]):
        display_to_internal[lang_name][("climate", display_value)] = [
            "Semi-arid",
            "Tropical",
            "Sub-tropical",
            "Temperate",
            "Arid"
        ][index]

    for index, display_value in enumerate(data["season_options"]):
        display_to_internal[lang_name][("season", display_value)] = [
            "Kharif",
            "Rabi",
            "Zaid"
        ][index]

    for index, display_value in enumerate(data["rotation_options"]):
        display_to_internal[lang_name][("rotation", display_value)] = [
            "3 seasons",
            "4 seasons",
            "6 seasons"
        ][index]

    for index, display_value in enumerate(data["crop_options"]):
        display_to_internal[lang_name][("crop", display_value)] = [
            "None / left fallow",
            "Rice",
            "Wheat",
            "Maize",
            "Cotton",
            "Groundnut",
            "Chickpea",
            "Millet"
        ][index]

soil_internal = display_to_internal[language][("soil", soil_type)]
water_internal = display_to_internal[language][("water", water)]
climate_internal = display_to_internal[language][("climate", climate)]
season_internal = display_to_internal[language][("season", season)]
rotation_internal = display_to_internal[language][("rotation", rotation_length)]
last_crop_internal = display_to_internal[language][("crop", last_crop_display)]

# ============================================================
# ADVANCED DATA
# ============================================================

with st.expander(T["advanced"]):

    col1, col2, col3 = st.columns(3)

    with col1:
        nitrogen = st.number_input(
            T["nitrogen"],
            min_value=0.0,
            max_value=200.0,
            value=60.0,
            key="nitrogen"
        )

    with col2:
        phosphorus = st.number_input(
            T["phosphorus"],
            min_value=0.0,
            max_value=200.0,
            value=40.0,
            key="phosphorus"
        )

    with col3:
        potassium = st.number_input(
            T["potassium"],
            min_value=0.0,
            max_value=200.0,
            value=40.0,
            key="potassium"
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        rainfall = st.number_input(
            T["rainfall"],
            min_value=100.0,
            max_value=5000.0,
            value=700.0,
            key="rainfall"
        )

    with col2:
        temperature = st.number_input(
            T["temperature"],
            min_value=5.0,
            max_value=45.0,
            value=26.0,
            key="temperature"
        )

    with col3:
        organic_matter = st.number_input(
            T["organic"],
            min_value=0.0,
            max_value=20.0,
            value=1.5,
            key="organic_matter"
        )

# ============================================================
# BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2 = st.columns([3, 1])

with button_col2:

    calculate = st.button(
        T["button"],
        use_container_width=True,
        key="calculate"
    )

st.markdown(
    "</div>",
    unsafe_allow_html=True
)

# ============================================================
# CROP RECOMMENDATION ENGINE
# ============================================================

def get_crop_recommendations(
    soil_type,
    soil_ph,
    water,
    climate,
    season,
    nitrogen,
    phosphorus,
    potassium,
    rainfall,
    temperature,
    last_crop
):

    scores = {
        "Rice": 60,
        "Wheat": 60,
        "Maize": 60,
        "Cotton": 60,
        "Groundnut": 60,
        "Chickpea": 60,
        "Millet": 60
    }

    # SOIL
    if soil_type == "Clay":
        scores["Rice"] += 28
        scores["Wheat"] += 20
        scores["Chickpea"] += 10

    elif soil_type == "Sandy":
        scores["Groundnut"] += 28
        scores["Millet"] += 24
        scores["Chickpea"] += 18

    elif soil_type == "Black soil":
        scores["Cotton"] += 28
        scores["Maize"] += 22
        scores["Groundnut"] += 18

    elif soil_type == "Loamy":
        scores["Maize"] += 25
        scores["Chickpea"] += 22
        scores["Groundnut"] += 20

    elif soil_type == "Silty":
        scores["Wheat"] += 23
        scores["Rice"] += 20
        scores["Maize"] += 20

    elif soil_type == "Red soil":
        scores["Groundnut"] += 23
        scores["Millet"] += 22
        scores["Chickpea"] += 18

    # PH
    if 5.5 <= soil_ph <= 7.5:
        scores["Maize"] += 8
        scores["Chickpea"] += 7
        scores["Groundnut"] += 7
        scores["Wheat"] += 6

    if soil_ph < 5.5:
        scores["Millet"] += 8
        scores["Groundnut"] += 5

    if soil_ph > 7.5:
        scores["Wheat"] += 7
        scores["Cotton"] += 6

    # WATER
    if water == "Rainfed (low)":
        scores["Millet"] += 15
        scores["Chickpea"] += 12
        scores["Groundnut"] += 10
        scores["Rice"] -= 15

    elif water == "Partial irrigation (medium)":
        scores["Groundnut"] += 8
        scores["Maize"] += 8
        scores["Chickpea"] += 7

    else:
        scores["Rice"] += 15
        scores["Wheat"] += 10
        scores["Maize"] += 10

    # CLIMATE
    if climate == "Semi-arid":
        scores["Millet"] += 12
        scores["Groundnut"] += 10
        scores["Chickpea"] += 10

    elif climate == "Tropical":
        scores["Rice"] += 12
        scores["Maize"] += 8
        scores["Cotton"] += 8

    elif climate == "Sub-tropical":
        scores["Wheat"] += 10
        scores["Maize"] += 8
        scores["Chickpea"] += 8

    elif climate == "Temperate":
        scores["Wheat"] += 14
        scores["Chickpea"] += 8

    elif climate == "Arid":
        scores["Millet"] += 15
        scores["Chickpea"] += 10

    # SEASON
    if season == "Kharif":
        scores["Rice"] += 8
        scores["Maize"] += 8
        scores["Cotton"] += 8
        scores["Groundnut"] += 8
        scores["Millet"] += 8

    elif season == "Rabi":
        scores["Wheat"] += 12
        scores["Chickpea"] += 12

    elif season == "Zaid":
        scores["Maize"] += 8
        scores["Groundnut"] += 8
        scores["Millet"] += 6

    # NITROGEN
    if nitrogen < 40:
        scores["Chickpea"] += 12
        scores["Groundnut"] += 10

    elif nitrogen > 100:
        scores["Maize"] += 8
        scores["Rice"] += 7

    # RAINFALL
    if rainfall < 500:
        scores["Millet"] += 10
        scores["Chickpea"] += 8
        scores["Rice"] -= 15

    elif rainfall > 1200:
        scores["Rice"] += 12
        scores["Maize"] += 5

    # TEMPERATURE
    if temperature > 28:
        scores["Millet"] += 7
        scores["Cotton"] += 7
        scores["Rice"] += 5

    if temperature < 20:
        scores["Wheat"] += 10
        scores["Chickpea"] += 8

    # LAST CROP
    family = {
        "Rice": "cereal",
        "Wheat": "cereal",
        "Maize": "cereal",
        "Millet": "cereal",
        "Cotton": "cash",
        "Groundnut": "legume",
        "Chickpea": "legume",
        "None / left fallow": None
    }

    previous_family = family.get(last_crop)

    for crop in scores:

        if crop == last_crop:
            scores[crop] -= 20

        if previous_family == "cereal" and family[crop] == "cereal":
            scores[crop] -= 5

        if previous_family == "legume" and family[crop] == "legume":
            scores[crop] -= 4

    # LIMIT
    for crop in scores:
        scores[crop] = max(0, min(99, scores[crop]))

    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )


# ============================================================
# ROTATION ENGINE
# ============================================================

def create_rotation(
    recommendations,
    rotation_length,
    last_crop
):

    crops = [crop for crop, score in recommendations]

    number = int(rotation_length.split()[0])

    rotation = []
    used = set()

    for crop in crops:

        if crop == last_crop:
            continue

        if crop not in used:
            rotation.append(crop)
            used.add(crop)

        if len(rotation) == number:
            break

    while len(rotation) < number:

        for crop in crops:

            if crop != last_crop:
                rotation.append(crop)

                if len(rotation) == number:
                    break

    return rotation


# ============================================================
# CALCULATE
# ============================================================

if calculate:

    recommendations = get_crop_recommendations(
        soil_internal,
        soil_ph,
        water_internal,
        climate_internal,
        season_internal,
        nitrogen,
        phosphorus,
        potassium,
        rainfall,
        temperature,
        last_crop_internal
    )

    rotation = create_rotation(
        recommendations,
        rotation_internal,
        last_crop_internal
    )

    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.html(
        f"""
        <div class="section-wrapper">

            <div class="section-heading">

                <h2>{T["plan"]}</h2>

                <span class="section-number">
                    {T["recommendations"]}
                </span>

            </div>

        </div>
        """
    )

    # ========================================================
    # TOP 3
    # ========================================================

    top_three = recommendations[:3]

    cols = st.columns(3)

    for i, (crop, score) in enumerate(top_three):

        crop_display = CROP_NAMES[language][crop]

        with cols[i]:

            st.html(
                f"""
                <div class="result-card">

                    <div class="result-number">
                        {T["recommendation"]} {i + 1}
                    </div>

                    <div class="result-crop">
                        {crop_display}
                    </div>

                    <div class="result-score">
                        {T["score"]}:
                        <strong>{score}%</strong>
                    </div>

                </div>
                """
            )

    # ========================================================
    # ROTATION HEADER
    # ========================================================

    st.html(
        f"""
        <div class="section-wrapper">

            <div class="section-heading">

                <h2>{T["rotation"]}</h2>

                <span class="section-number">
                    {T["rotation_number"]}
                </span>

            </div>

        </div>
        """
    )

    # ========================================================
    # ROTATION CARDS
    # ========================================================

    season_names = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06"
    ]

    for i, crop in enumerate(rotation):

        crop_display = CROP_NAMES[language][crop]

        if i == 0:

            reason = {
                "English":
                    "Best immediate match for your current soil, climate and water conditions.",
                "ಕನ್ನಡ":
                    "ನಿಮ್ಮ ಪ್ರಸ್ತುತ ಮಣ್ಣು, ಹವಾಮಾನ ಮತ್ತು ನೀರಿನ ಪರಿಸ್ಥಿತಿಗಳಿಗೆ ಅತ್ಯುತ್ತಮ ಹೊಂದಾಣಿಕೆ.",
                "हिन्दी":
                    "आपकी वर्तमान मिट्टी, जलवायु और पानी की स्थिति के लिए सबसे अच्छा विकल्प।",
                "తెలుగు":
                    "మీ ప్రస్తుత నేల, వాతావరణం మరియు నీటి పరిస్థితులకు ఉత్తమంగా సరిపోతుంది.",
                "தமிழ்":
                    "உங்கள் தற்போதைய மண், காலநிலை மற்றும் நீர் நிலைகளுக்கு சிறந்த பொருத்தம்."
            }[language]

        elif crop in ["Chickpea", "Groundnut"]:

            reason = {
                "English":
                    "Legume rotation helps diversify the field and supports nutrient recovery.",
                "ಕನ್ನಡ":
                    "ದ್ವಿದಳ ಧಾನ್ಯ ಬೆಳೆ ಪರಿವರ್ತನೆಯು ಹೊಲದ ವೈವಿಧ್ಯತೆಯನ್ನು ಹೆಚ್ಚಿಸಿ ಪೋಷಕಾಂಶಗಳ ಪುನಃಪೂರಣಕ್ಕೆ ಸಹಾಯ ಮಾಡುತ್ತದೆ.",
                "हिन्दी":
                    "दलहनी फसल का चक्र खेत में विविधता और पोषक तत्वों की पुनर्प्राप्ति में मदद करता है।",
                "తెలుగు":
                    "పప్పుధాన్య పంట మార్పిడి పొలంలో వైవిధ్యాన్ని పెంచి పోషక పునరుద్ధరణకు సహాయపడుతుంది.",
                "தமிழ்":
                    "பருப்பு வகை பயிர் சுழற்சி வயல் பல்வகைமையையும் ஊட்டச்சத்து மீட்பையும் மேம்படுத்துகிறது."
            }[language]

        elif crop == "Millet":

            reason = {
                "English":
                    "A lower-water crop that can improve rotation diversity under semi-arid conditions.",
                "ಕನ್ನಡ":
                    "ಅರೆ-ಶುಷ್ಕ ಪರಿಸ್ಥಿತಿಗಳಲ್ಲಿ ಕಡಿಮೆ ನೀರು ಬೇಕಾಗುವ ಈ ಬೆಳೆ ಪರಿವರ್ತನೆಯ ವೈವಿಧ್ಯತೆಯನ್ನು ಹೆಚ್ಚಿಸುತ್ತದೆ.",
                "हिन्दी":
                    "कम पानी वाली यह फसल अर्ध-शुष्क परिस्थितियों में फसल चक्र की विविधता बढ़ाती है।",
                "తెలుగు":
                    "తక్కువ నీరు అవసరమయ్యే ఈ పంట అర్ధ-శుష్క పరిస్థితుల్లో పంట మార్పిడి వైవిధ్యాన్ని పెంచుతుంది.",
                "தமிழ்":
                    "குறைந்த நீர் தேவையுள்ள இந்த பயிர் அரை வறண்ட சூழலில் பயிர் சுழற்சி பல்வகைமையை மேம்படுத்துகிறது."
            }[language]

        else:

            reason = {
                "English":
                    "Provides crop-family diversity and avoids repeating the same crop continuously.",
                "ಕನ್ನಡ":
                    "ಬೆಳೆ ಕುಟುಂಬದ ವೈವಿಧ್ಯತೆಯನ್ನು ಹೆಚ್ಚಿಸಿ ಒಂದೇ ಬೆಳೆಯನ್ನು ನಿರಂತರವಾಗಿ ಬೆಳೆಸುವುದನ್ನು ತಪ್ಪಿಸುತ್ತದೆ.",
                "हिन्दी":
                    "यह फसल परिवार में विविधता लाती है और लगातार एक ही फसल लगाने से बचाती है।",
                "తెలుగు":
                    "పంట కుటుంబ వైవిధ్యాన్ని పెంచి ఒకే పంటను వరుసగా పండించకుండా చేస్తుంది.",
                "தமிழ்":
                    "பயிர் குடும்ப பல்வகைமையை வழங்கி ஒரே பயிரை தொடர்ந்து பயிரிடுவதைத் தவிர்க்கிறது."
            }[language]

        st.html(
            f"""
            <div class="section-wrapper"
                 style="padding-top: 0; padding-bottom: 15px;">

                <div class="rotation-card">

                    <div class="rotation-season">
                        {T["season_label"]} {season_names[i]}
                    </div>

                    <div class="rotation-crop">
                        {crop_display}
                    </div>

                    <div class="rotation-reason">
                        {reason}
                    </div>

                </div>

            </div>
            """
        )

# ============================================================
# FOOTER
# ============================================================

st.html(
    f"""
    <div class="footer">
        {T["footer"]}
    </div>
    """
)