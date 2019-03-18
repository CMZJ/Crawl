import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random

driver = webdriver.Chrome()
driver.get("http://dun.163.com/trial/sense")
time.sleep(2)
button1 = driver.find_element_by_xpath('//div[@class="m-tcapt"]/ul/li[@captcha-type="jigsaw"]')
button1.click()
time.sleep(0.1)
button2 = driver.find_element_by_css_selector("[class='tcapt-bind_btn tcapt-bind_btn--login j-bind']")
button2.click()
time.sleep(1)
img = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'yidun_bgimg')))
location = img.location
size = img.size
print(size)
#可能是电脑或者浏览器的原因，获取的位置x差了55px左右，y差了20px左右
top, bottom, left, right = location['y']+20, location['y']+20 + size['height'], location['x']+55, location['x']+55 + size['width']
print('验证码位置', top, bottom, left, right)
#截屏
screenshot = driver.get_screenshot_as_png()
screenshot = Image.open(BytesIO(screenshot))
#获取验证码图片
captcha = screenshot.crop((left, top, right, bottom))
print(left, top, right, bottom)
# 保存验证码图片
captcha.save('captcha.png')

#为了使移动速度不均匀
def get_track(distance):
    lim = int(distance / 3)
    print(lim)
    s1 = random.randint(0, lim)
    s2 = random.randint(0, lim)
    s3 = random.randint(0, lim)
    s4 = distance - s1 - s2 - s3
    print(s1)
    track = [s1, s2, s3, s4]
    return track

a = int(input("输入偏移量："))
#浏览器显示宽度为356px
#实际div尺寸可以通过size获取
distance = (a/356)*286
track = get_track(distance)
print(track)
#获取滑块对象
slider = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'yidun_slider')))
#按住不放
ActionChains(driver).click_and_hold(slider).perform()
#滑动
for i in track:
    print(i)
    time.sleep(0.1)
    ActionChains(driver).move_by_offset(xoffset=i,yoffset=0).perform()
time.sleep(1)
#对齐松开
ActionChains(driver).release().perform()
