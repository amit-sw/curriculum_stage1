# openai_utils.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_topic_name(topic_sentence, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",  # gpt-4.1-mini if available, else gpt-4-1106-preview
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": topic_sentence},
        ]
    )
    return response.choices[0].message.content.strip()

def get_curriculum(topic, prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4.1-mini",  # gpt-4.1-mini if available
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": topic},
        ]
    )
    return response.choices[0].message.content.strip()