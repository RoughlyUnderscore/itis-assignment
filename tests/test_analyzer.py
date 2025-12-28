import pandas as pd
import pytest

from perfanalysis.analyzer import analyze_students, RISK_THRESHOLD


def sample_dataframe():
    return pd.DataFrame(
        {
            "student_id": [1, 2, 3],
            "name": ["Alice", "Bob", "Charlie"],
            "score": [90, 55, 70],
        }
    )


def test_analyze_students_basic():
    df = sample_dataframe()

    result = analyze_students(df)

    assert result["total_students"] == 3
    assert result["average_score"] == round((90 + 55 + 70) / 3, 2)


def test_students_at_risk_detection():
    df = sample_dataframe()

    result = analyze_students(df)

    at_risk = result["students_at_risk"]

    assert len(at_risk) == 1
    assert at_risk[0]["name"] == "Bob"
    assert at_risk[0]["score"] < RISK_THRESHOLD


def test_empty_dataframe_raises_error():
    df = pd.DataFrame()

    with pytest.raises(ValueError):
        analyze_students(df)


def test_missing_score_column_raises_error():
    df = pd.DataFrame(
        {
            "student_id": [1],
            "name": ["Alice"],
        }
    )

    with pytest.raises(ValueError):
        analyze_students(df)
