import streamlit as st

# Page Configuration
st.set_page_config(page_title="Pro Quiz Master", page_icon="🏆", layout="centered")

# 1. Questions Database (15 Questions)
quiz_data = [
    {"q": "What is the capital of France?", "o": ["Berlin", "Madrid", "Paris", "Rome"], "a": "Paris"},
    {"q": "Which programming language is known as the language of AI?", "o": ["Java", "Python", "C++", "HTML"], "a": "Python"},
    {"q": "What does CPU stand for?", "o": ["Central Process Unit", "Central Processing Unit", "Computer Personal Unit", "Central Processor Unit"], "a": "Central Processing Unit"},
    {"q": "Which planet is known as the Red Planet?", "o": ["Earth", "Mars", "Jupiter", "Venus"], "a": "Mars"},
    {"q": "Who developed the Python language?", "o": ["Mark Zuckerberg", "Guido van Rossum", "Elon Musk", "Bill Gates"], "a": "Guido van Rossum"},
    {"q": "What is the largest ocean on Earth?", "o": ["Atlantic", "Indian", "Arctic", "Pacific"], "a": "Pacific"},
    {"q": "In Python, which keyword is used to create a function?", "o": ["func", "define", "def", "lambda"], "a": "def"},
    {"q": "Which component is known as the brain of the computer?", "o": ["RAM", "Hard Disk", "CPU", "Monitor"], "a": "CPU"},
    {"q": "What is the square root of 64?", "o": ["6", "7", "8", "9"], "a": "8"},
    {"q": "Which of these is NOT an operating system?", "o": ["Windows", "Linux", "Python", "macOS"], "a": "Python"},
    {"q": "What is the chemical symbol for Water?", "o": ["O2", "CO2", "H2O", "HO2"], "a": "H2O"},
    {"q": "Which year did World War II end?", "o": ["1940", "1945", "1950", "1939"], "a": "1945"},
    {"q": "What is the smallest prime number?", "o": ["0", "1", "2", "3"], "a": "2"},
    {"q": "Which company owns the Android OS?", "o": ["Apple", "Microsoft", "Google", "Samsung"], "a": "Google"},
    {"q": "What is the main purpose of Streamlit?", "o": ["Game Development", "Web Apps for Data Science", "Operating Systems", "Video Editing"], "a": "Web Apps for Data Science"}
]

# 2. Initialize Session State
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'quiz_complete' not in st.session_state:
    st.session_state.quiz_complete = False

# --- UI Header ---
st.title("🎯 Professional Quiz Challenge")
st.markdown("---")

# 3. Quiz Logic
if not st.session_state.quiz_complete:
    item = quiz_data[st.session_state.current_index]
    
    # Progress Bar
    progress = (st.session_state.current_index) / len(quiz_data)
    st.progress(progress)
    
    st.subheader(f"Question {st.session_state.current_index + 1} of {len(quiz_data)}")
    st.write(f"### {item['q']}")

    # Answer Selection
    answer = st.radio("Choose the correct option:", item['o'], key=f"q_{st.session_state.current_index}")

    if st.button("Submit Answer"):
        if answer == item['a']:
            st.session_state.score += 5
            st.success("Correct! 🎉 (+5 Points)")
        else:
            st.session_state.score -= 2
            st.error(f"Wrong! ❌ (-2 Points). The correct answer was: {item['a']}")
        
        # Move to next or finish
        if st.session_state.current_index < len(quiz_data) - 1:
            st.session_state.current_index += 1
            st.rerun()
        else:
            st.session_state.quiz_complete = True
            st.rerun()

# 4. Final Result Display
else:
    st.header("🏁 Quiz Completed!")
    
    total_questions = len(quiz_data)
    max_possible_score = total_questions * 5
    user_score = st.session_state.score
    
    # Calculate Percentage (Result out of 100)
    # Using the formula: (User Score / Max Score) * 100
    final_percentage = (user_score / max_possible_score) * 100
    
    # Prevent negative percentage display if score is below zero
    display_percent = max(0, final_percentage)

    st.divider()
    col1, col2 = st.columns(2)
    col1.metric("Total Score", f"{user_score}")
    col2.metric("Percentage", f"{display_percent:.2f}%")

    if display_percent >= 80:
        st.balloons()
        st.success("Excellent Performance! 🌟")
    elif display_percent >= 50:
        st.info("Good Job! You passed. 👍")
    else:
        st.warning("Better luck next time! Keep practicing.📚")

    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.current_index = 0
        st.session_state.quiz_complete = False
        st.rerun()

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")