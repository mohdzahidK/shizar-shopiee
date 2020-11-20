from flask import Flask , request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://postgres:poiuy@localhost:5432/shizar'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)




class ContactInfo(db.Model):
    __tablename__ = "Conatcts"
    id = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String)
    LastName = db.Column(db.String)
    Email = db.Column(db.String)
    Phone = db.Column(db.String)
    Password = db.Column(db.String)

    def __init__(self,FirstName,LastName,Email,Phone,Password):
         self.FirstName = FirstName
         self.LastName = LastName
         self.Email = Email
         self.Phone = Phone
         self.Password = Password
         print('data cretaed')




@app.route('/ConatctInfo', methods = ['post'])
def postContacts():
     data = request.get_json()
     FirstName = data["FirstName"]
     LastName = data["LastName"]
     Email = data["Email"]
     Phone = data["Phone"]
     Password = data["Password"]
     con = ContactInfo(FirstName,LastName,Email,Phone,Password)
     db.session.add(con)
     db.session.commit()
     return jsonify(message ="task list is created") , 201

@app.route('/ConatctInfo')
def getContacts():
     Contacts = ContactInfo.query.all()
     contcat_List = []
     for con in Contacts :
        c={}
        c["FirstName"] = con.FirstName
        c["LastName"] = con.LastName
        c["Email"] = con.Email
        c["Phone"] = con.Phone
        c["Password"] = con.Password
        contcat_List.append(c)
     return jsonify(list = contcat_List)    






















@app.route('/')
def get_task_lists():
    return "hello world"

if __name__ == '__main__':
     db.create_all()
     app.run(debug = True)
