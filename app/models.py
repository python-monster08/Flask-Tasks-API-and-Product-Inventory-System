from . import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(10), nullable=False, default="Incomplete")

    def __repr__(self):
        return f'<Task {self.id}: {self.description}>'
