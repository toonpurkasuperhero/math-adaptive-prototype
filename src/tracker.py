import pandas as pd

class PerformanceTracker:
    def __init__(self):
        self.records = []

    def record(self, question, correct_answer, user_answer, correct, time_taken, difficulty, mastery):
        self.records.append({
            "Question": question,
            "Correct Answer": correct_answer,
            "User Answer": user_answer,
            "Correct": correct,
            "Time (sec)": time_taken,
            "Difficulty": difficulty,
            "Mastery": round(mastery, 3)
        })

    def get_summary(self):
        df = pd.DataFrame(self.records)

        return {
            "df": df,
            "accuracy": round(df["Correct"].mean() * 100, 2),
            "avg_time": round(df["Time (sec)"].mean(), 2),
            "final_mastery": df["Mastery"].iloc[-1]
        }
