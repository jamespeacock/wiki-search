import asyncio
import traceback
from quart import jsonify, Quart, request
from wiki_search import search_results

app = Quart(__name__)

@app.route("/", methods=["GET"])
async def wiki_search():
    host = request.host
    if host:
        subdomain = host.split(".")[0] 
    try:
        results = search_results(subdomain)
    except:
        error_msg = traceback.format_exc()
    if results:
        return jsonify({"links": results})
    else:
        return jsonify({"error": error_msg}), 500

app.run(host="localhost")
