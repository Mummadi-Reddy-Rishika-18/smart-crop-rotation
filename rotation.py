ROTATION_RULES = {
    "rice": [
        "groundnut",
        "chickpea",
        "green gram",
    ],
    "maize": [
        "groundnut",
        "chickpea",
        "millet",
    ],
    "cotton": [
        "chickpea",
        "groundnut",
        "millet",
    ],
    "groundnut": [
        "maize",
        "millet",
        "wheat",
    ],
    "wheat": [
        "chickpea",
        "groundnut",
        "maize",
    ],
    "chickpea": [
        "maize",
        "millet",
        "rice",
    ],
    "millet": [
        "groundnut",
        "chickpea",
        "wheat",
    ],
}


CROP_TYPES = {
    "rice": "cereal",
    "maize": "cereal",
    "wheat": "cereal",
    "millet": "cereal",
    "cotton": "cash crop",
    "groundnut": "legume",
    "chickpea": "legume",
}


def get_rotation_options(current_crop):
    current_crop = current_crop.lower().strip()

    return ROTATION_RULES.get(
        current_crop,
        ["groundnut", "chickpea", "millet"],
    )


def get_crop_type(crop):
    return CROP_TYPES.get(crop.lower(), "unknown")


def calculate_rotation_score(previous_crop, recommended_crop):
    previous_crop = previous_crop.lower().strip()
    recommended_crop = recommended_crop.lower().strip()

    if previous_crop == recommended_crop:
        return 40

    previous_type = get_crop_type(previous_crop)
    recommended_type = get_crop_type(recommended_crop)

    if previous_type == "cereal" and recommended_type == "legume":
        return 95

    if previous_type == "legume" and recommended_type == "cereal":
        return 90

    if previous_type == recommended_type:
        return 65

    return 80


def generate_rotation_plan(first_crop):
    first_crop = first_crop.lower().strip()

    options = get_rotation_options(first_crop)

    plan = [
        first_crop,
        options[0],
        options[1],
    ]

    return plan