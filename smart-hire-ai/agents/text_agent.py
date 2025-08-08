import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.getenv("HF_TOKEN", "")
MODEL = "Qwen/Qwen-VL-Chat"  # change if needed

def generate_job_ad(prompt: str) -> str:
    if not HF_TOKEN:
        # Fallback simple template when no token present
        return f"Job Title & Role based on prompt:\n{prompt}\n\nResponsibilities:\n- ...\nQualifications:\n- ...\nBenefits:\n- ...\n\n(Note: Add HF_TOKEN to use cloud LLM generation.)"
    client = InferenceClient(token=HF_TOKEN)
    try:
        response = client.text_generation(model=MODEL, inputs=prompt, max_new_tokens=300)
        # The InferenceClient returns a dict-like output; try to extract text
        if isinstance(response, dict):
            return response.get('generated_text') or str(response)
        # For other formats, convert to string
        return str(response)
    except Exception as e:
        return f"[LLM generation error: {e}]\n\nFallback template:\n{prompt}"
