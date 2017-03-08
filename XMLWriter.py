# -*- coding: utf-8 -*-

class XMLWriter():
    
    from Article import Article
    
    
    def __init__(self, articles: list, path: str)->None:
        
        self.articles = articles
        self.path = path
        return
    
    def write(self):
        
        import os
        import re
        import xml.etree.cElementTree as ET
        
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        
        os.chdir(self.path)
        
        for article in self.articles:
            
            folder = article.date
            
                
            
            if not os.path.exists(folder):
                os.mkdir(folder)
            
            
            rootNode = ET.Element("article")
            rootNode.set("date",article.date)
            time_pubNode = ET.SubElement (rootNode,"published")
            time_pubNode.text = article.pub_time
            
            
            ET.SubElement(rootNode,"author").text = article.author
            ET.SubElement(rootNode,"headline").text = article.headline
            ET.SubElement(rootNode,"text").text = article.text
            ET.SubElement(rootNode,"source").text = article.link
            tree = ET.ElementTree(rootNode)
            tree.write (folder+"/"+article.headline+".xml")
            
        return
            