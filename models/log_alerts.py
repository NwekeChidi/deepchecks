from utils.db import db

# Define schema
class LogAlertsModel(db.Model):
  __tablename__ = "log_alerts"

  id = db.Column(db.Integer, primary_key=True)
  input = db.Column(db.Text)
  output = db.Column(db.Text)
  alert = db.Column(db.Text)
  timestamp = db.Column(db.DateTime)

  def json(self):
    return {
      "id": self.id,
      "input": self.input,
      "output": self.output,
      "alert": self.alert,
      "timestamp": self.timestamp
    }