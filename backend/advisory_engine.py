def generate_advice(problem_type, details=None):

    if problem_type == "disease":
        return {
            "issue": "Crop disease symptoms detected",
            "cause": "This may be due to fungal or bacterial infection affecting the crop leaves.",
            "advice": [
                "Remove infected leaves immediately",
                "Avoid watering leaves directly",
                "Spray neem oil or recommended fungicide every 7 days"
            ]
        }

    elif problem_type == "pest":
        return {
            "issue": "Pest infestation detected",
            "cause": "Insects may be feeding on the crop leaves or stems.",
            "advice": [
                "Inspect the underside of leaves regularly",
                "Use neem-based organic pesticide",
                "Maintain field hygiene and remove weeds"
            ]
        }

    elif problem_type == "irrigation":
        return {
            "issue": "Irrigation-related stress detected",
            "cause": "Overwatering or underwatering may be affecting crop health.",
            "advice": [
                "Check soil moisture before watering",
                "Avoid water stagnation around roots",
                "Water crops early morning or evening"
            ]
        }

    else:
        return {
            "issue": "Unable to clearly identify the problem",
            "cause": "The provided input is insufficient or unclear for accurate analysis.",
            "advice": [
                "Please provide more details about the problem",
                "Upload a clearer image of the affected crop"
            ]
        }
