from selenium import webdriver
from selenium import*
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import urllib.request as urllib2


def data(cc,i): # get profile pic 
        
        r = requests.get(cc)
        print(cc)
        j=str(i)
        s = BeautifulSoup(r.text,"html.parser")
        a=(cc)
        print(a)
        p = s.find("meta",property ="og:image").attrs['content']
        with open(j+".jpg","wb") as pic:
                binary = requests.get(p).content
                pic.write(binary)
           
       
abc=input("enter the name for searching:")
username=input("enter your fb user name/or phone number/email id:")
password=input("enter your fb password")


url='http://www.facebook.com/'

driver = webdriver.Chrome(" ... enter the directory of our webdriver ...") # webdriver dir... 

driver.get(url)
driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()


time.sleep(5)
search = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div/div[3]/label/input')
search.send_keys(abc,Keys.ENTER)





i=1
while(True):
        try:
                action = webdriver.common.action_chains.ActionChains(driver)
                a=action.move_to_element_with_offset(search,132,320)
                time.sleep(3)
                a.click()
                action.click()
                action.perform()
                time.sleep(3)
        except:
                action = webdriver.common.action_chains.ActionChains(driver)
                a=action.move_to_element_with_offset(search,132,310)
                time.sleep(3)
                a.click()
                action.click()
                action.perform()
                time.sleep(3)
        
        driver.find_element_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t d2edcug0 rj1gh0hx buofh1pr g5gj957u hpfvmrgz dp1hu0rb']//"+"div"+"["+str(i)+"]"+"//div[1]//div[1]//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//span[1]//div[1]//div[1]//a[1]").click()
        print("enter the account")
        time.sleep(3)
        #------------scrap start
       
        copiedText = driver.find_element_by_class_name('sjgh65i0').text
        xxx=driver.find_element_by_css_selector('#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div > div > div.d2edcug0.cbu4d94t.j83agx80.bp9cbjyn > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.o387gat7.buofh1pr.g5gj957u.hpfvmrgz.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.rek2kq2y > div > div > div > div:nth-child(1) > div').text
        print(copiedText)
        qqq=driver.find_element_by_css_selector("#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.dp1hu0rb.cbu4d94t.j83agx80 > div > div > div.bp9cbjyn.j83agx80.cbu4d94t.d2edcug0 > div.rq0escxv.d2edcug0.ecyo15nh.hv4rvrfc.dati1w0a.tr9rh885 > div > div.rq0escxv.l9j0dhe7.du4w35lb.d2edcug0.o387gat7.buofh1pr.g5gj957u.hpfvmrgz.aov4n071.oi9244e8.bi6gxh9e.h676nmdw.aghb5jc5.rek2kq2y > div.lpgh02oy > div > div:nth-child(1) > div > div > div > div.sej5wr8e > div:nth-child(1)").text
        zz=str(i)+str(".txt")
        file_object  = open(str(zz),'w+')
        file_object.write(xxx)
        
        file_object.write(qqq)
        file_object.close()

        
        print("scraping complete")
        time.sleep(2)
        #-------------scrap end
        i = i+1
        url = driver.current_url
        print(url)
        #screenshot = driver.save_screenshot('my_screenshot.png')
        time.sleep(1)
        data(url,i)
        driver.execute_script("window.history.go(-1)") # go to previous page
        print(i)
        
f.close()
