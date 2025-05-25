import json
import os
from sklearn.model_selection import train_test_split

# Paths
clinical_input = "data/cleaned_clinical_notes.json"
pubmed_input = "data/cleaned_pubmedqa.json"

clinical_out_dir = "data/split_clinical_notes"
pubmed_out_dir = "data/split_pubmedqa"
os.makedirs(clinical_out_dir, exist_ok=True)
os.makedirs(pubmed_out_dir, exist_ok=True)

def split_and_save(data, out_dir, name):
    train, temp = train_test_split(data, test_size=0.2, random_state=42)
    val, test = train_test_split(temp, test_size=0.5, random_state=42)

    with open(f"{out_dir}/train.json", "w") as f:
        json.dump(train, f, indent=2)
    with open(f"{out_dir}/val.json", "w") as f:
        json.dump(val, f, indent=2)
    with open(f"{out_dir}/test.json", "w") as f:
        json.dump(test, f, indent=2)

    print(f"{name} split into train ({len(train)}), val ({len(val)}), test ({len(test)})")

# Load JSON
with open(clinical_input) as f:
    clinical_data = json.load(f)
with open(pubmed_input) as f:
    pubmed_data = json.load(f)

# Split and save
split_and_save(clinical_data, clinical_out_dir, "Clinical Notes")
split_and_save(pubmed_data, pubmed_out_dir, "PubMedQA")