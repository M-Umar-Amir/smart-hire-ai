# SmartHireAI Starter (16-week FYP)

This is a starter repository for the SmartHireAI project — an agentic, multimodal job ad assistant.

## Features (starter)
- Text generation (Qwen-VL-Chat via Hugging Face Inference API) — fallback template if no token
- Lightweight bias detection using spaCy + lexicon
- Image/banner generation using Stable Diffusion XL (Hugging Face)
- Mock LinkedIn formatting
- Simulated Google Calendar scheduling stub

## Setup (local testing)
1. Create virtual environment and activate:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
2. Export your Hugging Face token (optional, but required for real LLM/image calls):
   ```bash
   export HF_TOKEN=hf_xxx   # Mac/Linux
   set HF_TOKEN=hf_xxx      # Windows
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deploy to Streamlit Cloud
1. Push repository to GitHub.
2. On Streamlit Cloud, create a new app and link to the repo.
3. Add secrets via **Manage app -> Secrets**:
   ```
   HF_TOKEN = hf_xxx
   ```
4. Deploy.

## Notes
- This is a starter template. For production or a full FYP, expand bias lexicons, add real LinkedIn posting (use API or automation), and implement Google Calendar OAuth flow.
- Keep your Hugging Face token private.
