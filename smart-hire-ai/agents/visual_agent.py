import os
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO

HF_TOKEN = os.getenv("HF_TOKEN", "")
MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

def generate_banner(prompt: str):
    if not HF_TOKEN:
        raise RuntimeError("HF_TOKEN not set. Add your Hugging Face token in Streamlit secrets or environment.")
    client = InferenceClient(token=HF_TOKEN)
    # The inference client may return bytes or a URL depending on model & plan.
    # Attempt text_to_image; adjust based on actual client behavior.
    result = client.text_to_image(model=MODEL, inputs=prompt)
    # If bytes, convert to PIL image
    if isinstance(result, (bytes, bytearray)):
        return Image.open(BytesIO(result))
    # If result is a dict with images
    if isinstance(result, dict) and 'images' in result:
        first = result['images'][0]
        if isinstance(first, (bytes, bytearray)):
            return Image.open(BytesIO(first))
    # Otherwise, raise for now
    raise RuntimeError(f"Unexpected result from image API: {type(result)}.\n{result}")
