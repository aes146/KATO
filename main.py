from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/my_schedules')
def my_schedules():
	return render_template('my_schedules.html')

if __name__ == "__main__":
    app.run(debug=True)