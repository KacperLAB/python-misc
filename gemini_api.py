import google.generativeai as genai
import os
import api_key

API_KEY=api_key.GEMINI_API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


response = model.generate_content(f"What's the avereage distance from Earth to Sun ? Print only number")
print(response.text)