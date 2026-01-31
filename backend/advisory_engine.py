def generate_advice(problem_type, details=None):
    """
    Common advisory engine
    Used by BOTH Streamlit app and IVR
    """

    if problem_type == "disease":
        return {
            "issue": "Possible crop disease detected",
            "advice": [
                "Remove affected leaves",
                "Avoid overwatering",
                "Spray neem oil once every 7 days"
            ]
        }

    elif problem_type == "pest":
        return {
            "issue": "Possible pest infestation",
            "advice": [
                "Inspect leaves regularly",
                "Use organic pesticide if available",
                "Maintain field hygiene"
            ]
        }

    elif problem_type == "irrigation":
        return {
            "issue": "Irrigation-related issue",
            "advice": [
                "Avoid water stagnation",
                "Water crops early morning or evening",
                "Check soil moisture before watering"
            ]
        }

    else:
        return {
            "issue": "Unable to identify the issue clearly",
            "advice": [
                "Please provide more details",
                "Upload a clearer image if possible"
            ]
        }
