# src/genai_infer_mistral.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json
from tqdm import tqdm
from pathlib import Path

# Load prompts
with open("data/pubmedqa_formatted_prompts.jsonl", "r", encoding="utf-8") as f:
    prompts = [json.loads(line)["prompt"] for line in f]

# Load Mistral model
model_name = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Run inference
outputs = []
print(f"Running inference on {len(prompts)} prompts...")
for prompt in tqdm(prompts):
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)
    generated_ids = model.generate(input_ids, max_new_tokens=128, do_sample=True, top_p=0.95, temperature=0.7)
    response = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
    response_clean = response.replace(prompt, "").strip()
    outputs.append({
        "prompt": prompt,
        "generated_response": response_clean
    })

# Save outputs
Path("data").mkdir(exist_ok=True)
with open("data/pubmedqa_predictions_mistral.jsonl", "w", encoding="utf-8") as f:
    for o in outputs:
        f.write(json.dumps(o) + "\n")

print("Mistral inference complete. Results saved to data/pubmedqa_predictions_mistral.jsonl")