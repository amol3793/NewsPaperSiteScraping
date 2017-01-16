"""
Definition of views.
"""
from models import Article,ArticleData
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

import requests
from bs4 import BeautifulSoup, SoupStrainer
import urllib2
import re
import pymongo
from app.forms import BootstrapUserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


#connected mlab account for mongodb
MONGODB_URI = 'mongodb://amol:123456789@ds111479.mlab.com:11479/article'

client = pymongo.MongoClient(MONGODB_URI)
db = client.get_default_database()
article_db=db['article']




def get_news(request,day):
    """   According to selected dropdown date this view will be invoked   """

    news=article_db.find({'date' :day+"-01-2017"})
    news_cursor_data=[article for article in news][0]
    return render(
        request,
        'app/article.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'news_data':news_cursor_data['data_list'][1:-1],
            'news_date':news_cursor_data['date']
                       
        })
    )




@login_required
def home(request):
    """Renders the home page."""
    
    start_loop_date=9
    article_list=[]
    for loop_date in range(start_loop_date,start_loop_date+5):
        article=Article()
        url = 'http://www.thehindu.com/archive/print/2017/01/'+str(loop_date)+'/'
        article.date=str(loop_date)+'-01-2017'
        html=urllib2.urlopen( url ).read()
        soup = BeautifulSoup(html)    
        data = soup.find("ul",{"class":"archive-list"})
        article_header_list=data.text.encode('utf-8').split('\n\n\n')
        article_link_list=[i.find('a').get('href') for i in data.find_all('li')]
        
        article_data_list=zip(article_header_list,article_link_list)
        #for article_data in article_data_list:
        #    article_data=ArticleData(*article_data)
        #    article.data_list.append(article_data)
        #article_list.append(article)
        if '13-01-2017' not in [i['date'] for i in article_db.find()]:
            article_db.insert_one({'date':article.date,
                                       'data_list':article_data_list
                                        })
         
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'article_list':article_data_list[1:-1]
            #'title':title,
            #'text':text

        })
    )


def auth_view(request):
    username=request.POST.get('username','')
    password=request.POST.get('password','')
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        user.is_authenticated=True
        return HttpResponseRedirect('/home',{'user':user})
    else:
        return HttpResponseRedirect('/login')
 



def register_view(request):
    if request.method=='POST':
        form=BootstrapUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registersuccess')
    args={}
    args.update(csrf(request))
    args['form']=BootstrapUserCreationForm()

    return render_to_response('app/register.html',args)


def register_success_view(request):
    return render_to_response('app/registersuccess.html')


