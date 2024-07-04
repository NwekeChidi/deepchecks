from flask import Flask, jsonify, make_response, request
from werkzeug.exceptions import HTTPException, default_exceptions

from os import environ
from utils.calculateMetrics import calculate_metrics
from utils.db import db

import io
import os
import csv
import itertools

ALLOWED_EXTENSIONS = { "csv" }


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# initialize flask app
app = Flask(__name__)
app.config['BUNDLE_ERRORS'] = environ.get('BUNDLE_ERRORS')

# define error handlers
@app.errorhandler(Exception)
def error_handler(error):
  status_code = 500
  if isinstance(error, HTTPException): status_code = error.code
  print("this is error", error)
  return jsonify(error), status_code

# handle default errors
for default_exception in default_exceptions:
  app.register_error_handler(default_exception, error_handler)


# configure postgres to sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI') #settings.SQLALCHEMY_DATABASE_URI
db.init_app(app)
# create tables (not already existing)
with app.app_context():
  db.create_all()

#create a test route
@app.route('/ping', methods=['GET'])
def test():
  return make_response(jsonify({
    "status": True,
    "message": "test route"})), 200


# create post route
@app.route("/deepchecks/process", methods=["POST"])
def process_logs():
  try:
    print("this is request", request)

    db_inserts = []
    # handle threshold and conditions
    acceptable_conditions = ["le", "lt", "eq", "ge", "gt"]
    threshold = 50
    input_condition = "le"
    output_condition = "gt"

    if threshold in request.form: threshold = int(request.form["threshold"])

    if "input_condition" in request.form and request.form["input_condition"] in acceptable_conditions:
      input_condition = request.form["input_condition"]
    if "output_condition" in request.form and request.form["output_condition"] in acceptable_conditions:
      output_condition = request.form["output_condition"]
  
    # process file
    file = request.files["file"]
    if file and allowed_file(file.filename):

      # read the csv file
      file_content = io.StringIO(file.stream.read().decode("utf-8"))
      read_csv = csv.reader(file_content)

      for row in itertools.islice(read_csv, 1, None):
        print(row)
        db_inserts.append(calculate_metrics(row, threshold, input_condition, output_condition))
      
      # save to db
      db.session.bulk_save_objects(db_inserts)
      db.session.commit()

    return make_response(jsonify({
      "status": True,
      "message": "Logs processed successfully"
    })), 200
  except Exception as err:
    print("Error: >>", err)
    return make_response(jsonify({ 
      "status": False,
      "message": "Something went wrong 😕" })), 500

if __name__ == '__main__':
  app.run()