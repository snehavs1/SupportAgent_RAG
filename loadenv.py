import os
from getpass import getpass

try:
    from dotenv import load_dotenv
    load_dotenv(override=True)
except Exception:
    pass

if not os.getenv("GROK_API_KEY"):
    os.environ["GROK_API_KEY"] = getpass("Enter GROk_API_KEY: ")

if not os.getenv("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass("Enter TAVILY_API_KEY: ")

if not os.getenv("PINECONE_API_KEY"):
    os.environ["PINECONE_API_KEY"] = getpass("Enter PINECONE_API_KEY: ")

print("GROk_API_KEY configured:", bool(os.getenv("GROk_API_KEY")))
print("TAVILY_API_KEY configured:", bool(os.getenv("TAVILY_API_KEY")))
print("PINECONE_API_KEY configured:", bool(os.getenv("PINECONE_API_KEY")))