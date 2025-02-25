import os
from typing import TypedDict
from flask import Flask, request, jsonify
from server.openapi import Image, run_prompt
from dotenv import load_dotenv
import logging

load_dotenv()

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("flask")
HOST = os.getenv("FLASK_HOST", "127.0.0.1")
PORT = int(os.getenv("FLASK_PORT", 5000))


class PromptParams(TypedDict):
    prompt: str
    instructions: str
    images: list[Image]


@app.route("/", methods=["POST"])
def handle_run_prompt():
    req_json: PromptParams = request.get_json()
    images = req_json["images"]
    prompt = req_json["prompt"]
    instructions = req_json["instructions"]
    logger.log(
        logging.INFO,
        f"Prompt params:\nPrompt: {prompt}\nInstructions: {instructions}\nImage count: {len(images)}",
    )
    output = run_prompt(prompt, instructions, images)
    return jsonify(output)


def main():
    app.run(debug=True, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
