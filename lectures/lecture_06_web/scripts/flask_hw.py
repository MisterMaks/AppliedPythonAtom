#!/usr/bin/env python
# coding: utf-8

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    username = request.args.get("username")
    return "Hello %s" % username


# TODO Добавить рутинги /goodbye


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8081")
