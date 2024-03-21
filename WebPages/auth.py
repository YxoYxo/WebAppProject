from flask import Blueprint, render_template, request, flash
import sqlite3

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
        
        if len(firstName) == 0:
            flash('First Name must be entered', category = 'error')
        elif len(firstName) < 2:
            flash('First Name too short, must be more than 3 charecters', category = 'error')
        elif len(lastName) == 0:
            flash('Last Name must be entered', category = 'error')
        elif len(lastName) == 2:
            flash('Last Name too short, must be more than 3 charecters', category = 'error')
        elif len(email) == 0:
            flash('Email must be entered', category = 'error')
        elif len(contactNum) == 0:
            flash('Contact Numbr must be entered', category = 'error')
        else:    
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO USER_REGISTER (first_name, last_name, company) VALUES (?,?,?)",(firstName, lastName, companyName))
                con.commit()
                flash('Inserted')
                
            con.close() 
            return render_template("home.html")
        
    return render_template("register.html")
                
            
            
            
            
        
    


