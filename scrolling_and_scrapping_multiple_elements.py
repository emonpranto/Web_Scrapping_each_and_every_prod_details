from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import requests
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.111 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get('''https://www.daraz.com.bd/products/-i223774695-s1169679637.html?c=&channelLpJumpArgs=&clickTrackInfo=query%253A%253Bnid%253A223774695%253Bsrc%253ALazadaMainSrp
%253Brn%253Ab0598c170b6ccc29fe430dc8116bf221%253Bregion%253Abd%253Bsku%253A223774695_BD%253Bprice%253A1190%253Bclient%253Adesktop%253Bsupplier_id%253A700508262159%253Bbiz_s
ource%253Ahp_categories%253Bslot%253A14%253Butlog_bucket_id%253A470687%253Basc_category_id%253A20000420%253Bitem_id%253A223774695%253Bsku_id%253A1169679637%253Bshop_id%253A
138226%253BtemplateInfo%253A&freeshipping=0&fs_ab=1&fuse_fs=&lang=en&location=Dhaka&price=1.19E%203&priceCompare=skuId%3A1169679637%3Bsource%3Alazada-search-voucher%3Bsn%3A
b0598c170b6ccc29fe430dc8116bf221%3BoriginPrice%3A119000%3BdisplayPrice%3A119000%3BsinglePromotionId%3A-1%3BsingleToolCode%3AmockedSalePrice%3BvoucherPricePlugin%3A0%3Btimes
tamp%3A1737886052955&ratingscore=4.2&request_id=b0598c170b6ccc29fe430dc8116bf221&review=4&sale=22&search=1&source=search&spm=a2a0e.searchlistcategory.list.14&stock=1''')

height = driver.execute_script('return document.body.scrollHeight')


while True:
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
    time.sleep(0.2)

    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height==height:
        break
    height=new_height

# for i in range(0,height,40):
#     driver.execute_script(f'window.scrollBy(0,{i});')
#     time.sleep(0.1)

contents = driver.find_elements(By.CLASS_NAME,'content')
rating = driver.find_element(By.XPATH,'//*[@id="module_product_review_star_1"]/div/a[1]').text
question_answered = driver.find_element(By.XPATH,'//*[@id="module_product_review_star_1"]/div/a[2]').text
prod_img = driver.find_element(By.XPATH, '//*[@id="module_item_gallery_1"]/div/div[1]/div/img')
img_url =prod_img.get_attribute('src')
img = requests.get(img_url)

print(img_url)

if img.status_code==200:
    img_name = img_url.split('/')[-1]
    os.makedirs('images', exist_ok=True)

    with open(f'images/{img_name}', 'wb') as file:
        file.write(img.content)

    print(f"Succesfully downloaded the image {img_name}")

else :
    print("Failed image download.")

prod_name = driver.find_element(By.CSS_SELECTOR, '#module_product_title_1 > div > div > h1').text
prod_descrip = driver.find_element(By.CSS_SELECTOR, '#module_product_detail > div > h2').text
price = driver.find_element(By.CSS_SELECTOR, '#module_product_price_1 > div > div > div > span.notranslate.pdp-price.pdp-price_type_deleted.pdp-price_color_lightgray.pdp-price_size_xs').text
dis_price = driver.find_element(By.CSS_SELECTOR, '#module_product_price_1 > div > div > span').text
print(f'The price of the product is: ',price)
print(f'Discount price is: ',dis_price)
print(f'The name of the product is: ',prod_name)
print('The description of the product is: ', prod_descrip)

print(f'rating is: ' ,rating)


for comment in contents:
    print(comment.text)

driver.quit()