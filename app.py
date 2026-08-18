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
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Playfair+Display:ital,wght@0,500;1,500&display=swap');

    /* ---------- PAGE ---------- */

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

    /* ---------- REMOVE STREAMLIT EXTRA SPACE ---------- */

    .element-container {
        margin-bottom: 0 !important;
    }

    /* ---------- HERO ---------- */

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

    /* ---------- DECORATIVE LINES ---------- */

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

    .hero-lines .line:nth-child(1) {
        right: 0;
    }

    .hero-lines .line:nth-child(2) {
        right: 90px;
    }

    .hero-lines .line:nth-child(3) {
        right: 180px;
    }

    .hero-lines .line:nth-child(4) {
        right: 270px;
    }

    .hero-lines .line:nth-child(5) {
        right: 360px;
    }

    /* ---------- SECTION ---------- */

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

    /* ---------- FORM CARD ---------- */

    .form-card {
        background: #fbfaf4;
        border: 1px solid #d6d8c7;
        border-radius: 20px;
        padding: 35px;
        box-sizing: border-box;
    }

    /* ---------- STREAMLIT LABELS ---------- */

    label {
        font-family: "DM Mono", monospace !important;
        font-size: 12px !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: #315f39 !important;
    }

    /* ---------- SELECT ---------- */

    div[data-baseweb="select"] > div {
        background: #f2f3f5 !important;
        border: 1px solid transparent !important;
        border-radius: 9px !important;
        min-height: 50px !important;
    }

    div[data-baseweb="select"] > div:hover {
        border: 1px solid #3e7746 !important;
    }

    /* ---------- NUMBER INPUT ---------- */

    div[data-baseweb="input"] > div {
        background: #f2f3f5 !important;
        border: 1px solid transparent !important;
        border-radius: 9px !important;
        min-height: 50px !important;
    }

    div[data-baseweb="input"] > div:hover {
        border: 1px solid #3e7746 !important;
    }

    /* ---------- BUTTON ---------- */

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

    /* ---------- CAPTION ---------- */

    .stCaption {
        color: #687064 !important;
    }

    /* ---------- EXPANDER ---------- */

    div[data-testid="stExpander"] {
        border: 1px solid #cfd2c1 !important;
        border-radius: 10px !important;
        background: transparent !important;
    }

    /* ---------- RESULT CARDS ---------- */

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

    /* ---------- ROTATION ---------- */

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

    /* ---------- FOOTER ---------- */

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

    /* ---------- MOBILE ---------- */

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

        .form-card {
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
    """
    <section class="hero-wrapper">

        <div class="hero-content">

            <div class="eyebrow">
                — Soil-first planning
            </div>

            <h1 class="hero-title">
                Grow what your
                <em>ground</em>
                is telling
                you.
            </h1>

            <div class="hero-description">
                Tell SmartCrop your soil, water, and climate —
                it scores crops against those conditions instead
                of habit, and lays out a rotation that helps keep
                the field's nutrients in balance across seasons.
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
# FIELD CONDITIONS TITLE
# ============================================================

st.html(
    """
    <div class="section-wrapper">

        <div class="section-heading">

            <h2>Field conditions</h2>

            <span class="section-number">
                01 — inputs
            </span>

        </div>

    </div>
    """
)


# ============================================================
# FORM CARD START
# ============================================================

st.markdown(
    """
    <style>
    .input-area {
        margin-left: 8%;
        margin-right: 8%;
        background: #fbfaf4;
        border: 1px solid #d6d8c7;
        border-radius: 20px;
        padding: 35px;
        margin-bottom: 20px;
    }
    </style>

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
        "Soil type",
        [
            "Loamy",
            "Clay",
            "Sandy",
            "Silty",
            "Black soil",
            "Red soil"
        ]
    )


with col2:

    soil_ph = st.number_input(
        "Soil pH",
        min_value=3.0,
        max_value=10.0,
        value=6.5,
        step=0.1,
        format="%.2f"
    )


with col3:

    water = st.selectbox(
        "Water availability",
        [
            "Rainfed (low)",
            "Partial irrigation (medium)",
            "Good irrigation (high)"
        ]
    )


# ============================================================
# SECOND ROW
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:

    climate = st.selectbox(
        "Climate zone",
        [
            "Semi-arid",
            "Tropical",
            "Sub-tropical",
            "Temperate",
            "Arid"
        ]
    )


with col2:

    season = st.selectbox(
        "Starting season",
        [
            "Kharif (monsoon, Jun–Oct)",
            "Rabi (winter, Nov–Mar)",
            "Zaid (summer, Mar–Jun)"
        ]
    )


with col3:

    rotation_length = st.selectbox(
        "Rotation length",
        [
            "3 seasons",
            "4 seasons",
            "6 seasons"
        ]
    )


# ============================================================
# LAST CROP
# ============================================================

last_crop = st.selectbox(
    "Last crop grown here (optional)",
    [
        "None / left fallow",
        "Rice",
        "Wheat",
        "Maize",
        "Cotton",
        "Groundnut",
        "Chickpea",
        "Millet"
    ]
)

st.caption(
    "Used to avoid repeating the same crop family "
    "and to plan nutrient recovery."
)


# ============================================================
# ADVANCED DATA
# ============================================================

