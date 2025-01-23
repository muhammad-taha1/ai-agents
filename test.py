import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()
apiKey = os.getenv("OPEN_ROUTER_KEY")

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer " + apiKey,
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    "model": "meta-llama/llama-3.2-1b-instruct:free", # Optional
    "messages": [
      {"role": "user", "content": "What is the meaning of life?"}
    ],
    "top_p": 1,
    "temperature": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "repetition_penalty": 1,
    "top_k": 0,
  })
)

print(response.json())