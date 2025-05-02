from concurrent.futures import ThreadPoolExecutor, as_completed
import openai
from django.conf import settings
from .models import Conversation

client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

def chatgpt_a():
    content = "Generate a creative question asking someone's top 3 favorite foods, and encourage them to include ingredients or whether they are plant-based"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()

def chatgpt_b(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}],
        temperature=0.9,
    )
    return response.choices[0].message.content.strip()

def simulate_conversations():
    def simulate_conversation():
        try:
            question = chatgpt_a()
            answer = chatgpt_b(question)
            Conversation.objects.create(question=question, answer=answer)
        except Exception as e:
            print(f"Error simulating conversation: {e}")

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(simulate_conversation) for _ in range(100)]
        for future in as_completed(futures):
            future.result()