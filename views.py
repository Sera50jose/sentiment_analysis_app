from django.shortcuts import render
from django.http import JsonResponse
from textblob import TextBlob

def index(request):
    return render(request, 'analysis/index.html')

def analyze(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        
        if not text.strip():
            return JsonResponse({'error': 'No text provided'}, status=400)
        
        # Analyze sentiment using TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity
        
        # Determine sentiment
        if polarity > 0.1:
            sentiment = 'positive'
            emoji = '😊'
        elif polarity < -0.1:
            sentiment = 'negative'
            emoji = '😔'
        else:
            sentiment = 'neutral'
            emoji = '😐'
        
        return JsonResponse({
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'emoji': emoji
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)