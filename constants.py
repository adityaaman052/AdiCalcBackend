from dotenv import load_dotenv
import os

# Load local .env only in development
if os.getenv("ENV", "dev") == "dev":
    load_dotenv()

# Get environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Server Config
SERVER_URL = os.getenv("SERVER_URL", "localhost")
PORT = os.getenv("PORT", "8900")
ENV = os.getenv("ENV", "dev")  # Default to "dev"
