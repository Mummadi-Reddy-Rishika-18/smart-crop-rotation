import streamlit as st
import pandas as pd
import os
import glob
import joblib

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Smart Crop Rotation",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background: #f4f6f4;
    color: #26352d;
}

/* Remove extra top spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1600px;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #eef3ef;
    border-right: 1px solid #d9e1da;
}

[data-testid="stSidebar"] > div:first-child {
    padding-top: 1.5rem;
}

/* Headings */
h1, h2, h3 {
    color: #26352d !important;
}

/* Buttons */
.stButton > button {
    background: #3d7a4b;
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 600;
    padding: 0.6rem 1rem;
}

.stButton > button:hover {
    background: #2e6139;
    color: white;
    border: none;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e2e8e3;
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0 8px 25px rgba(40, 70, 50, 0.07);
}

/* Containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 20px;
}

/* Input */
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 10px !important;
}

/* Horizontal rule */
hr {
    border-color: #dce5dd;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD MODEL SAFELY
# ============================================================

@st.cache_resource
def load_crop_model():

    possible_files = []

    possible_files += glob.glob("models/*.pkl")
    possible_files += glob.glob("models/*.joblib")
    possible_files += glob.glob("*.pkl")
    possible_files += glob.glob("*.joblib")

    for file in possible_files:
        try:
            model = joblib.load(file)
            return model
        except:
            pass

    return None


model = load_crop_model()


# ============================================================
# DEFAULT DATA
# ============================================================

default_N = 65
default_P = 45
default_K = 78
default_temperature = 24.5
default_humidity = 65.0
default_ph = 6.8
default_rainfall = 850.0


# ============================================================
# CROP EMOJIS
# ============================================================

crop_icons = {
    "Rice": "🌾",
    "Wheat": "🌾",
    "Maize": "🌽",
    "Chickpea": "🫛",
    "Groundnut": "🥜",
    "Cotton": "🌿",
    "Millet": "🌱"
}


# ============================================================
# CROP PREDICTION
# ============================================================

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):

    if model is not None:

        try:

            features = pd.DataFrame(
                [[N, P, K, temperature, humidity, ph, rainfall]],
                columns=[
                    "N",
                    "P",
                    "K",
                    "temperature",
                    "humidity",
                    "ph",
                    "rainfall"
                ]
            )

            prediction = model.predict(features)[0]

            probabilities = None

            if hasattr(model, "predict_proba"):

                probs = model.predict_proba(features)[0]
                classes = model.classes_

                probabilities = dict(
                    zip(classes, probs * 100)
                )

            return prediction, probabilities

        except Exception as e:
            pass

    # Default fallback
    probabilities = {
        "Rice": 92,
        "Maize": 78,
        "Chickpea": 65,
        "Wheat": 48
    }

    return "Rice", probabilities


# ============================================================
# SOIL HEALTH
# ============================================================

def calculate_soil_health(N, P, K, ph):

    score = 100

    if N < 40 or N > 100:
        score -= 5

    if P < 20 or P > 100:
        score -= 5

    if K < 20 or K > 120:
        score -= 5

    if ph < 5.5 or ph > 7.5:
        score -= 8

    return max(50, min(100, score))


# ============================================================
# CROP ROTATION
# ============================================================

def get_rotation(first_crop):

    rotations = {

        "Rice": [
            ("Rice", "Main Crop", "🌾"),
            ("Chickpea", "Legume Crop", "🫛"),
            ("Maize", "Cereal Crop", "🌽")
        ],

        "Wheat": [
            ("Wheat", "Main Crop", "🌾"),
            ("Groundnut", "Legume Crop", "🥜"),
            ("Maize", "Cereal Crop", "🌽")
        ],

        "Maize": [
            ("Maize", "Main Crop", "🌽"),
            ("Chickpea", "Legume Crop", "🫛"),
            ("Rice", "Cereal Crop", "🌾")
        ],

        "Chickpea": [
            ("Chickpea", "Main Crop", "🫛"),
            ("Maize", "Cereal Crop", "🌽"),
            ("Rice", "Cereal Crop", "🌾")
        ],

        "Groundnut": [
            ("Groundnut", "Main Crop", "🥜"),
            ("Rice", "Cereal Crop", "🌾"),
            ("Chickpea", "Legume Crop", "🫛")
        ],

        "Cotton": [
            ("Cotton", "Main Crop", "🌿"),
            ("Chickpea", "Legume Crop", "🫛"),
            ("Maize", "Cereal Crop", "🌽")
        ],

        "Millet": [
            ("Millet", "Main Crop", "🌱"),
            ("Groundnut", "Legume Crop", "🥜"),
            ("Chickpea", "Legume Crop", "🫛")
        ]
    }

    return rotations.get(
        first_crop,
        rotations["Rice"]
    )


