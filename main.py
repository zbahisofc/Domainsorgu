from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

# Environment değişkenlerinden al (Render üzerinden)
API_KEY = os.getenv("LUyGjnll5mLpe7s64P52oGEBWJA0ARl3")
PROXY = os.getenv("http://s3Wq9B:L6p1kZ@206.168.88.84:50100")

proxies = {
    "http": PROXY,
    "https": PROXY
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
    return "✅ Zbahis Proxy Çalışıyor - /whois?domain=example.com"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
