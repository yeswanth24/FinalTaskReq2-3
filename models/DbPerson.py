from config import db

class DbPerson(db.Model):
    __tablename__='req2emp'
    eno=db.Column(db.String(30),primary_key=True)
    ename=db.Column(db.String(30),index=False,unique=False,nullable=False)
    city=db.Column(db.String(30),index=False,unique=False,nullable=False)
    desig=db.Column(db.String(30),index=False,unique=False,nullable=False)
    basic=db.Column(db.String(30),index=False,unique=False,nullable=False)
    

    def __init__(self,eno,ename,city,desig,basic):
        self.eno=eno
        self.ename=ename
        self.city=city
        self.desig=desig
        self.basic=basic
    
    def serialize(self):
        return {
            'eno':self.eno,
            'ename':self.ename,
            'city':self.city,
            'desig':self.desig,
            'basic':self.basic
            }
    
    def __repr__(self):
        return str(self.serialize())