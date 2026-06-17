import mysql.connector
from mysql.connector import Error
from flask import Flask,render_template,request,redirect,session,flash
from database import get_db_connection
app=Flask(__name__)
app.secret_key="nayepankh_secret_key"
@app.route('/')
def home():
    return render_template(
        'home.html',
        active_page='home'
    )
@app.route('/about')
def about():
    return render_template(
        'about.html',
        active_page='about'
    )
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        skills = request.form['skills']
        availability = request.form['availability']
        message = request.form['message']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO volunteers
        (name, email, phone, city, skills, availability, message)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            name,
            email,
            phone,
            city,
            skills,
            availability,
            message
        )

        try:
            cursor.execute(query, values)
            conn.commit()

            flash("Volunteer registered successfully!", "success")

        except mysql.connector.IntegrityError:
            flash("A volunteer with this email already exists!", "error")

        except Exception as e:
            print(e)
            flash("Something went wrong. Please try again.", "error")

        finally:
            cursor.close()
            conn.close()

        return redirect('/register')

    return render_template(
    'register.html',
    active_page='register'
)
@app.route('/admin', methods=['GET', 'POST'])
def admin():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM admins WHERE username=%s AND password=%s",
            (username, password)
        )

        admin = cursor.fetchone()

        cursor.close()
        conn.close()

        if admin:
            session['admin'] = username

            flash("Logged in successfully!", "success")

            return redirect('/dashboard')

        else:
            flash("Invalid username or password!", "error")

            return redirect('/admin')

    return render_template(
    'admin_login.html',
    active_page='admin'
)
@app.route('/dashboard')
def dashboard():

    if 'admin' not in session:
        return redirect('/admin')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM volunteers")
    total_volunteers = cursor.fetchone()['total']

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM volunteers
        WHERE availability = 'Weekdays'
    """)
    weekday_volunteers = cursor.fetchone()['total']

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM volunteers
        WHERE availability = 'Weekends'
    """)
    weekend_volunteers = cursor.fetchone()['total']

    cursor.execute("""
        SELECT COUNT(*) AS total
        FROM volunteers
        WHERE availability = 'Both'
    """)
    both_volunteers = cursor.fetchone()['total']

    cursor.execute("""
        SELECT *
        FROM volunteers
        ORDER BY id DESC
        LIMIT 5
    """)
    recent_volunteers = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
    'dashboard.html',
    active_page='dashboard',
    total_volunteers=total_volunteers,
    weekday_volunteers=weekday_volunteers,
    weekend_volunteers=weekend_volunteers,
    both_volunteers=both_volunteers,
    recent_volunteers=recent_volunteers
)
@app.route('/volunteers')
def volunteers():
    if 'admin' not in session:
        return redirect('/admin')
    search=request.args.get('search', '')
    conn=get_db_connection()
    cursor=conn.cursor(dictionary=True)
    if search:
        query = """
        SELECT *
        FROM volunteers
        WHERE name LIKE %s
        OR city LIKE %s
        OR skills LIKE %s
        """
        search_term=f"%{search}%"
        cursor.execute(
            query,
            (search_term, search_term, search_term)
        )
    else:
        cursor.execute("SELECT * FROM volunteers")
    volunteers=cursor.fetchall()
    print(volunteers)
    cursor.close()
    conn.close()
    return render_template(
    'volunteers.html',
    volunteers=volunteers,
    search=search,
    active_page='volunteers'
)
@app.route('/logout')
def logout():

    session.pop('admin', None)

    flash("Logged out successfully!", "success")

    return redirect('/admin')
if __name__=='__main__':
    app.run(debug=True) 