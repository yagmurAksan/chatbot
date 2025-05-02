from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Conversation
from .chatbot_classifier import classify_food

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def classify_api(request):
    conversations = Conversation.objects.all().order_by('-created_at')[:100]
    results = []

    for conversation in conversations:
        food_description = f"{conversation.question}: {conversation.answer}"
        label, scores = classify_food(food_description)
        conversation.classification_result = label
        conversation.save()
        results.append({
            'question': conversation.question,
            'answer': conversation.answer,
            'predicted_label': label,
            'scores': scores
        })

    return Response({'classified': results})
