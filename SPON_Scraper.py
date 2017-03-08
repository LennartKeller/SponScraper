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
    
    def scrap(self):
        
        from XMLWriter import XMLWriter
        
        articles = self.getArticles()
        writer = XMLWriter(articles,self.path)
        writer.write()
        return
        
        
    
    
    
    
    
    
#    import os, re
#    import xml.etree.cElementTree as ET
#    
#    from lxml import html
#    import requests
#    links_overview = ['http://www.spiegel.de/nachrichtenarchiv/artikel-{}.html'.format(date) for date in dates]
#    
#    #################
#    #get links, headlines and publishtime from overview site
#    
#    for d in dates:
#        
#        link = 'http://www.spiegel.de/nachrichtenarchiv/artikel-{}.html'.format(d)    
#        
#        overview = requests.get(link)
#        overview_tree = html.fromstring(overview.content)
#       
#        article_links = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/a/@href')
#        headlines = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/a/@title')
#        pubs_and_resorts = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/span[@class="headline-date"]/text()')
#        #deleting format chars from pub_and_resort
#        pubs_and_resorts = [re.sub(r"[^\S ]","",i) for i in pubs_and_resorts]
#    
#        data = []
#        z = 0
#        while (z<len(headlines)):
#            data.append((re.sub("/","",headlines[z]),pubs_and_resorts[z],article_links[z]))
#            z += 1
#    
#    
#    
#    
#        os.makedirs("corpus/"+d)
#        
#        path="corpus/"+d+"/"
#        index = 0
#        for entry in data:
#            
#            article_link = "http://www.spiegel.de/"+entry[2].replace(".html","-druck.html")
#            
#            page = requests.get(article_link)
#            tree = html.fromstring(page.content)
#            time_pub = tree.xpath('//div[not(@*)]/h3/text()')
#            author = tree.xpath('//div[not(@*)]/h3/p[@class="author"]/a/text()')
#            headline = tree.xpath('//div[not(@*)]//h2[@class="headline"]/text()')
#            text = tree.xpath('//div[not(@*) and h3]/p[not(@class="author")]//text()')
#            
#            if len(time_pub) > 0:
#                time_pub_string = re.sub(r"[^\S ]+","",time_pub[0])
#            else:
#                time_pub_string = ""
#            
#            if len(author) > 0:
#                author_string = re.sub(r"[^\S ]+","",author[0])
#            else:
#                author_string = ""
#                
#            if len(headline) > 0:
#                headline_string = re.sub(r"[^\S ]+","",headline[0])
#            else:
#                headline_string = ""
#            
#            text_string = ""
#            for i in text:
#                text_string += i
#            if len(text_string) < 0:
#                break
#                
#                    
#                        
#            """article_string = "Veröffentlichungszeitpunkt: {}\nAutor: {}\nÜberschrift: {}\n{}\nQuelle: {}".format(time_pub_string,author_string,headline_string,text_string,link)
#                
#              
#            f = open("articles1/article"+"_"+headline_string+"_"+time_pub_string +"_"+str(index) +".txt","w",encoding="UTF-8")
#            f.write(article_string)
#            f.close()"""
#            
#            
#            print (str(index)+". Artikel geladen.")
#            
#            
#            rootNode = ET.Element("article")
#            time_pubNode = ET.SubElement (rootNode,"published")
#            time_pubNode.text = str(entry[1])
#            time_pubNode.set("date",d)
#            
#            ET.SubElement(rootNode,"author").text = author_string
#            ET.SubElement(rootNode,"headline").text = str(entry[0])
#            ET.SubElement(rootNode,"text").text = text_string
#            ET.SubElement(rootNode,"source").text = article_link
#            tree = ET.ElementTree(rootNode)
#            tree.write(path+"article"+"_"+re.sub(" ","",str(entry[0]))+"_"+str(entry[1]) +"_"+str(index) +".xml")
#            
#            index += 1
#    
#    
#    
#    
#    
#    
#    
#    """
#    #testing
#    overview = requests.get(links_overview[0])
#    overview_tree = html.fromstring(overview.content)
#    article_links = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/a/@href')
#    headlines = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/a/@title')
#    pubs_and_resorts = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/span[@class="headline-date"]/text()')
#    
#    #deleting format chars from pub_and_resort
#    pubs_and_resorts = [re.sub(r"[^\S ]","",i) for i in pubs_and_resorts]
#    """
#    
#   