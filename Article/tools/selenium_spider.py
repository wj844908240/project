# -*- coding: utf-8 -*-
__author__ = 'bobby'

from selenium import webdriver
from scrapy.selector import Selector

# browser = webdriver.Chrome(executable_path="D:/py/chromedriver.exe")
#
# browser.get("https://www.zhihu.com/#signin")
#
# browser.find_element_by_css_selector(".SignFlow-accountInput input[name='username']").send_keys("18382001701")
# browser.find_element_by_css_selector(".Input-wrapper input[name='password']").send_keys("wangji123@@")
#
# browser.find_element_by_css_selector(".SignFlow-submitButton").click()
#selenium 完成微博模拟登录

# browser.get("https://www.oschina.net/blog")
# import time
# time.sleep(5)
# browser.find_element_by_css_selector("#loginname").send_keys("liyao198705@sina.com")
# browser.find_element_by_css_selector(".info_list.password input[node-type='password']").send_keys("da_ge_da")
# browser.find_element_by_css_selector(".info_list.login_btn a[node-type='submitBtn']").click()

# for i in range(3):
#     browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;")
#     time.sleep(3)
# t_selector = Selector(text=browser.page_source)
# print (t_selector.css(".tm-promo-price .tm-price::text").extract())


#设置chromedriver不加载图片
# chrome_opt = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images":1}
# chrome_opt.add_experimental_option("prefs", prefs)
# browser = webdriver.Chrome(executable_path="D:/py/chromedriver.exe",chrome_options=chrome_opt)
# browser.get("https://www.taobao.com")

#phantomjs, 无界面的浏览器， 多进程情况下phantomjs性能会下降很严重
#
# browser = webdriver.PhantomJS(executable_path="E:/home/phantomjs-2.1.1-windows/bin/phantomjs.exe")
# browser.get("https://detail.tmall.com/item.htm?spm=a230r.1.14.3.yYBVG6&id=538286972599&cm_id=140105335569ed55e27b&abbucket=15&sku_properties=10004:709990523;5919063:6536025")
#
# print (browser.page_source)
# browser.quit()