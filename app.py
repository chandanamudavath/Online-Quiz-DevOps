from flask import Flask, render_template, request

app = Flask(__name__)
questions = [
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["HTML", "Python", "Java", "All of these"],
        "answer": "All of these"
    },
    {
        "question": "What does Docker help us do?",
        "options": [
            "Create containers",
            "Edit images",
            "Write documents",
            "Browse websites"
        ],
        "answer": "Create containers"
    },
    {
        "question": "Which tool is used for CI/CD?",
        "options": ["Jenkins", "MS Word", "Paint", "Calculator"],
        "answer": "Jenkins"
    },
    {
        "question": "What does Kubernetes manage?",
        "options": [
            "Containers",
            "Spreadsheets",
            "Images",
            "Text files"
        ],
        "answer": "Containers"
    }
]


@app.route("/")
def home():
    return render_template("index.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, question in enumerate(questions):
        selected = request.form.get(f"question{i}")

        if selected == question["answer"]:
            score += 1

    return render_template(
        "result.html",
        score=score,
        total=len(questions)
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
