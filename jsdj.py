from selenium import webdriver
import time
import csv
opt = webdriver.ChromeOptions()
opt.add_argument('--headless')
#设置为无头浏览器
driver = webdriver.Chrome(chrome_options=opt)
# time.sleep(5)
driver.get("https://www.jd.com/")

#编辑搜索框内容
s = input("输入要爬取的商品")

text = driver.find_element_by_class_name("text")
text.send_keys(s)

button = driver.find_element_by_class_name("button")
button.click()
time.sleep(1)

while True:
    #动态加载，执行下拉到底部脚本
    k = 1
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    #提取了书名，价格，评论数量，三个信息量
    p_name = driver.find_elements_by_xpath('//div/ul[@class="gl-warp clearfix"]/li//div[@class="p-name"]')
    p_price = driver.find_elements_by_xpath('//div/ul[@class="gl-warp clearfix"]/li//div[@class="p-price"]')
    p_comment = driver.find_elements_by_xpath('//div/ul[@class="gl-warp clearfix"]/li//div[@class="p-commit"]')
    #几个列表提取的信息数量应该相同
    print(len(p_comment),len(p_name),len(p_price))

    mid = map(list,zip(p_name,p_price,p_comment))
    for i in mid:
        name = i[0].text.strip()
        price = i[1].text.strip()
        comment = i[2].text.strip()

        with open('E:/SCRAPY/{}.csv'.format(s),'a',newline='')as f:
            writer = csv.writer(f)
            L = [name,price,comment]
            writer.writerow(L)
    print("第{}页爬取完成".format(k))
    k += 1
    #点击下一页        
    if driver.page_source.find("pn-next disabled") == -1:
        driver.find_element_by_class_name("pn-next").click()
        time.sleep(1)
    else:
        print("爬取完毕，共抓取{}页数据".format(k))
        break















