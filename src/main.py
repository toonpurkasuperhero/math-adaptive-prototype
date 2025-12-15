import streamlit as st
import time

from puzzle_generator import PuzzleGenerator
from adaptive_engine import AdaptiveEngine
from tracker import PerformanceTracker


st.set_page_config(page_title="Adaptive Math Learning", page_icon="🧠", layout="centered")

# ------------------- CSS -------------------
st.markdown("""
<style>
.main .block-container {
    max-width: 95% !important;
    padding-left: 3rem;
    padding-right: 3rem;
}
.question-card {
    background-color: #f8f9fa;
    padding: 25px;
    border-radius: 12px;
    border: 1px solid #e0e0e0;
    margin-bottom: 20px;
    text-align: center;
}
.question-card h3 {
    margin: 0;
    color: #000000 !important;
    font-size: 28px;
    font-weight: 600;
}
.result-card {
    padding: 20px;
    border-radius: 12px;
    margin-top: 20px;
    color: #000;
}
.difficulty-badge {
    padding: 6px 15px;
    border-radius: 8px;
    color: white;
    font-weight: bold;
}
.difficulty-easy { background-color: #28a745; }
.difficulty-medium { background-color: #ffc107; color:#000 }
.difficulty-hard { background-color: #dc3545; }
</style>
""", unsafe_allow_html=True)

# ------------------- INIT STATE -------------------
if "engine" not in st.session_state:
    st.session_state.engine = AdaptiveEngine()
    st.session_state.generator = PuzzleGenerator()
    st.session_state.tracker = PerformanceTracker()

    st.session_state.difficulty = "Easy"
    st.session_state.q_no = 0
    st.session_state.history = []
    st.session_state.session_done = False

    st.session_state.current_question = None
    st.session_state.current_answer = None
    st.session_state.phase = "question"      # NEW: "question" or "feedback"
    st.session_state.start_time = None
    st.session_state.last_correct = None
    st.session_state.time_taken = None

def badge(level):
    if level == "Easy": return '<span class="difficulty-badge difficulty-easy">Easy 🟢</span>'
    if level == "Medium": return '<span class="difficulty-badge difficulty-medium">Medium 🟡</span>'
    return '<span class="difficulty-badge difficulty-hard">Hard 🔴</span>'

# ------------------- GENERATE QUESTION -------------------
def generate_new_q():
    q, ans = st.session_state.generator.generate(st.session_state.difficulty)
    st.session_state.current_question = q
    st.session_state.current_answer = ans
    st.session_state.start_time = time.time()
    st.session_state.phase = "question"

# ------------------- MAIN -------------------
st.title("🧠 Adaptive Math Learning Dashboard")
st.write("Smart adaptive math practice using **BKT + Rule-Based Engine**.")

if not st.session_state.session_done:

    if st.session_state.current_question is None:
        generate_new_q()

    progress = st.session_state.q_no / 10
    st.progress(progress)

    st.subheader(f"Question {st.session_state.q_no + 1} of 10")
    st.markdown(badge(st.session_state.difficulty), unsafe_allow_html=True)

    # ------------------- PHASE 1: QUESTION -------------------
    if st.session_state.phase == "question":

        st.markdown(f"""
        <div class="question-card">
            <h3>{st.session_state.current_question}</h3>
        </div>
        """, unsafe_allow_html=True)

        user_input = st.text_input("✏️ Your Answer:", key=f"ans_{st.session_state.q_no}")

        if st.button("Submit Answer"):
            try:
                user_value = float(user_input)
            except:
                user_value = None

            st.session_state.time_taken = round(time.time() - st.session_state.start_time, 2)
            correct = (user_value == st.session_state.current_answer)
            st.session_state.last_correct = correct

            mastery = st.session_state.engine.update_mastery(correct)
            st.session_state.tracker.record(
                st.session_state.current_question,
                st.session_state.current_answer,
                user_value,
                correct,
                st.session_state.time_taken,
                st.session_state.difficulty,
                mastery
            )
            st.session_state.history.append(correct)
            st.session_state.difficulty = st.session_state.engine.choose_difficulty(st.session_state.history)

            st.session_state.phase = "feedback"
            st.rerun()

    # ------------------- PHASE 2: FEEDBACK -------------------
    else:
        correct = st.session_state.last_correct
        msg = "🎉 Correct!" if correct else "❌ Incorrect"
        color = "#d4edda" if correct else "#f8d7da"

        st.markdown(f"""
        <div class="result-card" style="background-color:{color};">
            <h4>{msg}</h4>
            <p><b>Correct Answer:</b> {st.session_state.current_answer}</p>
            <p><b>Time Taken:</b> {st.session_state.time_taken} sec</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Next Question ➡️"):
            st.session_state.q_no += 1

            if st.session_state.q_no >= 10:
                st.session_state.session_done = True
            else:
                generate_new_q()

            st.rerun()


# ------------------- SUMMARY -------------------
else:
    st.success("🎉 Session Completed!")
    summary = st.session_state.tracker.get_summary()
    df = summary["df"]

    st.subheader("📊 Performance Summary")
    st.dataframe(df, use_container_width=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Accuracy", f"{summary['accuracy']}%")
    col2.metric("Avg Time", f"{summary['avg_time']} sec")
    col3.metric("Final Mastery", f"{summary['final_mastery']}")

    st.write("🔁 Refresh the page to restart.")
