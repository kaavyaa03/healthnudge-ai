# src/prepare_prompt_dataset.py

import json
from pathlib import Path
from datasets import load_dataset

# Load the training split from split_pubmedqa folder
pubmedqa = load_dataset("json", data_files="data/split_pubmedqa/train.json")

# Format as prompt-response pairs
formatted = []
for example in pubmedqa["train"]:
    prompt = f"Context: {example['context']}\nQuestion: {example['question']}"
    answer = example["answer"]
    formatted.append({
        "prompt": prompt,
        "response": answer
    })

# Save to JSONL
Path("data").mkdir(exist_ok=True)
with open("data/pubmedqa_formatted_prompts.jsonl", "w", encoding="utf-8") as f:
    for item in formatted:
        f.write(json.dumps(item) + "\n")

print("Prompt-format dataset saved to: data/pubmedqa_formatted_prompts.jsonl")