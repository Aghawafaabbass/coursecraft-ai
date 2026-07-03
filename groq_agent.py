import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_curriculum(topic, audience, duration, model_choice="Fast Draft (8B)"):
    model = "llama-3.1-8b-instant" if "Fast" in model_choice else "llama-3.3-70b-versatile"

    system_prompt = """You are an expert Curriculum Designer AI.
Generate a structured course curriculum in valid JSON format only — no extra text, no markdown fences.
The JSON must follow this exact structure:
{
  "weeks": [
    {
      "week_number": 1,
      "title": "string",
      "objectives": "string",
      "topics": "string",
      "exercise": "string"
    }
  ]
}"""

    user_prompt = f"""Create a {duration}-week course curriculum on the topic: "{topic}".
Target audience: {audience}.
For each week, provide a concise module title, 2-3 learning objectives, key topics covered, and one practical exercise.
Return ONLY valid JSON, no other text."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=4000,
    )

    content = response.choices[0].message.content.strip()
    if content.startswith("```"):
        content = content.strip("`")
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"weeks": [], "error": "Failed to parse AI response. Try again."}

    usage = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "model": model
    }
    return data, usage


def generate_assessments(topic, audience, weeks_data, model_choice="High Quality (70B)"):
    model = "llama-3.1-8b-instant" if "Fast" in model_choice else "llama-3.3-70b-versatile"

    weeks_summary = "\n".join(
        [f"Week {w.get('week_number')}: {w.get('title')} - {w.get('topics')}" for w in weeks_data]
    )

    system_prompt = """You are an expert Assessment Designer AI.
Generate assessments in valid JSON format only — no extra text, no markdown fences.
IMPORTANT: Each quiz option must start with the letter label like "A) option text", "B) option text", etc.
Structure:
{
  "quizzes": [
    {
      "week_number": 1,
      "question": "actual question text here",
      "options": ["A) first option", "B) second option", "C) third option", "D) fourth option"],
      "correct_answer": "A) first option"
    }
  ],
  "assignments": [{"week_number": 1, "title": "assignment title", "description": "assignment description"}],
  "grading_rubric": [{"criteria": "criteria name", "weight_percent": 25, "description": "what this measures"}]
}"""

    user_prompt = f"""Based on this curriculum for "{topic}" (audience: {audience}):
{weeks_summary}

Create: 1 quiz question per week with 4 options (A/B/C/D format), 1 assignment per week, and a 4-criteria grading rubric (weights summing to 100).
Return ONLY valid JSON."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.6,
        max_tokens=4000,
    )

    content = response.choices[0].message.content.strip()
    if content.startswith("```"):
        content = content.strip("`")
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"quizzes": [], "assignments": [], "grading_rubric": [], "error": "Failed to parse AI response."}

    usage = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "model": model
    }
    return data, usage


def generate_knowledge_graph(topic, weeks_data, model_choice="Fast Draft (8B)"):
    model = "llama-3.1-8b-instant" if "Fast" in model_choice else "llama-3.3-70b-versatile"

    weeks_summary = "\n".join(
        [f"Week {w.get('week_number')}: {w.get('title')} - {w.get('topics')}" for w in weeks_data]
    )

    system_prompt = f"""You are a Knowledge Graph extraction AI for a course on "{topic}".
Extract real concept names from the course content and return valid JSON only.

IMPORTANT RULES:
- Use REAL concept names from the topic (e.g. for Python: "Variables", "Loops", "Functions")
- Do NOT use placeholder words like "Concept", "string", "node"
- Each node must have a unique meaningful id and label
- Edges show which concept leads to or requires another

Return this exact format:
{{
  "nodes": [
    {{"id": "social_media_basics", "label": "Social Media Basics"}},
    {{"id": "content_strategy", "label": "Content Strategy"}}
  ],
  "edges": [
    {{"source": "social_media_basics", "target": "content_strategy"}}
  ]
}}
Keep to 8-12 nodes maximum."""

    user_prompt = f"""Course: "{topic}"
Weekly content:
{weeks_summary}

Extract the REAL core concepts from this specific course content and their relationships.
Return ONLY valid JSON with actual concept names, not placeholders."""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5,
        max_tokens=2000,
    )

    content = response.choices[0].message.content.strip()
    if content.startswith("```"):
        content = content.strip("`")
        if content.startswith("json"):
            content = content[4:]
    content = content.strip()

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = {"nodes": [], "edges": [], "error": "Failed to parse AI response."}

    usage = {
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
        "model": model
    }
    return data, usage