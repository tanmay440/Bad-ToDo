#import the necessary modules
from flask import Flask, render_template, request, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

#innitalise flask app
app = Flask(__name__)

#set up sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#class to define schema
class ToDo(db.Model):
    #define the schema

    # serial number primary key
    sno = db.Column(db.Integer, primary_key=True)

    #title of the object cannot be null
    title = db.Column(db.String(200), nullable=False)

    #description cannot be null
    desc = db.Column(db.String(400), nullable=False)

    #date created default is utc at that time
    date_created = db.Column(db.String(800), default=datetime.utcnow)

    #what should we give out if we want string?
    def __repr__(self) -> str:

        #this
        return f"{self.sno} | {self.title}"


#at home page, allow 'GET'and'POST'. also, run home() function
@app.route('/', methods=['GET', 'POST'])
def home():
    #if we get a POST req.(to add to the todo list) add to the todo list
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        today = datetime.today().strftime("%Y-%m-%d | %H:%M:%S")
        todo = ToDo(title=title, desc=desc, date_created=today)
        db.session.add(todo)
        db.session.commit()
    #get all the todos
    alltodo = ToDo.query.all()
    #give out index.html wtih variable "alltodo" containing all the todo list items
    return render_template("index.html", alltodo=alltodo)


#/delete with an int sno to be deleted
@app.route('/delete/<int:sno>')
def delete(sno):
    #delete the entry at given sno
    to_delete = ToDo.query.filter_by(sno=sno).first()
    db.session.delete(to_delete)
    db.session.commit()
    #send back to home
    return redirect("/")


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = ToDo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        todo.date_created = datetime.today().strftime("%Y-%m-%d | %H:%M:%S")
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    to_update = ToDo.query.filter_by(sno=sno).first()

    return render_template("update.html", todo=to_update)

@app.route("/about")
def about():
    return render_template("about.html")

#run the flask app
if __name__ == "__main__":
    app.run(debug=True, port=8000)
