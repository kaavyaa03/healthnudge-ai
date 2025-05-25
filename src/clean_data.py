import os
from datasets import load_from_disk
import json
import re

# S3 paths
clinical_path = "s3://healthnudge-datasets/clinical_notes_raw"
pubmed_path = "s3://healthnudge-datasets/pubmedqa_raw"

# Create output dir
os.makedirs("data", exist_ok=True)

def clean_text(text):
    # Basic text normalization
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\\n", " ", text)
    return text.strip()

def clean_clinical_notes():
    print("Cleaning Clinical Notes...")
    clinical_dataset = load_from_disk(clinical_path)
    samples = clinical_dataset["train"]
    
    cleaned = [clean_text(sample["text"]) for sample in samples]

    with open("data/cleaned_clinical_notes.json", "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2)

    print(f"Saved {len(cleaned)} cleaned clinical notes.")


def clean_pubmedqa():
    print("Cleaning PubMedQA...")
    pubmed_dataset = load_from_disk(pubmed_path)
    samples = pubmed_dataset["train"]
    
    cleaned = []
    for sample in samples:
        q = clean_text(sample.get("question", ""))
        contexts = sample.get("context", {}).get("contexts", [])
        context = clean_text(" ".join(contexts)) if isinstance(contexts, list) else clean_text(contexts)
        ans = clean_text(sample.get("long_answer", ""))
        
        if q and context and ans:
            cleaned.append({
                "question": q,
                "context": context,
                "answer": ans
            })

    with open("data/cleaned_pubmedqa.json", "w", encoding="utf-8") as f:
        json.dump(cleaned, f, indent=2)

    print(f"Saved {len(cleaned)} cleaned PubMedQA examples.")


if __name__ == "__main__":
    clean_clinical_notes()
    clean_pubmedqa()