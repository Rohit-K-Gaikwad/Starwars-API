from flask import Flask

from taskone.main_taskone import v1
from tasktwo.main_tasktwo import v2
from taskthree.main_taskthree import v3

app = Flask(__name__)


# register all the sub-applications here
app.register_blueprint(v1)  # /v1/taskone
app.register_blueprint(v2)  # /v2/tasktwo
app.register_blueprint(v3)  # /v3/taskthree


if __name__ == "__main__":
    app.run(host="localhost", port=4000, debug=True)
