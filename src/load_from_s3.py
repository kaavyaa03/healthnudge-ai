# src/load_from_s3.py

from datasets import load_from_disk

# S3 paths to each dataset folder
clinical_path = "s3://healthnudge-datasets/clinical_notes_raw"
pubmed_path = "s3://healthnudge-datasets/pubmedqa_raw"

# Load them using Hugging Face Datasets
clinical_dataset = load_from_disk(clinical_path)
pubmed_dataset = load_from_disk(pubmed_path)

# Show samples
print("📄 Clinical Notes Sample:")
print(clinical_dataset["train"][0])

print("\n📚 PubMedQA Sample:")
print(pubmed_dataset["train"][0])