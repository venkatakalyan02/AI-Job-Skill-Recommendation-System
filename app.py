from flask import Flask, render_template, request
from utils.ai_logic import get_trending_skills, recommend_by_role

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    skills = None
    trends = None
    job_role = None

    if request.method == 'POST':
        job_role = request.form['job_role']
        skills = recommend_by_role(job_role)
        trends = get_trending_skills()

    return render_template(
        'index.html',
        skills=skills,
        trends=trends,
        job_role=job_role
    )

if __name__ == '__main__':
    app.run(debug=True)
