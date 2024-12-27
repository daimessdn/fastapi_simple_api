# fastapi_simple_api

Here's a simple example of API development using FastAPI.

## Setup

1. Assuming `virtualenv` or `venv` has installed, create a virtual environment. Using `python3 -m venv venv` will add a virtual environment
2. Type `source venv/bin/activate` to use the Inside the virtual environment.
3. Inside the virtual environment, Install all dependencies: `pip install -r requirements.txt`
4. Run `uvicorn main:app --reload` to run FastAPI server. Server will be runned in port `8000`.

## Installation Command

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```
