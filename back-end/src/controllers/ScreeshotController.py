from flask import Blueprint, request, jsonify
from models.Screenshot import Screenshot
import asyncio


import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

screenshot_bp = Blueprint('screenshot_bp', __name__)

@screenshot_bp.route('/download', methods=['POST'])
def download_img():
    data = request.get_json()
    link = data.get('link')

    if not link:
        return jsonify({"error": "Campo 'link' é obrigatório"}), 400

    screenshot = Screenshot(link)

    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        result = loop.run_until_complete(screenshot.capture())
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f"Erro inesperado: {str(e)}"}), 500
