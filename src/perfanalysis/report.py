from datetime import datetime
from typing import Dict


def generate_html_report(analysis: Dict) -> str:
    """
    Generate HTML report from analysis results.
    """

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    rows = ""
    for student in analysis["students_at_risk"]:
        rows += (
            f"<tr>"
            f"<td>{student['student_id']}</td>"
            f"<td>{student['name']}</td>"
            f"<td>{student['score']}</td>"
            f"</tr>"
        )

    html = f"""
    <html>
        <head>
            <title>Student Performance Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 60%;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
            </style>
        </head>
        <body>
            <h1>Student Performance Report</h1>
            <p><strong>Generated:</strong> {timestamp}</p>

            <h2>Summary</h2>
            <ul>
                <li>Total students: {analysis['total_students']}</li>
                <li>Average score: {analysis['average_score']}</li>
            </ul>

            <h2>Students at Risk</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Score</th>
                </tr>
                {rows if rows else "<tr><td colspan='3'>None</td></tr>"}
            </table>
        </body>
    </html>
    """

    return html
