import streamlit as st
from openai import OpenAI
import os

# Initialize OpenAI client using environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="AI Text Generator", layout="centered")

st.title("🧠 AI Text Generator")
st.write("Generate text using Generative AI")

prompt = st.text_area("Enter your topic or prompt:", height=150)

if st.button("Generate Text"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt")
    else:
        with st.spinner("Generating..."):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI text generator."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200
            )

            st.subheader("✍️ Generated Text")
            st.write(response.choices[0].message.content)
