# src/pipeline.py

import sys
import os
sys.path.append(os.path.abspath("src"))

from ner import analyze_text
from classifier import assess_risk

def run_pipeline(text, question=None):
    ner_result = analyze_text(text, question)
    risk_result = assess_risk(
        ner_result["lifestyle_flags"],
        ner_result["symptoms_detected"]
    )

    return {
        "original_text": ner_result["original_text"],
        "cleaned_text": ner_result["cleaned_text"],
        "lifestyle_flags": ner_result["lifestyle_flags"],
        "symptoms_detected": ner_result["symptoms_detected"],
        "risk_score": risk_result["risk_score"],
        "risk_level": risk_result["risk_level"],
        "follow_up_question": ner_result["follow_up_question"]
    }

# Example usage
if __name__ == "__main__":
    text = "I smoke daily, drink alcohol and barely sleep 4 hours. I feel dizzy and tired all the time."
    question = "Why is this considered risky?"
    output = run_pipeline(text, question)
    print(output)