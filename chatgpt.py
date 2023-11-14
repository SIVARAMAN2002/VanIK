# import openai
# import os
# import pandas as pd
# import time
# openai.api_key = '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'
# def get_completion(prompt, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,
#         )
#     return response.choices[0].message["content"]

# prompt = "helo"

# response = get_completion(prompt)

# print(response)

# import Bard as google_bard
 
# # Replace "YOUR_API_KEY" with the actual API Key obtained earlier
# API_KEY = "AIzaSyA35cANg1MQroZu8lbe-J2XNyM35Ta0IlQ"
 
# def main():
#     query = "What is the meaning of life?"
#     response = google_bard.generate_text(query, api_key=API_KEY)
#     print("Google Bard Response (Using google_bard Module):")
#     print(response)
 
# if __name__ == "__main__":
#     main()   


# from bardapi import Bard
# import os
# import time

# os.environ['_BARD_API_KEY']="cgjQw3wYrLGWWjHYlpQ2u9TTlFvhErRQUAB3dJx9RZ3DOii3hig9FxfoALS302DZDQBc-Q"
# print(Bard().get_answer("why the sky is blue")['content'])


# from os import environ
# from Bard import Chatbot

# Secure_1PSID = environ.get("cgjQw3wYrLGWWjHYlpQ2u9TTlFvhErRQUAB3dJx9RZ3DOii3hig9FxfoALS302DZDQBc-Q.")
# Secure_1PSIDTS = environ.get("sidts-CjEBNiGH7m3PRk4hqsbMvYenRwM3Lj-_xS4LSaBQP3GnRK1rentqduw8p01A4o7erXL-EAA")
# chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)

# chatbot.ask("Hello, how are you?")


# from bardapi import Bard

# token = 'cgjQw3wYrLGWWjHYlpQ2u9TTlFvhErRQUAB3dJx9RZ3DOii3hig9FxfoALS302DZDQBc-Q.'
# bard = Bard(token=token)
# bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']


import google.generativeai as palm
import os

palm.configure(api_key='AIzaSyBcb60MeRiWmN7AJH8u_bpKyDxyW1ZNQN8')
#reducing the size of string 
def truncate_string_to_bytes(input_string, max_size_bytes):
    if len(input_string.encode('utf-8')) <= max_size_bytes:
        return input_string
    else:
        truncated_string = input_string
        while len(truncated_string.encode('utf-8')) > max_size_bytes:
            truncated_string = truncated_string[:-1]
        return truncated_string
def PalmConfig(text_file):
  if(len(text_file) >2000):
      text_file = truncate_string_to_bytes(text_file,2000)
  response = palm.generate_text(prompt="The opposite of hot is")
  print(response.result) #  'cold.'
  response = palm.chat(messages=[text_file,"Based on these given reviews of other places give me insights for my business."])
  return response.last #  'Hello! What can I help you with?'
  
  

