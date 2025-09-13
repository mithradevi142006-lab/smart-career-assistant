import streamlit as st
import openai

# -------------------------
# Smart Career Assistant
# -------------------------

st.set_page_config(page_title="Smart Career Assistant", page_icon="🎯", layout="wide")

st.title("Smart Career Assistant")
st.write("Welcome! Ask any career-related question or explore tips below.")

# -------------------------
# User Input Section
user_input = st.text_input("Ask me a career-related question:")

if user_input:
    try:
        # Use OpenAI API key from Streamlit secrets
        openai.api_key = st.secrets["OPENAI_API_KEY"]

        # Call GPT
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # change to gpt-4 if you have access
            messages=[
                {"role": "system", "content": "You are a helpful career assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        answer = completion.choices[0].message.content
        st.write(answer)

    except Exception as e:
        st.write("Error:", e)

# -------------------------
# Optional: Career Tips Button
if st.button("Show Career Tips"):
    st.write("""
    1. Keep learning new skills.
    2. Build a strong portfolio.
    3. Network actively.
    4. Stay updated with industry trends.
    """)
