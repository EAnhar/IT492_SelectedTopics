import logging
import arrow  # Replacement for datetime, based on moment.js
import flask
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import acp_times  # brevet time calculations
import config
from pymongo import MongoClient
import os

app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY

Hostname = CONFIG.HOSTNAME
DBname = CONFIG.DATABASE
Collectionname = CONFIG.COLLECTION


client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
# db = client.brevetsdb

# Hostname = 'brevets_mongodb'
# DBname = 'brevetsDB'
# Collectionname = 'brevetsCol'
# #from docker-compose.yml
# client = MongoClient(host=Hostname, port=27017)
db = client[DBname][Collectionname]


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('brevets.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


@app.route("/_calc_times")
def _calc_times():
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)

    app.logger.debug(f"request.args: {request.args}")
    app.logger.debug(f"km={km}")

    brevet_dist = request.args.get('brevet_dist', 0, type = int)
    begin_date = request.args.get('begin_date', "", type = str).strip()
    begin_time = request.args.get('begin_time', "", type = str).strip()
    # starting_time = arrow.get(begin_date + " " + begin_time, 'YYYY-MM-DD HH:mm')
    combined_datetime_str = "{} {}".format(begin_date, begin_time)
    starting_time = arrow.get(combined_datetime_str, 'YYYY-MM-DD HH:mm')

    open_time = acp_times.open_time(km, brevet_dist, starting_time)
    close_time = acp_times.close_time(km, brevet_dist, starting_time)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)



# @app.route('/display', methods=['GET', 'POST'])
# def display():
#     #checkpoint, opentime, closetime stored
#     _items = db.find()
#     items = [item for item in _items]
#     # print(_items,items)
#     #if there are no values entered then nothing to display
#     #return warning message
#     if (len(items) == 0): return render_template('errorWarning.html')
#     print(items)
#     #else, go to html and display checkpoint, opentime, closetime
#     return render_template('display.html', items=items)

@app.route('/display', methods=['GET', 'POST'])
def display():
    # Fetch the data from the database
    existing_data = db.find_one({"brevets": {"$exists": True}})

    # Check if there is any data to display
    if existing_data and "brevets" in existing_data:
        brevets = existing_data["brevets"]
    else:
        brevets = []

    # Pass the data to the template
    return render_template('display.html', brevets=brevets)



#if the user hits submit with no values entered, then go here and
#show them the error
@app.route('/submiterror')
def submiterror():
    return render_template('submiterror.html')
    


@app.route('/new', methods=['GET', 'POST'])
def new():
    # Get the values the user entered/program displayed
    openInfo = request.form.getlist("open")
    closeInfo = request.form.getlist("close")
    kmInfo = request.form.getlist("km")
    brevet_dist = request.form.get("distance", type=int)
    begin_date = request.form.get("begin_date", type=str)
    begin_time = request.form.get("begin_time", type=str)

    # Check if the lists are empty
    if not openInfo or not closeInfo or not kmInfo or not begin_date or not begin_time:
        return redirect(url_for('submiterror'))

    # Constructing the controls list
    controls = []
    for i in range(len(kmInfo)):
        if kmInfo[i]:  # Ensure that km info is not empty
            control = {
                "km": int(kmInfo[i]),
                "open": openInfo[i] if i < len(openInfo) else None,
                "close": closeInfo[i] if i < len(closeInfo) else None
            }
            controls.append(control)

    # Construct the brevet document
    brevet = {
        "brevet_dist": brevet_dist,
        "begin_date": begin_date,
        "begin_time": begin_time,
        "controls": controls
    }

    existing_data = db.find_one({"brevets": {"$exists": True}})
    if not existing_data:
        existing_data = {"brevets": []}

    # Add the new brevet to the list of brevets
    existing_data["brevets"].append(brevet)

    # Update the database
    db.update_one({"brevets": {"$exists": True}}, {"$set": existing_data}, upsert=True)
    
    print("Data saved:", brevet)

    # Redirect to the home page
    return redirect(url_for('index'))


app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
    app.run(port=CONFIG.PORT, host="0.0.0.0", debug=True)
