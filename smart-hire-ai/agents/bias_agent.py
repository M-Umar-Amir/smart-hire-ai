# Simple bias checker without spaCy for quick testing

# Lightweight bias lexicon
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
