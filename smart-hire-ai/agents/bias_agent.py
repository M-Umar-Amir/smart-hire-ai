import spacy
import subprocess

# Ensure the spaCy model is installed at runtime
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Lightweight bias lexicon (expand for your project)
BIAS_WORDS = {
    "young": "early-career or experienced",
    "energetic": "motivated or proactive",
    "native": "proficient (language)",
    "aggressive": "assertive"
}

def detect_bias(text: str):
    found = []
    lower = text.lower()
    for w in BIAS_WORDS:
        if w in lower:
            found.append(w)
    return found

def suggest_replacements(words):
    return {w: BIAS_WORDS.get(w, "consider rewording") for w in words}
