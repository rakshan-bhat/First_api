# LLM Query API

## Project Description
The LLM Query API is a web service that allows users to interact with a pre-trained language model to generate human-like text responses based on user queries. This API provides a simple and efficient way for developers and applications to leverage natural language processing capabilities.

## Table of Contents
- [Installation Instructions]
- [Usage Instructions]
- [API Endpoints]
- [Error Handling]
- [Environment Variables]
- [Contributing]
- [License]
- [Contact Information]

## Installation Instructions
1. Clone the repository:
git clone https://github.com/rakshan-bhat/First_api.git

2. Navigate into the project directory:
cd First_api


3. Create a virtual environment and activate it:
python -m venv venv

On Windows use: venv\Scripts\activate
source venv/bin/activate # On macOS/Linux


4. Install dependencies:
pip install -r requirements.txt



## Usage Instructions
To start the server, run:
python app.py


Once the server is running, you can send requests to the API endpoints using tools like Postman or cURL.

## API Endpoints

### 1. Root Endpoint (`/`)
- **Method:** GET
- **Description:** Returns a welcome message.
- **Response Example:**
"Welcome to the LLM API! Use /query to get responses."



### 2. Query Endpoint (`/query`)
- **Method:** POST
- **Description:** Accepts user queries and returns responses from the language model.
- **Request Body:**
{
"message": "What is the capital of France?"
}


- **Response Example (Success):**
{
"response": "The capital of France is Paris."
}


- **Response Example (Error):**
{
"error": "No message was found."
}



## Error Handling
Common error codes include:
- `400 Bad Request`: Indicates that the request body is missing or invalid.
- `415 Unsupported Media Type`: Indicates that the `Content-Type` header is not set to `application/json`.

## Environment Variables
To securely store your API keys, create a `.env` file in the root directory with the following content:
HUGGING_FACE_TOKEN=your_hugging_face_token_here


Make sure to load this variable in your application using `python-dotenv`.

## Contributing
Contributions are welcome! If you would like to contribute, please submit issues or pull requests for enhancements or bug fixes.

## License
This project is licensed under the MIT License.

## Contact Information
For questions or support, please contact Rakshan at rakshan@buildwithmelon.com
