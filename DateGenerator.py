#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 21:50:23 2017

@author: lennart
"""

class DateGenerator():
    
    def __init__(self, start_time: str, end_time: str, date_format: str = "%d.%m.%Y")->None:
        """Dates in format: <year,month,day> --> 2002,12,31"""
        
        
        
        self.start_time = start_time
        self.end_time = end_time
        self.date_format = date_format
        
        return
    
    def generateDates(self)->list:
        
        from datetime import date, timedelta as td
        
        start_time_list = self.start_time.split(",")
        end_time_list = self.end_time.split(",")
        ################
        #Generating links with dates
        #==============================================================================
        # start_year = 2000
        # start_month = 1
        # start_day = 1
        # 
        # end_year = 2017
        # end_month = 1
        # end_day = 22
        # 
        #==============================================================================
        dates = []
        
        
        d1 = date(int(start_time_list[0]), int(start_time_list[1]), int(start_time_list[2]))
        d2 = date(int(end_time_list[0]), int(end_time_list[1]), int(end_time_list[2]))
        
        delta = d2 - d1
        
        for i in range(delta.days + 1):
            dates.append((d1 + td(days=i)).strftime(self.date_format))
        
        return dates
        
    
    def iterDates(self):
        
        from datetime import date, timedelta as td
        
        start_time_list = self.start_time.split(",")
        end_time_list = self.end_time.split(",")
        ################
        #Generating links with dates
        #==============================================================================
        # start_year = 2000
        # start_month = 1
        # start_day = 1
        # 
        # end_year = 2017
        # end_month = 1
        # end_day = 22
        # 
        #==============================================================================
        
        
        
        d1 = date(int(start_time_list[0]), int(start_time_list[1]), int(start_time_list[2]))
        d2 = date(int(end_time_list[0]), int(end_time_list[1]), int(end_time_list[2]))
        
        delta = d2 - d1
        
        for i in range(delta.days + 1):
            yield (d1 + td(days=i)).strftime(self.date_format)
            