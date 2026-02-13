from flask import Flask, render_template, request
from diagnosis import diagnose_issue

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")
        result = diagnose_issue(symptoms)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
