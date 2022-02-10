from werkzeug.security import generate_password_hash,check_password_hash
from . import db

class User(db.Model):
    #...
    pass_secure = db.Column(db.String(255))
 
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)