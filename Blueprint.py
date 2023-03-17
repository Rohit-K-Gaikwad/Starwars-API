from flask import Flask

from taskone.main_taskone import v1
from tasktwo.main_tasktwo import v2
from taskthree.main_taskthree import v3

app = Flask(__name__)


# register all the sub-applications here
app.register_blueprint(v1)   # /v1/taskone
app.register_blueprint(v2)   # /v2/tasktwo
app.register_blueprint(v3)   # /v3/taskthree


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=9000, debug=True)




# TODO
"""
1. convert swapi project task1, task2, task3 into Blueprints
2. register all blueprints with main application
3. endpoints will be like following

    - 127.0.0.1:8000/v1/taskone
    - 127.0.0.1:8000/v2/tasktwo
    - 127.0.0.1:8000/v3/taskthree
"""