# -*- coding: utf-8 -*-


class ArticleScraper():
    
    from ArticleLink import ArticleLink
    
    def __init__(self, link: ArticleLink)->None:
        
        self.link = link
        return 
    
    def getArticles(self):
        
        #import os 
        import re
        import requests
        #import xml.etree.cElementTree as ET

        from lxml import html
        from Article import Article
        
            
        
            
        overview = requests.get(self.link.link)
        overview_tree = html.fromstring(overview.content)
       
        article_links = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/a/@href')
        headlines = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/a/@title')
        pubs_and_resorts = overview_tree.xpath('//div[@id="content-main"]/div[@class="column-wide"]/ul/li/span[@class="headline-date"]/text()')
        #deleting format chars from pub_and_resort
        pubs_and_resorts = [re.sub(r"[^\S ]","",i) for i in pubs_and_resorts]
    
        data = []
        z = 0
        while (z<len(headlines)):
            data.append((re.sub("/","",headlines[z]),pubs_and_resorts[z],article_links[z]))
            z += 1
    
    
    
    
        #os.makedirs("corpus/"+d)
        
        #path="corpus/"+d+"/"
        #index = 0
        for entry in data:
            
            article_link = "http://www.spiegel.de/"+entry[2].replace(".html","-druck.html")
            
            page = requests.get(article_link)
            tree = html.fromstring(page.content)
            time_pub = tree.xpath('//div[not(@*)]/h3/text()')
            author = tree.xpath('//div[not(@*)]/h3/p[@class="author"]/a/text()')
            headline = tree.xpath('//div[not(@*)]//h2[@class="headline"]/text()')
            text = tree.xpath('//div[not(@*) and h3]/p[not(@class="author")]//text()')
            
            if len(time_pub) > 0:
                time_pub_string = re.sub(r"[^\S ]+","",time_pub[0])
            else:
                time_pub_string = ""
            
            if len(author) > 0:
                author_string = re.sub(r"[^\S ]+","",author[0])
            else:
                author_string = ""
                
            if len(headline) > 0:
                headline_string = re.sub(r"[^\S ]+","",headline[0])
            else:
                headline_string = ""
            
            text_string = ""
            for i in text:
                text_string += i
            if len(text_string) < 0:
                break
            
            yield Article(headline_string, author_string, time_pub_string,text_string, article_link,self.link.date)
            
    
