from datevault import db

class Login(db.Modelodel):
    #schema for the login model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(250), unique=False, nullable=False)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    #partner login details
    partner_user_name = db.Column(db.VARCHAR(50), unique=True, nullable=False)
    partner_password = db.Column(db.VARCHAR(250), unique=False, nullable=False)
    partner_email = db.Column(db.VARCHAR(100), unique=True, nullable=False)

    def __repr__(self):
        #__repr__ to represent itself in the form of a string.
        return self.user_name
    