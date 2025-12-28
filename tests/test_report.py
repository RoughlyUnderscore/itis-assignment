from perfanalysis.report import generate_html_report


def sample_analysis():
    return {
        "total_students": 2,
        "average_score": 72.5,
        "students_at_risk": [
            {
                "student_id": 2,
                "name": "Bob",
                "score": 55,
            }
        ],
    }


def test_generate_html_report_returns_string():
    analysis = sample_analysis()

    html = generate_html_report(analysis)

    assert isinstance(html, str)


def test_html_report_contains_summary_data():
    analysis = sample_analysis()

    html = generate_html_report(analysis)

    assert "Student Performance Report" in html
    assert "Total students: 2" in html
    assert "Average score: 72.5" in html


def test_html_report_contains_student_data():
    analysis = sample_analysis()

    html = generate_html_report(analysis)

    assert "Bob" in html
    assert "55" in html