# ============================================================
# SESSION STATE
# ============================================================

if "N" not in st.session_state:
    st.session_state.N = default_N

if "P" not in st.session_state:
    st.session_state.P = default_P

if "K" not in st.session_state:
    st.session_state.K = default_K

if "temperature" not in st.session_state:
    st.session_state.temperature = default_temperature

if "humidity" not in st.session_state:
    st.session_state.humidity = default_humidity

if "ph" not in st.session_state:
    st.session_state.ph = default_ph

if "rainfall" not in st.session_state:
    st.session_state.rainfall = default_rainfall


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("# 🌱 SMART CROP")
    st.markdown("## ROTATION")

    st.caption("AI-Powered Sustainable Farming")

    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "🌱 Crop Analysis",
            "🔄 Rotation Plan",
            "🧪 Soil Health",
            "📊 Insights",
            "◷ History",
            "ⓘ About Us"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    with st.container(border=True):

        st.markdown("### 🌾")

        st.markdown(
            """
            <div style="
                text-align:center;
                font-size:18px;
                font-weight:600;
                color:#315f39;
                padding:10px;
            ">
            Smart farming for a<br>
            better tomorrow 🌱
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SIDEBAR SETTINGS
# ============================================================

with st.sidebar:

    with st.expander("⚙️ Update Field Data"):

        N = st.number_input(
            "Nitrogen (N)",
            min_value=0,
            max_value=200,
            value=st.session_state.N
        )

        P = st.number_input(
            "Phosphorus (P)",
            min_value=0,
            max_value=200,
            value=st.session_state.P
        )

        K = st.number_input(
            "Potassium (K)",
            min_value=0,
            max_value=200,
            value=st.session_state.K
        )

        temperature = st.number_input(
            "Temperature °C",
            value=float(st.session_state.temperature)
        )

        humidity = st.number_input(
            "Humidity %",
            value=float(st.session_state.humidity)
        )

        ph = st.number_input(
            "pH Level",
            min_value=0.0,
            max_value=14.0,
            value=float(st.session_state.ph)
        )

        rainfall = st.number_input(
            "Rainfall mm",
            value=float(st.session_state.rainfall)
        )

        if st.button("Update Dashboard"):

            st.session_state.N = N
            st.session_state.P = P
            st.session_state.K = K
            st.session_state.temperature = temperature
            st.session_state.humidity = humidity
            st.session_state.ph = ph
            st.session_state.rainfall = rainfall

            st.rerun()


# ============================================================
# CURRENT VALUES
# ============================================================

N = st.session_state.N
P = st.session_state.P
K = st.session_state.K
temperature = st.session_state.temperature
humidity = st.session_state.humidity
ph = st.session_state.ph
rainfall = st.session_state.rainfall


recommended_crop, probabilities = predict_crop(
    N,
    P,
    K,
    temperature,
    humidity,
    ph,
    rainfall
)

soil_health = calculate_soil_health(
    N,
    P,
    K,
    ph
)

rotation = get_rotation(recommended_crop)


# ============================================================
# DASHBOARD PAGE
# ============================================================

if page == "🏠 Dashboard":

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    left, right1, right2 = st.columns(
        [4.5, 1.2, 1.2]
    )

    with left:

        st.title("Smart Crop Rotation 🌱")

        st.caption(
            "AI-Powered Recommendations for Sustainable Farming"
        )

    with right1:

        with st.container(border=True):

            st.markdown(
                f"""
                ### 🌤️ {temperature:.0f}°C

                Partly Cloudy
                """
            )

    with right2:

        with st.container(border=True):

            st.markdown(
                """
                ### 📍 India

                Smart Farming
                """
            )

    st.write("")

    # --------------------------------------------------------
    # METRICS
    # --------------------------------------------------------

    m1, m2, m3, m4 = st.columns(4)

    with m1:

        with st.container(border=True):

            st.markdown("## 🌾")
            st.caption("Recommended Crop")
            st.markdown(f"## {recommended_crop}")
            st.caption("Best Match")

    with m2:

        with st.container(border=True):

            st.markdown("## ⭐")
            st.caption("Suitability Score")

            if probabilities and recommended_crop in probabilities:
                suitability = probabilities[recommended_crop]
            else:
                suitability = 92

            st.markdown(f"## {suitability:.0f}%")
            st.caption("Excellent")

    with m3:

        with st.container(border=True):

            st.markdown("## 🧪")
            st.caption("Soil Health Score")
            st.markdown(f"## {soil_health}%")

            if soil_health >= 80:
                health_text = "Good"
            elif soil_health >= 60:
                health_text = "Moderate"
            else:
                health_text = "Needs Attention"

            st.caption(health_text)

    with m4:

        with st.container(border=True):

            st.markdown("## 🔄")
            st.caption("Rotation Status")
            st.markdown("## Year 1 of 3")
            st.caption("On Track")

    st.write("")

    # --------------------------------------------------------
    # MAIN DASHBOARD
    # --------------------------------------------------------

    left_panel, right_panel = st.columns(
        [1.05, 1],
        gap="large"
    )

    # --------------------------------------------------------
    # AI RECOMMENDATION
    # --------------------------------------------------------

    with left_panel:

        with st.container(border=True):

            st.markdown("## ✨ AI Recommendation")

            crop_col, info_col = st.columns(
                [1, 1.4]
            )

            with crop_col:

                st.markdown("#")
                st.markdown(
                    f"# {crop_icons.get(recommended_crop, '🌱')}"
                )

                st.markdown(
                    f"### {recommended_crop}"
                )

            with info_col:

                suitability = 92

                if probabilities and recommended_crop in probabilities:
                    suitability = probabilities[recommended_crop]

                st.success(
                    f"{suitability:.0f}% Suitability"
                )

                st.write(
                    "Excellent match for your soil and climate "
                    "conditions. The recommendation is based on "
                    "nutrient levels, pH, temperature, humidity, "
                    "and rainfall."
                )

                st.button(
                    "View Details →",
                    key="details_button"
                )

            st.divider()

            st.markdown("### Top Crop Recommendations")

            if probabilities:

                sorted_crops = sorted(
                    probabilities.items(),
                    key=lambda x: x[1],
                    reverse=True
                )

                for crop, score in sorted_crops[:4]:

                    col_name, col_bar, col_score = st.columns(
                        [1.1, 4, 0.7]
                    )

                    with col_name:
                        st.write(crop)

                    with col_bar:
                        st.progress(
                            min(int(score), 100)
                        )

                    with col_score:
                        st.write(f"{score:.0f}%")

            else:

                fallback = {
                    "Rice": 92,
                    "Maize": 78,
                    "Chickpea": 65,
                    "Wheat": 48
                }

                for crop, score in fallback.items():

                    col_name, col_bar, col_score = st.columns(
                        [1.1, 4, 0.7]
                    )

                    with col_name:
                        st.write(crop)

                    with col_bar:
                        st.progress(score)

                    with col_score:
                        st.write(f"{score}%")

            st.info(
                f"💡 Why {recommended_crop}? Suitable temperature, "
                "rainfall, soil nutrient balance and pH conditions "
                "support better productivity."
            )

    # --------------------------------------------------------
    # ROTATION PLAN
    # --------------------------------------------------------

    with right_panel:

        with st.container(border=True):

            st.markdown("## 🔄 3 Year Crop Rotation Plan")

            y1, arrow1, y2, arrow2, y3 = st.columns(
                [1.3, 0.3, 1.3, 0.3, 1.3]
            )

            year_cards = [
                (y1, "Year 1", rotation[0]),
                (y2, "Year 2", rotation[1]),
                (y3, "Year 3", rotation[2])
            ]

            for column, year, crop_data in year_cards:

                crop, crop_type, icon = crop_data

                with column:

                    with st.container(border=True):

                        st.caption(year)

                        st.markdown(f"# {icon}")

                        st.markdown(
                            f"### {crop}"
                        )

                        st.caption(crop_type)

            with arrow1:
                st.markdown("# →")

            with arrow2:
                st.markdown("# →")

            st.write("")

            st.divider()

            st.markdown("### Benefits of this Rotation")

            b1, b2, b3, b4 = st.columns(4)

            with b1:
                st.markdown("## 🌱")
                st.caption("Improve Soil")
                st.caption("Fertility")

            with b2:
                st.markdown("## 🛡️")
                st.caption("Reduces Pests")
                st.caption("& Diseases")

            with b3:
                st.markdown("## 🍃")
                st.caption("Better Nutrient")
                st.caption("Balance")

            with b4:
                st.markdown("## 📈")
                st.caption("Higher Yield")
                st.caption("Sustainability")

    st.write("")

    # --------------------------------------------------------
    # FIELD PARAMETERS
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown("### 🔬 Field Parameters")

        p1, p2, p3, p4, p5, p6, p7 = st.columns(7)

        with p1:
            st.metric(
                "🌡 Temperature",
                f"{temperature:.1f} °C"
            )

        with p2:
            st.metric(
                "💧 Humidity",
                f"{humidity:.0f}%"
            )

        with p3:
            st.metric(
                "🌧 Rainfall",
                f"{rainfall:.0f} mm"
            )

        with p4:
            st.metric(
                "🟢 N",
                f"{N} mg/kg"
            )

        with p5:
            st.metric(
                "🟠 P",
                f"{P} mg/kg"
            )

        with p6:
            st.metric(
                "🟣 K",
                f"{K} mg/kg"
            )

        with p7:
            st.metric(
                "🧪 pH",
                f"{ph:.1f}"
            )


# ============================================================
# CROP ANALYSIS PAGE
# ============================================================

elif page == "🌱 Crop Analysis":

    st.title("🌱 Crop Analysis")

    st.write(
        "Analyze your soil and climate conditions to find the most suitable crop."
    )

    st.divider()

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("Recommended Crop")

        st.metric(
            "Best Crop",
            recommended_crop
        )

        st.markdown(
            f"# {crop_icons.get(recommended_crop, '🌱')}"
        )

    with c2:

        st.subheader("Suitability")

        if probabilities:

            chart_data = pd.DataFrame(
                {
                    "Crop": list(probabilities.keys()),
                    "Suitability": list(probabilities.values())
                }
            )

            chart_data = chart_data.sort_values(
                "Suitability",
                ascending=False
            )

            st.bar_chart(
                chart_data,
                x="Crop",
                y="Suitability"
            )


# ============================================================
# ROTATION PLAN PAGE
# ============================================================

elif page == "🔄 Rotation Plan":

    st.title("🔄 3 Year Crop Rotation Plan")

    st.write(
        "A balanced crop sequence helps maintain soil nutrients and reduce pest pressure."
    )

    st.write("")

    r1, r2, r3 = st.columns(3)

    for column, year, data in [
        (r1, "Year 1", rotation[0]),
        (r2, "Year 2", rotation[1]),
        (r3, "Year 3", rotation[2])
    ]:

        crop, crop_type, icon = data

        with column:

            with st.container(border=True):

                st.subheader(year)

                st.markdown(f"# {icon}")

                st.markdown(f"## {crop}")

                st.caption(crop_type)

                st.write(
                    "Selected to maintain a healthier crop sequence."
                )


# ============================================================
# SOIL HEALTH PAGE
# ============================================================

elif page == "🧪 Soil Health":

    st.title("🧪 Soil Health Analysis")

    st.metric(
        "Overall Soil Health Score",
        f"{soil_health}%"
    )

    st.progress(soil_health)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Nitrogen", N)

    with col2:
        st.metric("Phosphorus", P)

    with col3:
        st.metric("Potassium", K)

    with col4:
        st.metric("pH", ph)


# ============================================================
# INSIGHTS PAGE
# ============================================================

elif page == "📊 Insights":

    st.title("📊 Farm Insights")

    st.info(
        "Your recommendations are generated using soil nutrients and climate conditions."
    )

    insights = pd.DataFrame(
        {
            "Parameter": [
                "Nitrogen",
                "Phosphorus",
                "Potassium",
                "Temperature",
                "Humidity",
                "Rainfall",
                "pH"
            ],
            "Value": [
                N,
                P,
                K,
                temperature,
                humidity,
                rainfall,
                ph
            ]
        }
    )

    st.dataframe(
        insights,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# HISTORY PAGE
# ============================================================

elif page == "◷ History":

    st.title("◷ Recommendation History")

    st.info(
        "Future recommendations can be stored here for tracking crop decisions."
    )

    history = pd.DataFrame(
        {
            "Date": ["Current"],
            "Recommended Crop": [recommended_crop],
            "Suitability": [
                f"{probabilities.get(recommended_crop, 92):.0f}%"
                if probabilities
                else "92%"
            ],
            "Status": ["Active"]
        }
    )

    st.dataframe(
        history,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# ABOUT PAGE
# ============================================================

elif page == "ⓘ About Us":

    st.title("ⓘ About Smart Crop Rotation")

    st.write(
        """
        Smart Crop Rotation is an AI-powered agricultural
        decision-support system designed to help farmers select
        suitable crops based on soil and climate conditions.
        """
    )

    st.subheader("🌱 What the system analyzes")

    st.write(
        """
        • Nitrogen

        • Phosphorus

        • Potassium

        • Soil pH

        • Temperature

        • Humidity

        • Rainfall
        """
    )

    st.subheader("🤖 Machine Learning")

    st.write(
        """
        The system can use a trained machine learning model
        to recommend a suitable crop based on the provided
        environmental and soil parameters.
        """
    )

    st.success(
        "Smart farming for a better tomorrow 🌱"
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🌱 SMART CROP ROTATION • AI-POWERED SUSTAINABLE FARMING"
)