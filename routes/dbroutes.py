from config import app,db
from flask import jsonify,request,abort
from models import DbPerson

@app.route("/req2emp")
def getDbPeople():
    listp=DbPerson.query.all()
    result = [x.serialize() for x in listp]
    return jsonify(result)


@app.route("/req2emp",methods=['POST'])
def processDepartments():
    try:
        input=request.get_json()
        eno=input['eno']
        ename=input['ename']
        city=input['city']
        desig=input['desig']
        basic=input['basic']
        db.session.add(DbPerson(eno,ename,city,desig,basic))
        db.session.commit()
        return {"status": "success"}, 201
    except:
        abort({'status':"Internal server error"},500)