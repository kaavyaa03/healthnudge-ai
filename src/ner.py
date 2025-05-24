# src/ner.py

import re
import spacy

# Load both general spaCy and biomedical scispaCy
nlp_general = spacy.load("en_core_web_sm")
nlp_medical = spacy.load("en_core_sci_sm")

# Rule-based lifestyle flags
LIFESTYLE_RULES = {
    "smoking": r"\b(smoke|cigarette|tobacco|nicotine)\b",
    "alcohol": r"\b(drink|alcohol|wine|beer|vodka)\b",
    "low_sleep": r"\b(sleep.*(2|3|4|5) hours?|insomnia|poor sleep|restless)\b",
    "no_exercise": r"\b(inactive|no exercise|sedentary|lazy|never workout)\b",
    "junk_food": r"\b(junk food|fries|chips|pizza|burger|soda|fast food)\b"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def extract_lifestyle_flags(text):
    flags = []
    for label, pattern in LIFESTYLE_RULES.items():
        if re.search(pattern, text, re.IGNORECASE):
            flags.append(label)
    return flags

def extract_medical_entities(text):
    doc = nlp_medical(text)
    return list(set(ent.text.strip() for ent in doc.ents if len(ent.text.strip()) > 2))

def extract_named_entities(text):
    doc = nlp_general(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

def analyze_text(text, question=None):
    cleaned = clean_text(text)
    lifestyle_flags = extract_lifestyle_flags(cleaned)
    symptoms = extract_medical_entities(cleaned)
    named_entities = extract_named_entities(text)

    return {
        "original_text": text,
        "cleaned_text": cleaned,
        "lifestyle_flags": lifestyle_flags,
        "symptoms_detected": symptoms,
        "named_entities": named_entities,
        "follow_up_question": question or ""
    }

# Example usage
if __name__ == "__main__":
    input_text = "I feel dizzy and my hands sweat whenever I go out in the sun. I’ve been drinking wine lately and not working out at all."
    question = "Why is this risky?"
    result = analyze_text(input_text, question)
    print(result)