"""
Definition of models.
"""

from django.db import models

class Article:
    def __init__(self,date=None,data_list=[]):
        self.date=date   
        self.data_list=data_list

class ArticleData:
    def __init__(self,headline=None,link=None):
        self.headline=headline
        self.link=link



    

