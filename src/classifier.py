# src/classifier.py

def compute_risk_score(flags, symptoms):
    """
    Assign a numeric risk score based on weighted flags and symptoms.
    You can later replace this logic with a trained LightGBM model.
    """
    score = 0

    # Risk scoring rules
    risk_weights = {
        "smoking": 3,
        "alcohol": 2,
        "low_sleep": 2,
        "no_exercise": 2,
        "junk_food": 1
    }

    for flag in flags:
        score += risk_weights.get(flag, 0)

    score += len(symptoms) * 1.5  # Each symptom adds weight

    return score

def classify_risk_level(score):
    """
    Convert numeric score into categorical risk level
    """
    if score >= 7:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"

def assess_risk(lifestyle_flags, symptoms_detected):
    """
    Public function to be called from main pipeline.
    """
    score = compute_risk_score(lifestyle_flags, symptoms_detected)
    risk = classify_risk_level(score)
    return {
        "risk_score": score,
        "risk_level": risk
    }

# Example usage
if __name__ == "__main__":
    flags = ["smoking", "alcohol", "low_sleep"]
    symptoms = ["dizzy", "sweating", "tired"]
    result = assess_risk(flags, symptoms)
    print(result)