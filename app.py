from flask import Flask, request, render_template, redirect, url_for,session,flash
from forms import SignupForm,SigninForm
from flask_sqlalchemy import SQLAlchemy
from backend.functions import generate_workout

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///wodder'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        # process the form data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['user_id'] = user.id
            session['email'] = user.email

            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
    return render_template('signin.html', form=form)


@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user is not None:
            flash('This email address is already registered!', 'danger')
            return redirect(url_for('signup'))

        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        flash('You have successfully signed up!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('signup.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'email' not in session:
        flash('Please sign in first!', 'danger')
        return redirect(url_for('signin'))
    
    email = session['email']
    user = User.query.filter_by(email=email).first()

    if request.method == 'POST':
        fitness_level = request.form['fitness-level']
        workout_length = int(request.form['workout-length'])

        result = generate_workout(fitness_level, workout_length)

        return render_template('dashboard.html', user=user, result=result)
    else:
        return render_template('dashboard.html', user=user)



@app.route('/generate-workout', methods=['GET', 'POST'])
def generate_workout_handler():
    if request.method == 'POST':
        fitness_level = request.form['fitness-level']
        workout_length = int(request.form['workout-length'])

        result = generate_workout(fitness_level, workout_length)

        return result
    else:
        # Handle GET request
        return render_template('generate_workout.html')


if __name__ == '__main__':
    app.run(debug=True)
