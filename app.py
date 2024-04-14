from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test_db"
)
cursor = db.cursor()


@app.route('/')
def index():
    return render_template('userinput.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        user_id = request.form['id']
        # Insert data into the database
        query = "INSERT INTO test_db.users (name, id) VALUES (%s, %s)"
        cursor.execute(query, (name, user_id))
        db.commit()
        return 'Data saved successfully!'


if __name__ == '__main__':
    app.run(debug=True)
