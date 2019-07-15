from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
import datetime as dt


# Create your views here.
def welcome(request):

    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    # function to convert date object to find exact day

    return render(request, 'all-news/today-news.html',{'date':date,})
def past_days_news(request,past_date):
    try:
        
    #converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(new_of_day)
    return render(request, 'all-news/past-news.html',{'date':date})