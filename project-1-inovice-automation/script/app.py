import os
import logging
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "clean_cashflow.py")

@app.route("/payment", methods=["POST"])
def payment_webhook():
    # 1. Validate JSON
    if not request.is_json:
        logging.warning("Payload is not JSON")
        return jsonify({"error": "Invalid payload format"}), 400

    payload = request.get_json()
    invoice_id = payload.get("invoice_id")
    status     = payload.get("status")

    # 2. Validate required fields
    if not invoice_id or not status:
        logging.warning("Missing invoice_id or status in %s", payload)
        return jsonify({"error": "invoice_id and status required"}), 400

    # 3. Launch background process
    try:
        subprocess.Popen(
            ["python", SCRIPT_PATH, "--update", str(payload)],
            cwd=os.path.dirname(SCRIPT_PATH),
        )
        logging.info("Launched update for invoice %s → %s", invoice_id, status)
    except Exception as e:
        logging.error("Failed to launch process: %s", e, exc_info=True)
        return jsonify({"error": "Internal server error"}), 500

    # 204 = accepted, no content
    return ("", 204)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
