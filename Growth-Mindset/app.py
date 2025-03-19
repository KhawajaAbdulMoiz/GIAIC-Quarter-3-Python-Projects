import streamlit as st
# Setting page 
st.set_page_config(page_title="Growth Mindset", page_icon="✨")
st.title("🌟 Growth Mindset Challenge: Your Journey to Success 🌟")
# Welcome Section
st.header("Welcome to Your Growth Journey �")
st.write("""
Embark on a transformative journey where challenges become opportunities, and every step forward is a victory. 
This is your space to reflect, grow, and celebrate your progress. Let's cultivate a growth mindset together!
""")
# Quote Section
st.header("💬 Daily Dose of Inspiration")
st.write("""
*"The only limit to our realization of tomorrow is our doubts of today."* – Franklin D. Roosevelt
""")
# Challenge Input Section
st.header("💪 What's Your Challenge?")
user_input = st.text_input("Describe a challenge you're currently facing:")
if user_input:
    st.success(f"🌟 You're facing: **{user_input}**. Remember, every challenge is a stepping stone to growth. Keep pushing forward! 🌟")
else:
    st.warning("🚨 Share a challenge you'd like to overcome. It's the first step towards growth!")
# Reflection Input Section
st.header("📝 Reflect on Your Learning")
reflect = st.text_area("Write your reflection here:")
if reflect:
    st.success(f"✨ **Great Insight!** ✨\n\n{reflect}\n\nReflecting on your experiences is a powerful way to grow. Keep it up!")
else:
    st.info("💡 Take a moment to reflect on a past experience. What did you learn? How did it help you grow?")
# Achievements Input Section
st.header("🎉 Celebrate Your Achievements")
wins = st.text_input("Share something you've achieved recently (big or small!):")
if wins:
    st.success(f"🎊 **Congratulations!** 🎊\n\nYou've achieved: **{wins}**. Every achievement, no matter the size, is worth celebrating!")
else:
    st.info("🌟 Big or small, every achievement counts. Share something you're proud of!")
# Footer
st.write("---")
# Adding some Css
st.markdown(
    """
    <div style="text-align: center;">
        <p>💖 Keep believing in yourself. You're capable of amazing things! 💖</p>
        <p>Created with ❤️ by Khawaja Abdul Moiz</p>
    </div>
    """,
    unsafe_allow_html=True
)