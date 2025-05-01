import openai
from django.conf import settings

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

# ChatGPT A - Asks the question
def chatgpt_a():
    content = "Generate a creative question asking someone's top 3 favorite foods, and encourage them to include ingredients or whether they are plant-based"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()

# ChatGPT B - Answers the question
def chatgpt_b(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()
