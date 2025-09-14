import streamlit as st

# --------- PAGE CONFIG ---------
st.set_page_config(
    page_title="AI Buildathon Demo",
    page_icon="🤖",
    layout="wide"
)

# --------- HEADER ---------
st.markdown(
    """
    <h1 style='text-align: center; color: #4B0082;'>🤖 AI Buildathon Demo</h1>
    <p style='text-align: center; font-size:18px;'>Interactive AI assistant demo for resumes, LinkedIn posts, career advice, and image generation (placeholder)</p>
    """, unsafe_allow_html=True
)
st.markdown("---")

# --------- TABS ---------
tab1, tab2 = st.tabs(["💼 Resume & LinkedIn Assistant", "🖼️ AI Image Generator"])

# --------- TAB 1: RESUME & POSTS ---------
with tab1:
    st.subheader("Choose a Task")
    task = st.selectbox(
        "",
        ["Generate Resume Tip", "Generate LinkedIn Post", "Career Advice"]
    )

    st.markdown("**Type your query below:**")
    user_input = st.text_input("", placeholder="e.g., internship resume, project post, coding tips")
    
    if st.button("Submit Query"):
        # Expanded predefined responses
        responses = {
            "Generate Resume Tip": {
                "default": "✅ Make your resume concise and highlight achievements.",
                "internship": "💡 Focus on projects and coursework for internships.",
                "job": "💼 Emphasize professional experience and measurable results for jobs.",
                "skills": "🛠️ Highlight relevant technical and soft skills prominently.",
                "projects": "📁 Include 2-3 impactful projects with results and technologies used.",
                "format": "📄 Use clear headings, bullet points, and consistent formatting.",
                "education": "🎓 Mention GPA, honors, and relevant courses for academics."
            },
            "Generate LinkedIn Post": {
                "default": "🌟 Sharing your achievements on LinkedIn boosts visibility.",
                "promotion": "🎉 Excited to share my promotion! Thanks to my team.",
                "project": "🚀 Proud of completing my latest project. Collaboration wins!",
                "achievement": "🏆 Celebrating milestones increases engagement with your network.",
                "newjob": "💼 Excited to join my new company! Looking forward to contributing.",
                "learning": "📚 Sharing recent learning or certification can inspire your connections.",
                "thankyou": "🙏 Appreciate mentors and colleagues in your post for authenticity."
            },
            "Career Advice": {
                "default": "📚 Keep learning and networking in your field.",
                "coding": "💻 Practice coding and contribute to open-source projects.",
                "interview": "📝 Prepare with mock interviews and research companies.",
                "resume": "📝 Tailor your resume to each job description.",
                "networking": "🤝 Attend meetups and connect with professionals online.",
                "skills": "🛠️ Learn in-demand technologies relevant to your career path.",
                "growth": "🚀 Take small steps daily; consistency beats speed in long-term growth."
            }
        }

        def get_response(task, query):
            q = query.lower()
            for key, resp in responses[task].items():
                if key in q:
                    return resp
            return responses[task]["default"]

        if user_input.strip() != "":
            result = get_response(task, user_input)
            st.success(result)
        else:
            st.warning("⚠️ Please type something before submitting!")

# --------- TAB 2: IMAGE GENERATOR ---------
with tab2:
    st.subheader("AI Image Generator (Demo)")
    st.markdown("This is a **placeholder demo** simulating AI image generation.")

    img_prompt = st.text_input("Enter image prompt", placeholder="e.g., futuristic city, robot art")
    if st.button("Generate Image"):
        if img_prompt.strip() != "":
            st.image(
                "https://via.placeholder.com/500x300.png?text=AI+Generated+Image",
                caption=f"Generated image for: {img_prompt}",
                use_column_width=True
            )
            st.success("✅ Image generated successfully (placeholder)")
        else:
            st.warning("⚠️ Please enter a prompt first!")

# --------- STYLISH FOOTER ---------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size:14px;'>📝 Demo version for buildathon submission. No real AI API is used. All outputs are predefined or placeholder images.</p>",
    unsafe_allow_html=True
)
