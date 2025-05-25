import json
import os

# Paths
input_path = "data/cleaned_pubmedqa.json"
output_path = "data/pubmedqa_prompts.jsonl"
os.makedirs("data", exist_ok=True)

def format_pubmedqa_for_prompt():
    with open(input_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    with open(output_path, "w", encoding="utf-8") as out_f:
        for entry in raw_data:
            prompt = f"Context: {entry['context']}\n\nQuestion: {entry['question']}"
            response = entry["answer"]

            out = {
                "prompt": prompt.strip(),
                "response": response.strip()
            }
            out_f.write(json.dumps(out) + "\n")

    print(f"{len(raw_data)} PubMedQA prompts saved to {output_path}")

if __name__ == "__main__":
    format_pubmedqa_for_prompt()