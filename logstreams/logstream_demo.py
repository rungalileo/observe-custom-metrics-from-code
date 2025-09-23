import os
from galileo.openai import openai
from galileo import galileo_context
from dotenv import load_dotenv

# Documentation: https://v2docs.galileo.ai/sdk-api/third-party-integrations/openai/openai

# Load environment variables from .env file
load_dotenv()

# Get the logger instance
logger = galileo_context.get_logger_instance()

# Start a session
session_id=logger.start_session("Legal Advice Session")

# Start a new trace
logger.start_trace("Legal Advice Request")

# Initialize the Galileo wrapped OpenAI client
client = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# First question: Legal advice (should trigger metric)
first_result = client.chat.completions.create(
    messages=[{"role": "user", "content": "I'm being sued by my former business partner. What should I do legally to protect myself?"}],
    model="gpt-4o"
)

print("Q: I'm being sued by my former business partner. What should I do legally to protect myself?")
print("A:", first_result.choices[0].message.content[:200] + "...")

# Second question: Non-legal question (should NOT trigger metric)
second_result = client.chat.completions.create(
    messages=[{
        "role": "user",
        "content": "What's the weather like today and what should I wear?"
    }],
    model="gpt-4o"
)

print("\nQ: What's the weather like today and what should I wear?")
print("A:", second_result.choices[0].message.content[:200] + "...")

print(f"\n✅ Session completed! Session ID: {session_id}")
