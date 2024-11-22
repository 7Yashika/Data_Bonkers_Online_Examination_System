from flask import Blueprint, request,render_template,flash,redirect,url_for,session
from controllers.user_controller import ExamController
from flask_cors import cross_origin

exam_routes = Blueprint('exam_routes', __name__)
controller = ExamController()


@exam_routes.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return controller.get_user(user_id)

@exam_routes.route("/user",methods=["GET"])
def get_all_users():
    return controller.get_all_users()

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
    student = controller.get_student(student_id)  # Get the student data
       
    print(student)
    if student.get("error") is not None:  # Check if the student is not found
        return render_template("view_profile.html", error=student.get("error"))
    
    return render_template("view_profile.html", student=student)  # Render the profile if student is found
    #except Exception as e:
       # return render_template("view_profile.html", error=f"An error occurred: {str(e)}")  # Handle errors
       

@exam_routes.route("/student",methods=["GET"])
def get_all_students():
    students= controller.get_all_students()

    if isinstance(students, dict) and students.get("error"):
        return render_template("view_all_students.html", error=students.get("error"))
    
    return render_template("view_all_students.html", students=students) 



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

@exam_routes.route("/student_portal")
def student_portal():
    email = session.get('email')  # Get the email from session

    if email in student_emails:
        student_id = student_emails.index(email) + 1  # Use the index as a student ID (or another unique ID logic)

        return render_template('student_portal.html', email=email, student_id=student_id)
    
    flash("No student found with this email")
    return redirect(url_for('exam_routes.login'))




@exam_routes.route('/')
def index():
    return render_template('index.html')


student_emails = ['s1p@gmail.com', 's2@gmail.com', 's3@gmail.com', 's4@gmail.com']
admin_emails = ['admin@gmail.com']


@exam_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')

        # Check if the email is in the student email list
        if email in student_emails:
            session['email'] = email  # Store the student's email in session
            
            return redirect(url_for('exam_routes.student_portal'))
        
        # Check if the email is an admin email
        elif email in admin_emails:
            # Redirect to admin portal
            return redirect(url_for('exam_routes.admin_portal'))
        
        else:
            flash("Invalid email domain or email not registered.")
            return redirect(url_for('exam_routes.login'))

    return render_template('login.html')


@exam_routes.route("/admin_portal")
def admin_portal():
    return render_template('admin_portal.html')

