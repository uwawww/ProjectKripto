from flask import Flask, jsonify, render_template, request

from cipher import VigenereError, generate_process, is_letter

MAX_TEXT_LENGTH = 10000

app = Flask(__name__)


def error_response(message, status=400):
    return jsonify({"success": False, "error": message}), status


def handle_cipher(mode):
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return error_response("Request body harus berupa JSON dengan field 'text' dan 'key'.")

    text = data.get("text")
    key = data.get("key")

    if not isinstance(text, str) or not text.strip():
        return error_response("Teks tidak boleh kosong.")
    if len(text) > MAX_TEXT_LENGTH:
        return error_response(f"Teks terlalu panjang (maksimal {MAX_TEXT_LENGTH} karakter).")

    try:
        output = generate_process(text, key, mode)
    except VigenereError as exc:
        return error_response(str(exc))

    warnings = []
    if any(not is_letter(c) for c in key):
        warnings.append(
            f"Karakter non-huruf pada key diabaikan. Key yang dipakai: {output['key']}."
        )
    if not output["process"]:
        warnings.append("Teks tidak mengandung huruf A-Z, sehingga tidak ada yang diproses.")

    return jsonify({
        "success": True,
        "mode": mode,
        "result": output["result"],
        "process": output["process"],
        "key": output["key"],
        "effective_key": output["effective_key"],
        "warnings": warnings,
    })


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/encrypt", methods=["POST"])
def api_encrypt():
    return handle_cipher("encrypt")


@app.route("/api/decrypt", methods=["POST"])
def api_decrypt():
    return handle_cipher("decrypt")


@app.errorhandler(405)
def method_not_allowed(_):
    return error_response("Method tidak diizinkan.", 405)


@app.errorhandler(500)
def server_error(_):
    return error_response("Terjadi kesalahan internal pada server.", 500)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)