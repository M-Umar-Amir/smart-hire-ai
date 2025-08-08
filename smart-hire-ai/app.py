import streamlit as st
from agents.text_agent import generate_job_ad
from agents.bias_agent import detect_bias, suggest_replacements
from agents.visual_agent import generate_banner
from utils.linkedin_mock import format_linkedin_post
from agents.calendar_api import schedule_dummy_interview

st.set_page_config(page_title="SmartHireAI Starter", layout="wide")
st.title("SmartHireAI — Starter (Free Models, Cloud-first)")

st.markdown("""Enter a short prompt describing the role (title, key skills, company tone).\
The app will generate an inclusive job ad, run bias detection, create a banner, and show a mock LinkedIn post.""")

with st.form("prompt_form"):
    prompt = st.text_input("HR Prompt (e.g. 'Frontend Engineer — React, CSS, remote, inclusive team')", "")
    post_to_linkedin = st.checkbox("Simulate posting to LinkedIn", value=False)
    schedule_interview = st.checkbox("Simulate scheduling an interview", value=False)
    submitted = st.form_submit_button("Generate")

if submitted:
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating job ad..."):
            ad = generate_job_ad(prompt)
        st.subheader("Generated Job Ad")
        st.write(ad)

        st.subheader("Bias Detection")
        biases = detect_bias(ad)
        if biases:
            st.warning("Potential bias terms found: " + ", ".join(biases))
            suggestions = suggest_replacements(biases)
            st.write("Suggestions:")
            for b, s in suggestions.items():
                st.write(f"- **{b}** → {s}")
        else:
            st.success("No common bias terms detected (lightweight check).")

        st.subheader("Generated Banner (Stable Diffusion XL)")
        try:
            image = generate_banner(f"Banner for: {prompt}")
            st.image(image, use_column_width=True)
        except Exception as e:
            st.error(f"Image generation failed or no HF token provided. Error: {e}")

        st.subheader("LinkedIn Mock Post")
        post = format_linkedin_post(ad, prompt)
        st.code(post)

        if post_to_linkedin:
            st.info("Simulated posting... (this is a mock in the starter repo).")

        if schedule_interview:
            st.info("Scheduling dummy interview...")
            ev = schedule_dummy_interview(title="Interview: " + prompt)
            st.write(ev)
