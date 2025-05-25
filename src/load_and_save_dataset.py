# src/load_and_save_dataset.py

from datasets import load_dataset

print("Downloading datasets from Hugging Face...")

# Load datasets from Hugging Face
clinical = load_dataset("meowterspace42/clinical_notes")
pubmed = load_dataset("qiaojin/PubMedQA", "pqa_labeled")

# Save locally under data/
print("Saving datasets to local disk...")
clinical.save_to_disk("data/clinical_notes_raw")
pubmed.save_to_disk("data/pubmedqa_raw")

print("Datasets saved successfully to /data folder.")

# Inspect structure
print("\n🧠 Clinical Notes Keys:", clinical_dataset["train"].features.keys())
print("🧠 PubMedQA Keys:", pubmed_dataset["train"].features.keys())

# Show a few entries
print("\n🔍 Clinical Notes Text Sample:\n", clinical_dataset["train"][1])
print("\n🔍 PubMedQA Entry:\n", pubmed_dataset["train"][1])