from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)

def check_banned(player_id):
    url = f"https://ff.garena.com/api/antihack/check_banned?lang=en&uid={player_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "referer": "https://ff.garena.com/en/support/",
        "x-requested-with": "B6FksShzIgjfrYImLpTsadjS86sddhFH"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json().get("data", {})
            is_banned = data.get("is_banned", 0)
            period = data.get("period", 0)

            result = {
                "credits": "@dear_sumi",
                "free repo": "https://github.com/bisug/FF-Ban-Check-api",
                "status": "BANNED" if is_banned else "NOT BANNED",
                "ban_period": period if is_banned else 0,
                "uid": player_id,
                "is_banned": bool(is_banned)
            }

            return Response(json.dumps(result), mimetype="application/json")
        else:
            return Response(json.dumps({"error": "Failed to fetch data from server", "status_code": 500}), mimetype="application/json")
    except Exception as e:
        return Response(json.dumps({"error": str(e), "status_code": 500}), mimetype="application/json")

@app.route("/bancheck", methods=["GET"])
def bancheck():
    player_id = request.args.get("uid", "")
    if not player_id:
        return Response(json.dumps({"error": "Player ID is required", "status_code": 400}), mimetype="application/json")
    return check_banned(player_id)
