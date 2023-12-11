
import logging
import flask
import config
from vocab import Vocab
from jumble import jumbled
from letterbag import LetterBag

app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY  # Should allow using session variables

WORDS = Vocab(CONFIG.VOCAB)


@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
    """The main page of the application"""
    flask.g.vocab = WORDS.as_list()
    flask.session["target_count"] = min(
        len(flask.g.vocab), CONFIG.SUCCESS_AT_COUNT)
    flask.session["jumble"] = jumbled(
        flask.g.vocab, flask.session["target_count"])
    flask.session["matches"] = []
    app.logger.debug("Session variables have been set")
    assert flask.session["matches"] == []
    assert flask.session["target_count"] > 0
    app.logger.debug("At least one seems to be set correctly")
    return flask.render_template('vocab.html')


@app.route("/keep_going")
def keep_going():
    """
    After initial use of index, we keep the same scrambled
    word and try to get more matches
    """
    flask.g.vocab = WORDS.as_list()
    return flask.render_template('vocab.html')


@app.route("/success")
def success():
    return flask.render_template('success.html')

#######################
# Form handler.
#   You'll need to change this to
#   a JSON request handler
#######################


@app.route("/_check" , methods=["POST"])
def check():

    app.logger.debug("Entering check")

    text = flask.request.json["attempt"]

    jumble = flask.session["jumble"]
    matches = flask.session.get("matches", [])  # Default to empty list

    app.logger.debug(f"Received text: {text}")
    app.logger.debug(f"Current matches: {matches}")


    in_jumble = LetterBag(jumble).contains(text)
    matched = WORDS.has(text)

    # Respond appropriately
    if matched and in_jumble and not (text in matches):
        # Cool, they found a new word
        matches.append(text)
        flask.session["matches"] = matches
    elif text in matches:
        flask.flash(f"تم العثور على ({text}) بالسابق.")
    elif text not in jumble:
        for letter in text:
            if letter not in jumble:
                flask.flash(f"الحرف({letter}) غير موجود بالقائمة .")
    else:
        app.logger.debug("This case shouldn't happen!")
        assert False  # Raises AssertionError

    if len(matches) >= flask.session["target_count"]:
        solved = True #this boolean will trigger success page to show on vocab.html
    else: solved = False

    rslt = {"flashMessage": flask.get_flashed_messages(), "solved": solved, "matchesMade": matches, "matchMade":  matched , "newt":text}
    return flask.jsonify(result = rslt)

###############
# AJAX request handlers
#   These return JSON, rather than rendering pages.
###############


@app.route("/_example")
def example():
    """
    Example ajax request handler
    """
    app.logger.debug("Got a JSON request")
    rslt = {"key": "value"}
    return flask.jsonify(result=rslt)


#################
# Functions used within the templates
#################

@app.template_filter('filt')
def format_filt(something):
    """
    Example of a filter that can be used within
    the Jinja2 code
    """
    return "Not what you asked for"

###################
#   Error handlers
###################


@app.errorhandler(404)
def error_404(e):
    app.logger.warning(f"++ 404 error: {e}")
    return flask.render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    app.logger.warning(f"++ 500 error: {e}")
    assert not True  # I want to invoke the debugger
    return flask.render_template('500.html'), 500


@app.errorhandler(403)
def error_403(e):
    app.logger.warning(f"++ 403 error: {e}")
    return flask.render_template('403.html'), 403


if __name__ == "__main__":
    if CONFIG.DEBUG:
        app.debug = True
        app.logger.setLevel(logging.DEBUG)
        app.logger.info(f"Opening for global access on port {CONFIG.PORT}")
        app.run(port=CONFIG.PORT, host="0.0.0.0")
