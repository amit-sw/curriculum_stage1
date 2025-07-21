# config.py
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

DEFAULT_PROMPT = """
Prompt for Curriculum Generation:

You are designing a training curriculum for seasoned professionals. Given the following inputs:
	•	Topic Sentence: [Provide Topic Sentence Here]
	•	Description: [Provide Detailed Topic Description Here]

Create a structured curriculum outline that includes:

1. Key Learning Objectives:
	•	Clearly define measurable learning goals for participants.

2. Core Concepts Required for Mastery:
	•	Outline the essential concepts and principles necessary for participants to deeply understand and master the topic.

3. Assessment Questions for Trainee Mastery:
	•	Provide key evaluative questions that participants should confidently answer upon completing the training, reflecting a thorough grasp of the subject matter.

Ensure the curriculum aligns closely with the provided Topic Sentence and Description, is appropriate for seasoned professionals, and promotes analytical depth and practical application.

Please provide curriculum directly, without any additional commentary.
"""

TOPIC_PROMPT = "Generate a topic name for the following sentence."
DESCRIPTION_PROMPT = "Generate a short description for the following topic sentence."
OPENAI_API_KEY = st.secrets.get('OPENAI_API_KEY', os.environ.get('OPENAI_API_KEY'))
DB_FILE = "output/curriculum.db"

DEFAULT_SESSION_DURATION = 60  # Default session duration in minutes