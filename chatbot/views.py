from django.shortcuts import render
from concurrent.futures import ThreadPoolExecutor, as_completed
from .models import Conversation
from .chatbot_simulator import simulate_conversations
from .chatbot_classifier import classify_hugging_face

def home(request):
    return render(request, 'home.html')

def simulate(request):
    error_message = None

    try:
        simulate_conversations()
    except Exception as e:
        error_message = f"An error occurred while simulating conversations: {e}"

    conversations = Conversation.objects.all().order_by('-created_at')[:100]

    return render(request, 'simulation_results.html', {'conversations': conversations, 'error_message': error_message})\

def classify_and_filter(conversation):
    food_description = f"{conversation.question}: {conversation.answer}"
    label, scores = classify_hugging_face(food_description)

    if label in ['vegan', 'vegetarian']:
        return {
            'question': conversation.question,
            'answer': conversation.answer,
            'classification_result': label,
            'scores': scores
        }
    return None

def classify(request):
    conversations = Conversation.objects.all().order_by('-created_at')[:100]
    filtered_conversations = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(classify_and_filter, conversation) for conversation in conversations]

        for future in as_completed(futures):
            result = future.result()
            if result:
                filtered_conversations.append(result)

    return render(request, 'classification_results.html', {'conversations': filtered_conversations})

def show_conversations(request):
    error_message = None

    conversations = Conversation.objects.all().order_by('-created_at')[:100]

    return render(request, 'simulation_results.html', {
        'conversations': conversations,
        'error_message': error_message
    })

def classification_results(request):
    conversations = Conversation.objects.filter(classification_result__in=['vegan', 'vegetarian']).order_by('-created_at')[:100]

    return render(request, 'classification_results.html', {'conversations': conversations})
