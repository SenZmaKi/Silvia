import json
import logging
from typing import Callable, TypedDict
from dotenv import load_dotenv
import openai
import time


load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("openai")


class OpenAIException(Exception):
    pass


class Image(TypedDict):
    base64_data: str
    format: str


client = openai.OpenAI()
if not client.api_key:
    raise OpenAIException("OPENAI_API_KEY environment variable is not set.")


def print_runtime_later(task: str) -> Callable[[], None]:
    start_time = time.time()

    def print_runtime() -> None:
        elapsed_time = time.time() - start_time
        logger.info(f"Task {task} took {elapsed_time:.2f} seconds.")

    return print_runtime


def run_prompt(prompt: str, instructions: str, images: list[Image]) -> dict:
    logger.info(f"Prompting OpenAI with {len(images)} images")
    prt = print_runtime_later("Prompting OpenAI")
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    *[
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{image['format']};base64,{image['base64_data']}",
                            },
                        }
                        for image in images
                    ],
                ],
            },
            {
                "role": "system",
                "content": instructions,
            },
        ],
    )
    prt()
    output = response.choices[0].message.content
    if not output:
        raise OpenAIException("OpenAI response is empty.")
    logger.info(f"OpenAI response: {output}")
    output_json = json.loads(output)
    return output_json
