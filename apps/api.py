from openai import OpenAI
import os
import json
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_bp(guideline, query):
        
    system_prompt = (
        f"You are an expert in the business plan who can help entrepreneurs formulate their business plans. Write a professional business plan based this guideline: {guideline}"
        f"Output in a JSON format that has the following keys: {guideline.keys()}"
    )

    prompt = (
        f"Current Draft: {query}\n"
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}  
    ]

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.0,
        response_format={"type": "json_object"}
    )

    answer = response.choices[0].message.content.strip()
    return json.loads(answer)

if __name__ == "__main__":
    with open('params.json', 'r') as f:
        params = json.load(f)
        sequoia_guideline = params['sequoia']
    generate_bp(sequoia_guideline, """Nutrition Coaching: An app that connects users with certified nutritionists for personalized advice, possibly through video calls or messaging.""")

