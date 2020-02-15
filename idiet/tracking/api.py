from flask import Blueprint, Response


api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/hc", methods=["GET"])
def hc():
    return Response(status=200, mimetype="application/json")
