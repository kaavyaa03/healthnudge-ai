from transformers import T5Tokenizer, T5ForConditionalGeneration
import json
from tqdm import tqdm

# Load fine-tuned model
model_path = "genai_finetuned_t5/t5_pubmedqa_finetuned"
model = T5ForConditionalGeneration.from_pretrained(model_path)
tokenizer = T5Tokenizer.from_pretrained(model_path)

# Load test set
with open("data/split_pubmedqa/test.json", "r", encoding="utf-8") as f:
    test_data = json.load(f)

# Inference loop
results = []
model.eval()

for example in tqdm(test_data):
    prompt = f"Context: {example['context']}\nQuestion: {example['question']}"
    input_ids = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True).input_ids
    output = model.generate(input_ids, max_new_tokens=60)
    decoded = tokenizer.decode(output[0], skip_special_tokens=True)

    results.append({
        "prompt": prompt,
        "expected_response": example["answer"],
        "generated_response": decoded
    })

# Save predictions
with open("genai_finetuned_t5/local_predictions.jsonl", "w", encoding="utf-8") as f:
    for r in results:
        f.write(json.dumps(r) + "\n")

print("Inference completed and saved to local_predictions.jsonl")