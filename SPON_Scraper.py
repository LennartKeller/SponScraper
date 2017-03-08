#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 17:40:01 2017

@author: lennart
"""

class SponScraper():
    
    
    
    def __init__(self,start_time: str,end_time: str,path: str ="corpus", headlines: bool = True)->None:
        """Dates in format: (year,month,day) --> 2002,12,31
        path is the folder where the data will be stored"""
        self.start_time = start_time
        self.end_time = end_time
        self.path = path
        self.headlines = headlines
        return
    
    
    def generateDates (self,start_time = None,end_time = None)->list:
        """Returns a list of all dates between start- and endtime as strings
        Dates in format: (year,month,day) --> 2002,12,31
        Takes dates from Counstructor if not called with arguments
        Note: if only one date is changed by argument the other date is taken from constructor"""
        
        from DateGenerator import DateGenerator
        
        return DateGenerator.generateDates(self.start_time, self.end_time)
       
    
    def dateIterator(self,start_time: str = None, end_time: str = None)->str:
        """return an iterator object with dates, same use as generateDates"""
        
        from DateGenerator import DateGenerator
        
        for date in DateGenerator.iterDates(self.start_time, self.start_time):
            
            yield date
        
        
        
    
    
    
    
    def generateLinks(self)->list:
        
        from LinkGenerator import LinkGenerator
        
        linkGenerator = LinkGenerator(self.start_time, self.end_time)
        
        links = linkGenerator.generateLinks()
        
        return links
    
    
    def getArticles(self):
        
        from ArticleScraper import ArticleScraper
        from LinkGenerator import LinkGenerator
        
        linkGenerator = LinkGenerator(self.start_time,self.end_time)
        
        
        articles = []
        for link in linkGenerator.iterLinks():
            
            articleScraper = ArticleScraper(link)
            for article in articleScraper.getArticles():
                articles.append(article)
        
        return articles
    
    def scrape(self):
        
        from XMLWriter import XMLWriter
        
        articles = self.getArticles()
        writer = XMLWriter(articles,self.path)
        writer.write()
        return
        
        
    
    
    
    
    

