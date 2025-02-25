# Silvia

Silvia is a server that uses OpenAI's GPT-4-based language model to extract information from images in json format.

## Table of Contents

- [Silvia](#silvia)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Server](#server)
    - [Prerequisites](#prerequisites-1)
    - [Setup virtual environment](#setup-virtual-environment)
    - [Activate virtual environment](#activate-virtual-environment)
    - [Install dependencies](#install-dependencies)
    - [Run server](#run-server)
    - [Configuration](#configuration)
    - [Endpoints](#endpoints)
      - [POST `/`](#post-)
  - [Example](#example)
    - [Prerequisites](#prerequisites-2)
    - [Install dependencies](#install-dependencies-1)
    - [Run example](#run-example)

## Prerequisites

- Clone the repository

```bash
git clone https://github.com/SenZmaKi/Silvia.git
```

## Server

### Prerequisites

- [Python 3.12.7](https://www.python.org/downloads/release/python-3127/) or higher
- [OpenAI API Key](https://platform.openai.com/account/api-keys), set it to the `OPENAI_API_KEY` environment variable (can be set in a `.env` file in the root directory)

### Setup virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

- Windows

```bash
venv\Scripts\activate
```

- Linux/Mac

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run server

```bash
python -m server
```

### Configuration

The server can be configured by setting environment variables (can be set in a `.env` file in the root directory):

- `FLASK_HOST`: The host to run the server on. Defaults to `127.0.0.1`.
- `FLASK_PORT`: The port to run the server on. Defaults to `5000`.

### Endpoints

#### POST `/`

Receives a JSON object with the following properties:

- `prompt (string)`: The prompt to send to the language model.
- `instructions (string)`: The instructions to send to the language model.
- `images ([Image])`: An array of images to send to the language model. Each image is an object with the following properties:
  - `base64_data (string)`: The base64 encoded image data. This is the encoding format OpenAI expects.
  - `format (string)`: The file format of the image, e.g., "jpeg".

## Example

- Extracts information from a receipt image.

### Prerequisites

- [Node.js](https://nodejs.org/en/download/) version 23.2.0 or higher

### Install dependencies

```bash
npm install
```

### Run example

```bash
npm run dev
```
