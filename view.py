import asyncio
import traceback
from quart import jsonify, Quart, request
from wiki_search import search_results
from wikipedia.exceptions import PageError

app = Quart(__name__)

@app.route("/", methods=["GET"])
async def wiki_search():
    host = request.host
    if host:
        subdomain = host.split(".")[0] 
    error_msg = ""
    status = 200
    try:
        results = search_results(subdomain)
    except PageError:
        error_msg = subdomain + " did not return any wikipedia search results."
        status = 404
    except:
        error_msg = traceback.format_exc()
        status = 500
    if not error_msg:
        return jsonify({"links": results}), status
    else:
        return jsonify({"error": error_msg}), status

app.run(host="localhost")
