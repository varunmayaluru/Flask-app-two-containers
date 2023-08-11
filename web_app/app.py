from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import sqlite3
import os

app = Flask(__name__)

DATABASE = "data.db"

def analyze_data(file):
    try:
        df = pd.read_csv(file)
        
        conn = sqlite3.connect(DATABASE)
        df.to_sql("data", conn, if_exists="replace", index=False)
        conn.close()

        summary = df.describe().to_html()
        return summary
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        summary = analyze_data(file)
        return render_template("index.html", summary=summary)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
