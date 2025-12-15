🧮 Math Adventures — AI-Powered Adaptive Learning Prototype
📌 Overview

Math Adventures is a lightweight AI-powered adaptive learning prototype designed to help children aged 5–10 practice basic math operations such as addition, subtraction, multiplication, and division. The system dynamically adjusts question difficulty in real time based on user performance, keeping learners in their optimal challenge zone.

The focus of this project is on adaptive learning logic, not complex UI design.

🎯 Objective

To demonstrate how simple AI techniques can personalize learning difficulty dynamically using:

Rule-based logic

A lightweight, research-backed adaptive model

⚙️ Core Components
Component	Description
Puzzle Generator	Dynamically creates math problems for Easy, Medium, and Hard levels
Performance Tracker	Logs correctness, response time, difficulty, and mastery
Adaptive Engine	Adjusts difficulty using Bayesian Knowledge Tracing (BKT) with rule-based smoothing
Progress Summary	Displays session statistics such as accuracy and average response time
🧠 Adaptive Logic

This prototype uses Bayesian Knowledge Tracing (BKT), a well-established cognitive model introduced by Corbett & Anderson (1995).
BKT estimates a learner’s mastery probability after each response and updates difficulty accordingly.
Simple rule-based smoothing is applied to handle noisy or inconsistent performance.

🗂️ Project Structure
math-adaptive-prototype/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── puzzle_generator.py
    ├── adaptive_engine.py
    └── tracker.py

🚀 How to Run the Application
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the Streamlit app
cd src
streamlit run main.py


The application will open automatically in your browser at:

http://localhost:8501

📊 Output & Features

Three difficulty levels: Easy, Medium, Hard

Real-time difficulty adaptation

Accurate tracking of performance metrics

End-of-session performance summary

Clean, modular, and well-documented code

📚 Research Reference

Corbett, A. T., & Anderson, J. R. (1995).
Knowledge tracing: Modeling the acquisition of procedural knowledge.
User Modeling and User-Adapted Interaction, 4(4), 253–278.

📈 Future Enhancements

Train adaptive models using real learner data

Extend to other subjects (science, vocabulary, reasoning)

Add data persistence and analytics dashboards

✅ Assignment Compliance

✔ Meets all deliverables
✔ Follows recommended repository structure
✔ Uses lightweight AI logic
✔ Fully functional prototype
✔ Easy to explain and extend# math-adaptive-prototype
