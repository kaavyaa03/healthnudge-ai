# src/genai.py

def answer_follow_up(question, flags):
    q = question.lower().strip() if question else ""

    # Keyword + flag-based explanation
    faq = {
        "smoking": "Smoking is linked to increased risks of lung cancer, heart disease, and stroke.",
        "alcohol": "Alcohol consumption affects the liver and can lead to dependence or hypertension.",
        "low_sleep": "Lack of sleep impairs focus, weakens the immune system, and increases stress levels.",
        "no_exercise": "Physical inactivity raises the risk of obesity, diabetes, and heart issues.",
        "junk_food": "Processed foods are often high in fat, salt, and sugar — leading to chronic health problems."
    }

    if "why is this risky" in q or "why risky" in q:
        if flags:
            reasons = [faq[flag] for flag in flags if flag in faq]
            return " ".join(reasons) if reasons else "This behavior may pose significant health risks."
        return "The detected lifestyle behaviors can contribute to long-term health issues."

    for key in faq:
        if key in q:
            return faq[key]

    return "Health risks vary by individual. Please consult a doctor for personalized guidance."


def generate_recommendation(risk_level, flags, symptoms, question=None):
    recommendations = []

    # Flag-specific advice
    flag_advice = {
        "smoking": "Consider quitting smoking. It significantly increases your risk of respiratory and cardiovascular diseases.",
        "alcohol": "Reduce alcohol intake. Excessive drinking can harm your liver and mental health.",
        "low_sleep": "Aim to get at least 7 hours of sleep each night to support brain and body function.",
        "no_exercise": "Start incorporating at least 30 minutes of physical activity into your daily routine.",
        "junk_food": "Reduce intake of fast food. Opt for fresh fruits, vegetables, and whole grains."
    }

    for flag in flags:
        if flag in flag_advice:
            recommendations.append(flag_advice[flag])

    # Risk-level context
    if risk_level == "High":
        recommendations.append("Your overall health risk is high. We strongly advise you to consult a healthcare provider soon.")
    elif risk_level == "Medium":
        recommendations.append("You're at moderate risk. Making small but consistent improvements can lower your health risks.")
    else:
        recommendations.append("Your current health status is low risk. Maintain your healthy habits!")

    # Symptom-based general tips
    if any(symptom in ["fatigue", "dizzy", "headache", "sweat"] for symptom in symptoms):
        recommendations.append("Persistent physical symptoms may indicate underlying issues. Please consider a clinical check-up.")

    follow_up_answer = answer_follow_up(question, flags)

    return {
        "recommendations": recommendations,
        "follow_up_answer": follow_up_answer
    }

# test block only
if __name__ == "__main__":
    flags = ["smoking", "low_sleep"]
    symptoms = ["dizzy", "fatigue"]
    risk_level = "High"
    question = "Why is this risky?"

    result = generate_recommendation(risk_level, flags, symptoms, question)
    for line in result["recommendations"]:
        print("", line)
    print("Follow-up Answer:", result["follow_up_answer"])