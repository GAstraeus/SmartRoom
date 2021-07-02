import flask
import os
import configuration

import traceback

from flask import request



import logging

logging.basicConfig(filename="server.log", level=logging.DEBUG, format="%(levelname)s:%(asctime)s:%(message)s")

app = flask.Flask(__name__)


@app.before_first_request
def setup():
    pass


@app.route('/incoming', methods=["POST"])
def incoming():
    try:
        if request.method == "POST":
            logging.debug("*********Recieved Message")
            logging.debug(request.form)
            print(request.form)

            return "200"

    except Exception:
        logging.warning(request.form)
        logging.exception("Internal Server Error")
        traceback.print_exc()
        return "500 Internal Server Error"


if __name__ == "__main__":
    app.run(
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0'),
        debug=False
    )

