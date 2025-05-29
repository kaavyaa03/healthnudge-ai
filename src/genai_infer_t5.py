import json
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
from tqdm import tqdm

# Paths
input_path = "data/pubmedqa_prompts.jsonl"
output_path = "data/pubmedqa_predictions_t5.jsonl"

# Load model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Load prompts
prompts = []
with open(input_path, "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)
        prompts.append(item)

# Inference
results = []
print(f"Running inference on {len(prompts)} prompts...")
for item in tqdm(prompts):
    input_text = item["prompt"]
    inputs = tokenizer.encode(input_text, return_tensors="pt", truncation=True, max_length=512).to(device)

    with torch.no_grad():
        outputs = model.generate(inputs, max_length=100, num_beams=2, early_stopping=True)

    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    results.append({
        "prompt": item["prompt"],
        "expected_response": item["response"],
        "generated_response": prediction
    })

# Save predictions
with open(output_path, "w", encoding="utf-8") as f:
    for item in results:
        f.write(json.dumps(item) + "\n")

print(f"Inference complete. Results saved to {output_path}")