from dotenv import load_dotenv
import os
import openai



openai.api_key = os.getenv("OPEN_API_KEY")

chat_completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Tell me about ShriRangam and shrivaishnavam",
    }
  ])
for chat in chat_completion:
    print(chat_completion.choices[0].message.content)