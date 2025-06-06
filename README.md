# HealthNudge AI

HealthNudge AI is an intelligent health assistant powered by Machine Learning and Generative AI.  
It extracts lifestyle patterns, classifies health risk, and delivers personalized health guidance — with follow-up Q/A — from natural user input.

---

## What It Does

- Accepts free-text lifestyle or health-related input from the user  
- Extracts **habits & symptoms** using spaCy + scispaCy  
- Predicts health **risk level** (Low / Medium / High)  
- Generates **personalized health recommendations** using GenAI logic  
- Handles **follow-up questions** like “Why is this risky?” using PubMed-style answers  
- Loads real clinical datasets from AWS S3  
- Visualizes trends via a Streamlit dashboard (in progress)  
- Supports full MLOps workflow with DVC, MLflow, GitHub Actions (upcoming)

---

## Features

- Rule-based NER (lifestyle flag extractor)
- Risk prediction using rule logic → LightGBM upgrade planned
- Personalized recommendations (rule-based now → T5/Mistral soon)
- Q/A response from user questions (PubMedQA-style)
- Clean Python modules with full pipeline in `pipeline.py`
- Dataset management and versioning via S3 and `datasets`
- End-to-end executable flow with one command

---

## LLM Readiness & Prompting Plan

- Format: prompt-response `.jsonl` (`pubmedqa_prompts.jsonl`)
- Format type:  
  `"Context: <...>\nQuestion: <...>" → "Answer"`
- Ready for:
  - Fine-tuning `t5-small` or `mistral-7b-instruct`
  - Inference-only testing with LLM APIs
  - Retrieval-augmented generation (RAG) with `langchain` or `transformers`
- Prompt file is stored locally **and uploaded to S3**

---

## Technologies Used

| Layer      | Tools |
|------------|-------|
| **NLP/NER** | `spaCy`, `scispaCy`, `regex`, `datasets` |
| **Risk Model** | `LightGBM`, `scikit-learn` |
| **GenAI** | `transformers`, `T5`, `Mistral`, `PubMedQA` |
| **Backend** | `Python`, `boto3`, `AWS S3`, `Streamlit` |
| **DevOps/MLOps** | `venv`, `git`, `pip`, `GitHub`, `MLflow`, `DVC`, `Docker` |

---

## Dataset Sources

| Dataset | Use |
|---------|-----|
| `meowterspace42/clinical_notes` | Simulate real-world lifestyle and symptom inputs |
| `qiaojin/PubMedQA` | Used for health Q/A training and response grounding |

Both are downloaded via Hugging Face and stored in AWS S3 for scalable access.  
Cleaned, split, and formatted datasets are also uploaded to S3.

---

## Author

**Kaavya Loganathan**  
Graduate Student, MS in Information Systems  
Northeastern University, Boston, MA  
Focus: Medical AI • Generative AI • MLOps • AI • High-Performance Machine Learning  
[LinkedIn](https://www.linkedin.com/in/kaavyaloganathan/)  
[GitHub](https://github.com/kaavyaa03)

---

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.