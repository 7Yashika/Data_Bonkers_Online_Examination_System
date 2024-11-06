from flask import Blueprint
from controllers.examination_controller import ExaminationController

examination_routes = Blueprint('examination_routes', __name__)
controller = ExaminationController()

# Examination routes
examination_routes.route("/examination/<int:exam_id>", methods=["GET"])(controller.get_examination)
examination_routes.route("/examination", methods=["POST"])(controller.create_examination)
examination_routes.route("/examination/<int:exam_id>", methods=["PUT"])(controller.update_examination)
examination_routes.route("/examination/<int:exam_id>", methods=["DELETE"])(controller.delete_examination)


# UserResponse routes
examination_routes.route("/user_response/<int:response_id>", methods=["GET"])(controller.get_user_response)
examination_routes.route("/user_response", methods=["POST"])(controller.create_user_response)
examination_routes.route("/user_response/<int:response_id>", methods=["PUT"])(controller.update_user_response)
examination_routes.route("/user_response/<int:response_id>", methods=["DELETE"])(controller.delete_user_response)
