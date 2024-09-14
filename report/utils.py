import os
from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_response(report):
    # Call the OpenAI API to generate the response
    response = recommended_action(report)
    # Format and return the response
    return format_response(response)

def recommended_action(report):
    system_prompt = f"""You are an AI assistant trained to provide 
    recommended responses for various types of emergency incidents. 
    Your task is to analyze user-reported incidents and provide the most 
    suitable response based on the type and severity of the situation. Please 
    respond to the incident report by providing clear, actionable recommendations 
    to emergency personell based on the type of incident described. Here is the
    user report: {report}"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": system_prompt
        }],
        temperature=0.8,
        max_tokens=2000
    )

    return response

def format_response(response):
    # Extract the generated story from the response
    answer = response.choices[0].message.content
    # Remove any unwanted text or formatting
    answer = answer.strip()
    # Return the formatted story
    return answer