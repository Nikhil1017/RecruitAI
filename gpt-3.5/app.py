import fitz,os
import time
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

start_time = time.time()

filename = "resume.pdf"
text = ""
doc = fitz.open(filename)
for page in doc:
    text += page.get_text("text")

    question = "I want you to check 4 things, 1 is if this guy has a cs degree, 2 is if he has work experience as a software engineer, 3 is if this guy has good projects, 4 is how many languages this guy can speak. if you has all 4 criteria, then your reply should be '4', if he has 3 of the 4 criteria then your reply should be 3 and so on"

chat_creation = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
     {
      "role": "user",
      "content":text
    },
     {
      "role": "user",
      "content":question
    }

  ])

print(chat_creation.choices[0].message.content)






print("Process finished --- %s seconds ---" % (time.time() - start_time))
