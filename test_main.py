# -*- coding: utf-8 -*-

if (__name__ == "__main__"):
    
    from Article import Article
    from ArticleScraper import ArticleScraper
    from DateGenerator import DateGenerator
    from LinkGenerator import LinkGenerator
    from SPON_Scraper import SponScraper
    from XMLWriter import XMLWriter
    
    s = SponScraper("2012,3,21","2012,5,21",path="test3")
    s.scrap()