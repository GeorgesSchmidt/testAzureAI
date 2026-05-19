# Azure OpenAI Client

A simple Python client to interact with Azure OpenAI using object-oriented programming and PEP8 standards.

## Prerequisites

- Python 3.10+
- An Azure account with an active OpenAI deployment
- VSCode (recommended)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/GeorgesSchmidt/testAzureAI.git
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install openai python-dotenv pytest
```

### 4. Configure environment variables

Create a `.env` file at the root of the project:

```env
AZURE_OPENAI_ENDPOINT=https://your-resource.cognitiveservices.azure.com/
AZURE_OPENAI_KEY=your_api_key_here
AZURE_OPENAI_DEPLOYMENT=gpt-4o
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

## Usage

```bash
python3 Models/test_azure_openai.py
```

## Running Tests

Integration tests make real API calls to Azure OpenAI. Ensure your `.env` is properly configured before running them.

```bash
python3 -m pytest Tests/test_integration.py -v
```

## Project Structure

testAzureAI/
├── .env                  # Environment variables (not committed). 
├── .gitignore. 
├── README.md. 
├── test_azure_openai.py  # Main client. 
└── test_integration.py   # Integration tests. 

