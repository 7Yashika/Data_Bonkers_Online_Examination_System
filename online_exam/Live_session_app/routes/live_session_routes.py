from flask import Blueprint, request
from controllers.live_session_controller import ExaminationController

# Create the blueprint
exam_routes = Blueprint('exam_routes', __name__)

# Instantiate the controller
examination_controller = ExaminationController()

# Define routes using the blueprint
@exam_routes.route('/live_sessions/<int:session_id>', methods=['GET'])
def get_live_session(session_id):
    return examination_controller.get_live_session(session_id)

@exam_routes.route('/live_sessions', methods=['POST'])
def create_live_session():
    return examination_controller.create_live_session()

@exam_routes.route('/live_sessions/<int:session_id>', methods=['PUT'])
def update_live_session(session_id):
    return examination_controller.update_live_session(session_id)

@exam_routes.route('/live_sessions/<int:session_id>', methods=['DELETE'])
def delete_live_session(session_id):
    return examination_controller.delete_live_session(session_id)

