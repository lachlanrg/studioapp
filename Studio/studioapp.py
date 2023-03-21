from flask import Flask, render_template
app = Flask(__name__)

# this is where I can add more html pages

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/student/')
def student():
    return render_template('student.html')


if __name__ == '__main__':
    app.run(debug=True)

