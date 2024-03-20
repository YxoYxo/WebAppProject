from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return "<p>Login</>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        companyName = request.form.get('companyName')
        streetAdd = request.form.get('streetAdd')
        city = request.form.get('city')
        state = request.form.get('state')
        zipCode = request.form.get('zipCode')
        country = request.form.get('country')
        email = request.form.get('email')
        contactNum = request.form.get('contactNum')
        
    return render_template("register.html")


