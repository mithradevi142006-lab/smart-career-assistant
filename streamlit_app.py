import streamlit as st

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="AI Career Assistant Demo",
    page_icon="🤖",
    layout="wide"
)

# -------- HEADER --------
st.markdown(
    """
    <h1 style='text-align: center; color: #4B0082;'>🤖 AI Career Assistant Demo</h1>
    <p style='text-align: center; font-size:18px;'>Interactive demo with Resume tips, LinkedIn posts, Career advice, Interview Q&A, Skill quiz, and Image generator (all predefined)</p>
    """, unsafe_allow_html=True
)
st.markdown("---")

# -------- TABS --------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💼 Resume Tips",
    "📝 LinkedIn Posts",
    "🎯 Career Advice",
    "❓ Interview Q&A & Skill Quiz",
    "🖼️ AI Image Demo"
])

# -------- TAB 1: Resume Tips --------
with tab1:
    st.subheader("Select Resume Tip Category")
    resume_option = st.radio("Choose an option:", ["Internship", "Job", "Skills", "Projects", "Education", "Format"])

    resume_responses = {
        "Internship": "💡 Focus on projects, coursework, and relevant achievements.",
        "Job": "💼 Highlight professional experience, measurable results, and leadership roles.",
        "Skills": "🛠️ Include both technical and soft skills prominently.",
        "Projects": "📁 Show 2-3 impactful projects with results and technologies used.",
        "Education": "🎓 Mention GPA, honors, and relevant courses.",
        "Format": "📄 Use clear headings, bullet points, and consistent formatting."
    }

    st.success(resume_responses[resume_option])

# -------- TAB 2: LinkedIn Posts --------
with tab2:
    st.subheader("Select LinkedIn Post Type")
    post_option = st.radio("Choose an option:", ["Project", "Promotion", "Achievement", "New Job", "Learning", "Thank You"])

    post_responses = {
        "Project": "🚀 Proud to announce completion of my latest project! Collaboration wins!",
        "Promotion": "🎉 Excited to share my promotion! Grateful for my team and mentors.",
        "Achievement": "🏆 Celebrating milestones motivates both you and your network.",
        "New Job": "💼 Thrilled to join my new company! Looking forward to contributing.",
        "Learning": "📚 Just completed a new certification! Continuous learning is key.",
        "Thank You": "🙏 Heartfelt thanks to mentors and colleagues for their guidance."
    }

    st.success(post_responses[post_option])

# -------- TAB 3: Career Advice --------
with tab3:
    st.subheader("Choose Career Advice Topic")
    advice_option = st.radio("Select an option:", ["Coding", "Interview", "Networking", "Resume", "Skills Growth", "Job Search"])

    advice_responses = {
        "Coding": "💻 Practice regularly and contribute to open-source projects.",
        "Interview": "📝 Prepare with mock interviews and research companies thoroughly.",
        "Networking": "🤝 Attend meetups and connect with professionals online.",
        "Resume": "📝 Tailor your resume for each job description you apply to.",
        "Skills Growth": "🚀 Learn in-demand technologies and track your progress.",
        "Job Search": "🔍 Apply consistently and follow up professionally."
    }

    st.success(advice_responses[advice_option])

# -------- TAB 4: Interview Q&A & Skill Quiz --------
with tab4:
    st.subheader("Interview Q&A")
    q_option = st.selectbox("Select a question:", [
        "Tell me about yourself",
        "Strengths and Weaknesses",
        "Why should we hire you?",
        "Describe a challenging project"
    ])

    q_responses = {
        "Tell me about yourself": "👤 I am a dedicated professional with experience in [field] and a passion for continuous learning.",
        "Strengths and Weaknesses": "💪 Strength: Problem-solving. ⚠️ Weakness: Perfectionism, which I manage with prioritization.",
        "Why should we hire you?": "🎯 I bring relevant experience, adaptability, and a commitment to delivering results.",
        "Describe a challenging project": "🚀 Managed a project under tight deadlines, coordinated a team, and delivered successfully."
    }

    st.info(q_responses[q_option])

    st.markdown("---")
    st.subheader("Skill Assessment Quiz")
    quiz_question = "Which programming language is best known for data analysis and machine learning?"
    quiz_options = ["Python", "C++", "JavaScript", "HTML"]
    answer = st.radio(quiz_question, quiz_options)
    if st.button("Check Answer", key="quiz"):
        if answer == "Python":
            st.success("✅ Correct! Python is widely used in data analysis and ML.")
        else:
            st.error("❌ Incorrect. The correct answer is Python.")

# -------- TAB 5: AI Image Demo --------
with tab5:
    st.subheader("AI Image Generator (Placeholder)")
    img_prompt = st.text_input("Enter image prompt:", placeholder="e.g., futuristic city, robot art")
    if st.button("Generate Image", key="img_gen"):
        if img_prompt.strip() != "":
            st.image(
                "https://via.placeholder.com/500x300.png?text=AI+Generated+Image",
                caption=f"Generated image for: {img_prompt}",
                use_column_width=True
            )
            st.success("✅ Image generated successfully (placeholder)")
        else:
            st.warning("⚠️ Please enter a prompt first!")

# -------- FOOTER --------
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size:14px;'>📝 Demo buildathon prototype. All outputs are predefined. No real AI API is used.</p>",
    unsafe_allow_html=True
)

