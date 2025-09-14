import streamlit as st

# Page setup
st.set_page_config(page_title="AI Buildathon Demo", page_icon="🤖", layout="centered")

st.title("🤖 AI Buildathon Demo")
st.write("This is a **demo version**. Interact with it and see outputs instantly!")

# Tabs for different functionalities
tab1, tab2 = st.tabs(["Resume & Posts", "AI Image Generator"])

# ----------- Tab 1: Resume & LinkedIn Post Demo -----------
with tab1:
    st.header("💼 Resume & LinkedIn Post Assistant")
    
    # Sidebar task selection (for Tab 1)
    task = st.selectbox(
        "Choose Task",
        ["Generate Resume Tip", "Generate LinkedIn Post", "Career Advice"]
    )

    # Input box
    user_input = st.text_input("Type your query here:")

    # Predefined responses
    responses = {
        "Generate Resume Tip": {
            "default": "Make sure your resume is concise and highlights your key achievements.",
            "internship": "For internships, focus on your projects and any relevant coursework.",
            "job": "For job applications, emphasize your professional experience and measurable results."
        },
        "Generate LinkedIn Post": {
            "default": "Sharing your achievements on LinkedIn increases your professional visibility!",
            "promotion": "Excited to share my recent promotion! Grateful for my team and mentors.",
            "project": "Proud to announce the completion of my latest project! Collaboration makes the dream work."
        },
        "Career Advice": {
            "default": "Keep learning new skills and networking with professionals in your field.",
            "coding": "Practice coding regularly and contribute to open-source projects.",
            "interview": "Prepare with mock interviews and understand the company thoroughly."
        }
    }

    # Function to get output
    def get_response(task, query):
        query_lower = query.lower()
        for key, response in responses[task].items():
            if key in query_lower:
                return response
        return responses[task]["default"]

    # Show output
    if user_input:
        output = get_response(task, user_input)
        st.markdown(f"**AI Response:** {output}")
    else:
        st.write("Enter something above to get a response.")

# ----------- Tab 2: Image Generator Demo -----------
with tab2:
    st.header("🖼️ AI Image Generator (Demo)")
    prompt = st.text_input("Enter image prompt:")

    if st.button("Generate Image"):
        if prompt:
            # Placeholder image (no API)
            st.image("https://via.placeholder.com/400x250.png?text=AI+Generated+Image", 
                     caption=f"Image for: {prompt}")
        else:
            st.warning("Type something first!")

# Footer
st.markdown("---")
st.markdown("📝 **Note:** This is a demo version for buildathon submission. No real AI API is used. All outputs are predefined or placeholders.")
