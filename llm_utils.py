# llm_utils.py
import openai
from config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)

def get_topic_name(topic_sentence, prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": topic_sentence},
        ]
    )
    return response.choices[0].message.content.strip()

def get_curriculum(topic, prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": topic},
        ]
    )
    return response.choices[0].message.content.strip()