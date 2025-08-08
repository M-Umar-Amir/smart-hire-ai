def format_linkedin_post(ad_text: str, prompt: str) -> str:
    # Shorten and format for LinkedIn post preview
    preview = ad_text.strip()
    if len(preview) > 800:
        preview = preview[:800] + "..."
    return f"LinkedIn Post Preview:\n\n{preview}\n\n#hiring #job #opportunity\nSource prompt: {prompt}"
