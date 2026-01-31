def generate_advice(problem_type, details=None):
    """
    Central advisory engine used by:
    - Text frontend
    - Image frontend
    - Future IVR system
    """

    if problem_type == "disease":
        return {
            "issue": "Crop disease symptoms detected",
            "cause": (
                "This is likely caused by fungal or bacterial infection. "
                "High humidity, poor air circulation, or infected soil can increase risk."
            ),
            "severity": "high",
            "immediate_action": (
                "Remove and destroy infected plant parts immediately to prevent spread."
            ),
            "organic_treatments": [
                "Spray neem oil once every 7 days",
                "Apply baking soda solution (1 tbsp per liter)",
                "Use copper-based organic fungicide"
            ],
            "chemical_treatments": [
                "Apply recommended fungicide as per local agricultural guidelines",
                "Avoid overuse of chemicals to prevent resistance"
            ],
            "prevention_tips": [
                "Ensure proper spacing between plants",
                "Avoid overhead irrigation",
                "Practice crop rotation",
                "Use disease-resistant seed varieties"
            ]
        }

    elif problem_type == "pest":
        return {
            "issue": "Pest infestation detected",
            "cause": (
                "Insects such as aphids or caterpillars are feeding on plant sap or leaves. "
                "This often happens during warm and humid conditions."
            ),
            "severity": "medium",
            "organic_treatments": [
                "Spray neem oil or soap-water solution",
                "Introduce natural predators like ladybugs",
                "Use garlic-chili spray"
            ],
            "chemical_treatments": [
                "Use insecticidal soap",
                "Apply approved pesticides only if infestation is severe"
            ],
            "prevention_tips": [
                "Inspect crops regularly",
                "Remove weeds near crop area",
                "Encourage beneficial insects",
                "Maintain field hygiene"
            ]
        }

    elif problem_type == "irrigation":
        return {
            "issue": "Irrigation stress detected",
            "cause": (
                "Overwatering or underwatering can stress plant roots, "
                "leading to poor nutrient absorption."
            ),
            "severity": "low",
            "organic_treatments": [
                "Use mulching to retain soil moisture",
                "Improve soil drainage naturally"
            ],
            "chemical_treatments": [
                "No chemical treatment required"
            ],
            "prevention_tips": [
                "Check soil moisture before watering",
                "Water crops early morning or evening",
                "Avoid water stagnation near roots"
            ]
        }

    else:
        return {
            "issue": "Unable to clearly identify the problem",
            "cause": (
                "The input provided is insufficient or unclear for accurate diagnosis."
            ),
            "severity": "low",
            "organic_treatments": [
                "Provide more detailed description",
                "Upload a clearer image of the affected crop"
            ],
            "chemical_treatments": [
                "Not applicable"
            ],
            "prevention_tips": [
                "Monitor crop condition regularly",
                "Seek expert advice if problem persists"
            ]
        }
