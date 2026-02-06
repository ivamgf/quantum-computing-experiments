import os
from dotenv import load_dotenv

load_dotenv()

IBM_TOKEN = os.getenv("IBM_QUANTUM_TOKEN")
IBM_INSTANCE = os.getenv("IBM_QUANTUM_INSTANCE")

