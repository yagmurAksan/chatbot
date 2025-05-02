from django.shortcuts import render
from .models import Conversation
from .chatbot_simulator import simulate_conversations

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
