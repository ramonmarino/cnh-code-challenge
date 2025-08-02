# Challenge API

A simple FastAPI-based service that performs basic arithmetic operations.

## Features

- Four basic operations: sum, subtract, multiply, divide
- Validates input with clear error messages
- Structured with modular code: services, routes, logs, etc.
- Basic logging
- Ready for unit testing and extension

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn (for local dev server)
- Pydantic (data validation)
- Logging module

## Project Structure


## How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/ramonmarino/cnh-code-challenge.git
   cd cnh-code-challenge

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn app.main:app --reload

Open in browser:

http://127.0.0.1:8000/docs

Sample Request

json
POST /api/v1/challenge
{
  "operation": "sum",
  "operands": [10, 5]
}
Supported operations:

sum
subtract
multiply
divide

Response
json
{
  "result": 15
}
Error Handling

Invalid operations return:
400: Invalid operation type. Supported operations are: sum, subtract, multiply, divide

Less than 2 operands:
400: At least two operands are required.

Division by zero:
400: Division by zero is not allowed.**