with st.expander("Advanced soil & climate data"):

    col1, col2, col3 = st.columns(3)

    with col1:

        nitrogen = st.number_input(
            "Nitrogen (N)",
            min_value=0.0,
            max_value=200.0,
            value=60.0
        )

    with col2:

        phosphorus = st.number_input(
            "Phosphorus (P)",
            min_value=0.0,
            max_value=200.0,
            value=40.0
        )

    with col3:

        potassium = st.number_input(
            "Potassium (K)",
            min_value=0.0,
            max_value=200.0,
            value=40.0
        )


    col1, col2, col3 = st.columns(3)

    with col1:

        rainfall = st.number_input(
            "Annual rainfall (mm)",
            min_value=100.0,
            max_value=5000.0,
            value=700.0
        )

    with col2:

        temperature = st.number_input(
            "Average temperature (°C)",
            min_value=5.0,
            max_value=45.0,
            value=26.0
        )

    with col3:

        organic_matter = st.number_input(
            "Organic matter (%)",
            min_value=0.0,
            max_value=20.0,
            value=1.5
        )


# ============================================================
# BUTTON
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

button_col1, button_col2 = st.columns([3, 1])

with button_col2:

    calculate = st.button(
        "Chart my rotation →",
        use_container_width=True
    )


# ============================================================
# CLOSE FORM CARD
# ============================================================

st.markdown(
    """
    </div>
    """,
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

    # --------------------------------------------------------
    # SOIL
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # PH
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # WATER
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # CLIMATE
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # SEASON
    # --------------------------------------------------------

    if "Kharif" in season:

        scores["Rice"] += 8
        scores["Maize"] += 8
        scores["Cotton"] += 8
        scores["Groundnut"] += 8
        scores["Millet"] += 8

    elif "Rabi" in season:

        scores["Wheat"] += 12
        scores["Chickpea"] += 12

    elif "Zaid" in season:

        scores["Maize"] += 8
        scores["Groundnut"] += 8
        scores["Millet"] += 6

    # --------------------------------------------------------
    # NITROGEN
    # --------------------------------------------------------

    if nitrogen < 40:

        scores["Chickpea"] += 12
        scores["Groundnut"] += 10

    elif nitrogen > 100:

        scores["Maize"] += 8
        scores["Rice"] += 7

    # --------------------------------------------------------
    # RAINFALL
    # --------------------------------------------------------

    if rainfall < 500:

        scores["Millet"] += 10
        scores["Chickpea"] += 8
        scores["Rice"] -= 15

    elif rainfall > 1200:

        scores["Rice"] += 12
        scores["Maize"] += 5

    # --------------------------------------------------------
    # TEMPERATURE
    # --------------------------------------------------------

    if temperature > 28:

        scores["Millet"] += 7
        scores["Cotton"] += 7
        scores["Rice"] += 5

    if temperature < 20:

        scores["Wheat"] += 10
        scores["Chickpea"] += 8

    # --------------------------------------------------------
    # LAST CROP
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # LIMIT
    # --------------------------------------------------------

    for crop in scores:

        scores[crop] = max(
            0,
            min(99, scores[crop])
        )

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
    season,
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

    # If needed repeat lower-ranked crops
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
    )

    rotation = create_rotation(
        recommendations,
        season,
        rotation_length,
        last_crop
    )

    # ========================================================
    # RESULTS HEADER
    # ========================================================

    st.html(
        """
        <div class="section-wrapper">

            <div class="section-heading">

                <h2>Your crop plan</h2>

                <span class="section-number">
                    02 — recommendations
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

        with cols[i]:

            st.html(
                f"""
                <div class="result-card">

                    <div class="result-number">
                        Recommendation {i + 1}
                    </div>

                    <div class="result-crop">
                        {crop}
                    </div>

                    <div class="result-score">
                        Field fit score:
                        <strong>{score}%</strong>
                    </div>

                </div>
                """
            )

    # ========================================================
    # ROTATION
    # ========================================================

    st.html(
        """
        <div class="section-wrapper">

            <div class="section-heading">

                <h2>Suggested rotation</h2>

                <span class="section-number">
                    03 — seasons
                </span>

            </div>

        </div>
        """
    )

    # ========================================================
    # ROTATION CARDS
    # ========================================================

    season_names = [
        "Season 01",
        "Season 02",
        "Season 03",
        "Season 04",
        "Season 05",
        "Season 06"
    ]

    for i, crop in enumerate(rotation):

        if i == 0:

            reason = (
                "Best immediate match for your current "
                "soil, climate and water conditions."
            )

        elif crop in ["Chickpea", "Groundnut"]:

            reason = (
                "Legume rotation helps diversify the field "
                "and supports nutrient recovery."
            )

        elif crop in ["Millet"]:

            reason = (
                "A lower-water crop that can improve rotation "
                "diversity under semi-arid conditions."
            )

        else:

            reason = (
                "Provides crop-family diversity and avoids "
                "repeating the same crop continuously."
            )

        st.html(
            f"""
            <div class="section-wrapper"
                 style="padding-top: 0; padding-bottom: 15px;">

                <div class="rotation-card">

                    <div class="rotation-season">
                        {season_names[i]}
                    </div>

                    <div class="rotation-crop">
                        {crop}
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
    """
    <div class="footer">

        SMARTCROP
        &nbsp;·&nbsp;
        SOIL-FIRST CROP PLANNING
        &nbsp;·&nbsp;
        ML-ASSISTED DECISION SUPPORT

    </div>
    """
)