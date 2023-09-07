"""
If you want to call real coordinates data from Sentinel2A
Just follow the steps below:
1. Replace line 17 by:
   from service.const import IssSatellite, Sentinel2A
2. Replace line 48 by:
    Worker(
        Sentinel2A.SENTINEL2A_URI.value,
        is_sentinel=True
    )
"""
from flask import (
    Flask,
    render_template,
    Response
)
from service.const import IssSatellite
from service.worker import Worker
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return render_template(
        'index.html'
    )


@app.route('/consumer_iss')
def iss():
    worker = Worker(
        IssSatellite.ISS_URI.value,
        is_iss=True
    )

    return Response(
        worker.consumer(),
        mimetype="text/event-stream"
    )


@app.route('/consumer_sentinel')
def sentinel():
    worker = Worker(
        "",
        is_sentinel=True
    )

    return Response(
        worker.consumer(),
        mimetype="text/event-stream"
    )


if __name__ == '__main__':
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5001
    )
