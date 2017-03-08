# -*- coding: utf-8 -*-


class ArticleLink():
    
    def __init__(self,link: str,date: str)->None:
        
        self.link = link
        self.date = date
        return
    
    def __str__(self)->str:
        return "Link: "+self.link+"\n"+"Abgerufen am: "+self.date
    
    def __hash__(self)->int:
        return hash(self.date)+hash(self.link)
    
    def __iter(self)->int:
        
        for i in (self.link,self.date):
            yield i
    
