import json

input_path = "data/pubmedqa_prompts.jsonl"

def preview_prompts(n=5):
    print(f"Previewing {n} prompt-response pairs from PubMedQA...")
    with open(input_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            item = json.loads(line)
            print(f"\n--- Example {i+1} ---")
            print("Prompt:\n", item["prompt"])
            print("Response:\n", item["response"])
            if i + 1 == n:
                break

if __name__ == "__main__":
    preview_prompts(5)