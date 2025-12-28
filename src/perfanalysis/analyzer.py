from typing import Dict

import pandas as pd


RISK_THRESHOLD = 60


def analyze_students(df: pd.DataFrame) -> Dict:
    """
    Analyze student performance data.

    Expected columns:
    - student_id
    - name
    - score
    """

    if df.empty:
        raise ValueError("Input dataframe is empty")

    if "score" not in df.columns:
        raise ValueError("Missing 'score' column")

    average_score = df["score"].mean()

    students_at_risk = df[df["score"] < RISK_THRESHOLD]

    result = {
        "total_students": len(df),
        "average_score": round(float(average_score), 2),
        "students_at_risk": students_at_risk[
            ["student_id", "name", "score"]
        ].to_dict(orient="records"),
    }

    return result
