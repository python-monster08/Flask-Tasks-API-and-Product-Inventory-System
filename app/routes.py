from flask import Blueprint, request, jsonify
from .models import Task, db

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()

    if not data or 'description' not in data:
        return jsonify({'error': 'Description is required'}), 400

    description = data.get('description')

    try:
        new_task = Task(description=description, status="Incomplete")
        db.session.add(new_task)
        db.session.commit()
        return jsonify({'message': 'Task created!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'description': task.description, 'status': task.status} for task in tasks])

@tasks_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()

    try:
        task.description = data.get('description', task.description)
        task.status = data.get('status', task.status)
        db.session.commit()
        return jsonify({'message': 'Task updated!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@tasks_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
