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
    empty = """data:image/png;base64,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"""
    imageName = post_body.get('imageName', empty)
    job = Job(
        title = title,
        name = name,
        email = email,
        price = price,
        bio = bio,
        imageName = imageName
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


@app.route('/api/job/<int:job_id>/', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.filter_by(id=job_id).first()
    if not job:
        return json.dumps({'success': False, 'error': 'Job not found'}), 404
    db.session.delete(job)
    db.session.commit()
    return json.dumps({'success': True, 'data': job.serialize()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
