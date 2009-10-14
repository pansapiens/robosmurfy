from google.appengine.ext import db
from google.appengine.api import users

class Waver(db.Model):
  user_id = db.StringProperty(required=True)
  wave_address = db.StringProperty(required=True)
  
class Replacement(db.Model):
  match = db.StringProperty(required=True)
  new = db.StringProperty(required=True)

class Regex(db.Model):
  regex = db.StringProperty(required=True)

