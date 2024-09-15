import os
from openai import OpenAI
from django.conf import settings
import re

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_response(report):
    response = recommended_action(report)
    return format_response(response)

def generate_priority(report):
    response = priority(report)
    return clean_priority(response)

def generate_supplies(report):
    response = recommended_supplies(report)
    return format_response(response)

def generate_user_actions(report):
    response = recommended_user_action(report)
    return format_response(response)

def priority(report):
    system_prompt = f"""You are an AI chatbot designed to analyze emergency 
    incident reports and assign a priority level from 1 to 10, with 1 being the 
    highest priority. Your task is to evaluate each report based on the urgency,
    potential impact, and severity of the situation described. Use the following 
    priority levels to guide your analysis:

    Priority 1 - Critical: The incident poses an immediate and severe threat to 
    life or safety. Immediate action is required to prevent loss of life or major 
    harm. Examples: active shooter, severe fire, major accident with casualties.

    Priority 2 - High: The incident involves a significant threat to life or safety 
    that requires urgent attention but is not immediately critical. Examples: major 
    medical emergency without immediate risk to life, large-scale hazardous material 
    spill.

    Priority 3 - Significant: The incident poses a considerable risk to people or 
    property but does not require immediate intervention. Examples: serious but 
    non-life-threatening injury, significant property damage without immediate risk.

    Priority 4 - Elevated: The incident has a notable impact on safety or operations 
    that needs prompt attention. Examples: small fire, moderate medical issue, potential
    but unconfirmed threat.

    Priority 5 - Moderate: The incident has a moderate impact and requires attention but 
    is not urgent. Examples: minor injuries, minor property damage, general maintenance 
    issues.

    Priority 6 - Noticeable: The incident affects normal operations and requires action 
    but does not pose a significant risk. Examples: minor safety hazards, non-urgent 
    medical issues.

    Priority 7 - Low: The incident has a minimal impact on safety or operations and can 
    be addressed in due course. Examples: small technical issues, non-critical complaints.

    Priority 8 - Minor: The incident involves issues that are unlikely to affect safety 
    or operations significantly. Examples: minor annoyances, non-urgent administrative 
    issues.

    Priority 9 - Trivial: The incident has a very low impact on safety or operations and 
    does not require immediate action. Examples: minor inconveniences, routine issues.

    Priority 10 - Informational: The incident provides information or is a report 
    without any immediate action required. Examples: routine updates, non-critical 
    status reports.

    Instructions:

    Read the emergency incident report carefully.
    Assess the severity, urgency, and potential impact of the situation described in the report.
    Assign a priority level from 1 to 10 based on the descriptions above.
    Do not provide any description, simply give the priority level with no additional
    message. Here is the report: {report}"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": system_prompt
        }],
        temperature=0.8,
        max_tokens=5
    )

    return response


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

def recommended_supplies(report):
    system_prompt = f"""You are an AI assistant trained to provide 
    recommended supplies for various types of emergency incidents. Your task is 
    to analyze user-reported incidents and provide a list of supplies that emergency
    personell might need at the scene. For example, in the case of a fire, firemen
    should bring protective gear and EMS should bring supplies to treat burn
    injuries. Here is the user report:{report}"""

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

def recommended_user_action(report):
    system_prompt = f"""You are an AI assistant trained to provide 
    advice and recommendations to people in emergency situations.
    Your task is to analyze user-reported incidents and provide the most 
    suitable response based on the type and severity of the situation. Please 
    respond to the incident report by providing clear, actionable recommendations 
    to the person in distress. Be clear, and more importantly, concise in your
    action recommendations. Prioritize the safety of the individual and
    others who may be affected by the emergency situation. Keep your answer short 
    with only a few action recommendations. Here is the user report: 
    {report}"""

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
    answer = response.choices[0].message.content
    answer = answer.strip()
    
    pattern = re.compile(r'(\n\s*[\•\-\*\d\.\)\s]+[^\n]+)')

    answer = pattern.sub(lambda x: x.group(1).strip() + '\n', answer)
    
    answer = re.sub(r'(\n\s*\n)+', '\n\n', answer)

    answer = re.sub(r'\n\s*\n', '\n\n', answer)
    
    return answer

def clean_priority(priority):
    answer = priority.choices[0].message.content
    numbers = re.findall(r'\d+', answer)
    return int(''.join(numbers)) if numbers else 0