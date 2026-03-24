from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)

# The prompt is hardcoded here.
# Every time we want to improve output quality or fix a bug,
# we edit this string, open a PR, wait for review, and deploy.
SUMMARIZE_PROMPT = """You are a medical documentation assistant.
Summarize the following patient information into 3 concise bullet points.
Focus on: chief complaint, key findings, and plan.

Patient information:
{patient_info}"""


def summarize(patient_info: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": SUMMARIZE_PROMPT.format(patient_info=patient_info)}
        ],
    )
    return response.choices[0].message.content
