from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from random import randint
import os


def update_file():
    with open('hashtags.txt') as f:
        main_list=f.read().splitlines()

    return(main_list)

def format(num):
    x=num.replace(',','')
    num=int(x)
    if num>999 and num<=999999:
        x=num%1000
        y=num//1000
        return(str(y)+'.'+str(x)[0]+'K')
    elif num>999999:
        x=num%1000000
        y=num//1000000
        return (str(y) + '.' + str(x)[0] + ' M')
    else: return (num)



br=webdriver.Chrome()
br.get('https://www.instagram.com/accounts/login/')
time.sleep(5)
br.find_element_by_name('username').send_keys('username')
br.find_element_by_name('password').send_keys('password',Keys.ENTER)
time.sleep(5)

main_list=update_file()
count=0
while True:
    try:
        br.get('https://www.instagram.com')
        time.sleep(3)
        if "Turn on" in br.page_source:
            x=br.find_element_by_class_name('mt3GC')
            a=x.find_elements_by_tag_name('button')
            a[1].click()
            time.sleep(2)
        for i in range(count,len(main_list)):
            tag=(str(main_list[i]))
            a=tag.strip()
            tag=a.lower()
            a=tag.replace(' ','')
            tag=a.replace('\n','')
            a=tag.replace('\t','')
            br.get('https://www.instagram.com/explore/tags/'+a)
            print(a)
            time.sleep(7)
            find=br.find_elements_by_xpath("//*[@class='g47SY ']")
            time.sleep(2)
            posts=find[0].text
            post=format(posts)
            print(post)
            with open('posts.txt', 'a') as f:
                x = str(post)
                f.write('%s\n' % x)

            with open('tags.txt', 'a') as f:
                x = '#'+a
                f.write('%s\n' % x)     

        time.sleep(3)

        count+=1

    except Exception as e:
        print(e)
        pass
        
    

    




