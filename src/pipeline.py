# src/pipeline.py

import sys
import os
sys.path.append(os.path.abspath("src"))

from ner import analyze_text
from classifier import assess_risk
from genai import generate_recommendation

def run_pipeline(text, question=None):
    ner_result = analyze_text(text, question)
    risk_result = assess_risk(
        ner_result["lifestyle_flags"],
        ner_result["symptoms_detected"]
    )

    recommendation_result = generate_recommendation(
        risk_result["risk_level"],
        ner_result["lifestyle_flags"],
        ner_result["symptoms_detected"],
        ner_result.get("follow_up_question")
    )

    return {
        "original_text": ner_result["original_text"],
        "cleaned_text": ner_result["cleaned_text"],
        "lifestyle_flags": ner_result["lifestyle_flags"],
        "symptoms_detected": ner_result["symptoms_detected"],
        "risk_score": risk_result["risk_score"],
        "risk_level": risk_result["risk_level"],
        "recommendations": recommendation_result["recommendations"],
        "follow_up_answer": recommendation_result["follow_up_answer"]
    }

# Example usage
if __name__ == "__main__":
    text = "I smoke daily, drink alcohol and barely sleep 4 hours. I feel dizzy and tired all the time."
    question = "Why is this considered risky?"
    output = run_pipeline(text, question)

    print("\nOriginal Text:", output["original_text"])
    print("Cleaned Text:", output["cleaned_text"])

    print("\nLifestyle Flags:")
    for flag in output["lifestyle_flags"]:
        print(" -", flag)

    print("\nSymptoms Detected:")
    for s in output["symptoms_detected"]:
        print(" -", s)

    print("\nRisk Score:", output["risk_score"])
    print("Risk Level:", output["risk_level"])

    print("\nRecommendations:")
    for r in output["recommendations"]:
        print(" -", r)

    print("\nFollow-Up Question:", question)
    print("Follow-Up Answer:", output["follow_up_answer"])