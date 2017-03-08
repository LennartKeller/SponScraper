#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:50:23 2017

@author: lennart
"""

class Article():
    
    import os
    
    def __init__(self, headline: str, author: str, pub_time: str, text: str, link: str,date: str)->None:
        
        self.headline = headline
        self.author = author
        self.pub_time = pub_time
        self.text = text
        self.link = link
        self.date = date
        return
    
    def writeTXT(self)->None:
        
        with open (self.headline+".txt", "w",encoding = "UTF-8") as f:
            f.write("\n\n".join((self.headline, self.author, self.pub_time, self.text, self.link)))
            f.close()
        return
    
    def writeXML(self)->None:
        
        import xml.etree.cElementTree as ET
        
        
        rootNode = ET.Element("article")
        time_pubNode = ET.SubElement (rootNode,"published")
        time_pubNode.text = self.pub_time
        
        
        ET.SubElement(rootNode,"author").text = self.author
        ET.SubElement(rootNode,"headline").text = self.headline
        ET.SubElement(rootNode,"text").text = self.text
        ET.SubElement(rootNode,"source").text = self.link
        tree = ET.ElementTree(rootNode)
        tree.write (self.headline+".xml")
        
        return
    
    def __str__(self)->str:
        
        return "\n\n".join((self.headline, self.author, self.pub_time, self.text, self.link))
    
    def __iter__(self)->str:
        
        for element in (self.headline, self.author, self.pub_time, self.text, self.link):
            yield element
    
    def __hash__(self)->int:
        
        return hash(self.author)+hash(self.headline)+hash(self.link)+hash(self.text)+hash(self.pub_time)
        