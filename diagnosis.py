def diagnose_issue(symptoms):
    rules = {
        "engine_misfire": {
            "issue": "Faulty spark plugs",
            "solution": "Inspect and replace spark plugs",
            "confidence": 85
        },
        "overheating": {
            "issue": "Coolant leak or bad thermostat",
            "solution": "Check coolant level and thermostat",
            "confidence": 80
        },
        "battery_dead": {
            "issue": "Weak or dying battery",
            "solution": "Test battery voltage and replace if needed",
            "confidence": 90
        }
    }

    for symptom in symptoms:
        if symptom in rules:
            return rules[symptom]

    return {
        "issue": "Unknown issue",
        "solution": "Further diagnostics required",
        "confidence": 40
    }
