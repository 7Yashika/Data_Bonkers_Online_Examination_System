from flask import Blueprint, request
from controllers.user_controller import ExamController

exam_routes = Blueprint('exam_routes', __name__)
controller = ExamController()

# User routes
@exam_routes.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return controller.get_user(user_id)

@exam_routes.route("/user", methods=["POST"])
def create_user():
    user_data = request.json
    return controller.create_user(user_data)

@exam_routes.route("/user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    return controller.update_user(user_id)

@exam_routes.route("/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return controller.delete_user()

# Student routes
@exam_routes.route("/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    return controller.get_student(student_id)

@exam_routes.route("/student", methods=["POST"])
def create_student():
    student_data = request.json
    return controller.create_student(student_data)

@exam_routes.route("/student/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    return controller.update_student(student_id)

@exam_routes.route("/student/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    return controller.delete_student()
