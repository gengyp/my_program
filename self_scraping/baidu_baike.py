# coding=utf-8
"""
Created on 2015-09-04 @author: Eastmount
"""

import time
import re
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

#Open PhantomJS
driver = webdriver.PhantomJS(executable_path="/Users/gengyanpeng/Applications/phantomjs-2.1.1-macosx/bin/phantomjs")
#driver = webdriver.Firefox()
wait = ui.WebDriverWait(driver,10)

#Get the infobox of 5A tourist spots
def getInfobox(name):
    try:
        #create paths and txt files
        basePathDirectory = "E:\\Tourist_spots_5A"
        if not os.path.exists(basePathDirectory):
            os.makedirs(basePathDirectory)
        baiduFile = os.path.join(basePathDirectory,"BaiduSpider.txt")
        if not os.path.exists(baiduFile):
            info = open(baiduFile,'w')
        else:
            info = open(baiduFile,'a')

        #locate input  notice: 1.visit url by unicode 2.write files
        print name.rstrip('\n') #delete char '\n'
        driver.get("http://baike.baidu.com/")
        elem_inp = driver.find_element_by_xpath("//form[@id='searchForm']/input")
        elem_inp.send_keys(name)
        elem_inp.send_keys(Keys.RETURN)
        info.write(name.rstrip('\n')+'\n')
        #print driver.current_url
        time.sleep(5)

        #load infobox
        elem_name = driver.find_elements_by_xpath("//div[@class='basic-info']/dl/dt")
        elem_value = driver.find_elements_by_xpath("//div[@class='basic-info']/dl/dd")

        #create dictionary key-value
        elem_dic = dict(zip(elem_name,elem_value))
        for key in elem_dic:
            print key.text,elem_dic[key].text
            info.write(key.text+":"+elem_dic[key].text+'\n')
        time.sleep(5)

    except Exception,e: #'utf8' codec can't decode byte
        print "Error: ",e
    finally:
        print '\n'
        info.write('\n')

#Main function
def main():
    #By function get information
    source = open("F:\\Tourist_spots_5A.txt",'r')
    for name in source:
        name = unicode(name,"utf-8")
        if u'故宫' in name: #else add a '?'
            name = u'北京故宫'
        getInfobox(name)
    print 'End Read Files!'
    source.close()
    info.close()
    driver.close()

main()