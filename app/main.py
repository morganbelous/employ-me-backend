import json
from .db import db, Job
from flask import Flask, request

db_filename = "todo.db"
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///%s' % db_filename
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
 return "Hello World!", 200


@app.route('/api/jobs/')
def get_jobs():
    jobs = Job.query.all()
    res = {'success': True, 'data': [j.serialize() for j in jobs]}
    return json.dumps(res), 200


@app.route('/api/jobs/', methods = ['POST'])
def create_job():
    post_body = json.loads(request.data)
    title = post_body.get('title', '')
    name = post_body.get('name', '')
    email = post_body.get('email', '')
    price = post_body.get('price', '')
    bio = post_body.get('bio', '')
    job = Job(
        title = title,
        name = name,
        email = email,
        price = price,
        bio = bio
    )
    db.session.add(job)
    db.session.commit()
    return json.dumps({'success': True, 'data': job.serialize()}), 200


@app.route('/api/job/<int:job_id>/')
def get_job(job_id):
    job = Job.query.filter_by(id=job_id).first()
    if not job:
        return json.dumps({'success': False, 'error': 'Job not found'}), 404
    return json.dumps({'success': True, 'data': job.serialize()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
