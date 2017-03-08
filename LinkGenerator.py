# -*- coding: utf-8 -*-

class LinkGenerator():
    
    def __init__(self, start_time: str, end_time: str)->None:
        
        self.link_overview = "http://www.spiegel.de/nachrichtenarchiv/artikel-{}.html"
        self.start_time = start_time
        self.end_time = end_time
        return
    
    def generateLinks(self)->list:
        
        
        from DateGenerator import DateGenerator
        from ArticleLink import ArticleLink
        
        Dates = DateGenerator(self.start_time,self.end_time)
        
        links = []
        
        for date in Dates.iterDates():
            links.append(ArticleLink(self.link_overview.format(date),date))
        
        return links
    
    def iterLinks(self)->str:
        
        from DateGenerator import DateGenerator
        from ArticleLink import ArticleLink
        
        Dates = DateGenerator(self.start_time,self.end_time)
        
        for date in Dates.iterDates():
            yield ArticleLink(self.link_overview.format(date),date)
        