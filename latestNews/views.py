from django.shortcuts import render
from .services import TrendsNews

def home(request):
    trends_news = TrendsNews()
    news = trends_news.get_news()
    data = {
        'data': news
    }
    return render(request, 'home.html', data)
