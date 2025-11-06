from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "LUyGjnll5mLpe7s64P52oGEBWJA0ARl3"  # kendi APILayer key'in
PROXY_URL = "http://s3Wq9B:L6p1kZ@206.168.88.84:50100"  # yeni proxy formatı

proxies = {
    "http": PROXY_URL,
    "https": PROXY_URL
}

@app.route("/whois")
def whois_check():
    domain = request.args.get("domain")
    if not domain:
        return jsonify({"error": "missing domain"}), 400
    try:
        url = f"https://api.apilayer.com/whois/check?domain={domain}"
        headers = {"apikey": API_KEY}
        r = requests.get(url, headers=headers, proxies=proxies, timeout=15)
        return jsonify(r.json()), r.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "✅ Proxy Çalışıyor - /whois?domain=example.com"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
