# Web_Scrapping_each_and_every_prod_details

### Scrapping Details: 
I have scrap each and every mendatory details of daraz product by using selenium. In this code you can learn how to scrap data from websites. There are several method to set the locator to scrap the data from the web. In this code i have use XPATH locator and CSS locator.For the comments of this site i have used the find_elements method by using CLASS_NAME to find the all comments in this website.

## Description: 
This Python script utilizes Selenium to automate the extraction of product details from a product page on Daraz Bangladesh (an e-commerce platform). The script scrapes product information such as:

-Product name
-Product description
-Price
-Discount price
-Rating
-Product image
-Product reviews/comments

## Dependencies:

-Selenium: For web scraping and interacting with the web page.
-requests: For downloading the product image.
-os: For file handling.
-time: For adding pauses in between actions to avoid overloading the server or triggering anti-scraping mechanisms.

## Output:

The product's image is saved to the "images" directory if available.
The script prints the following details:
-Product name
-Product description
-Price
-Discount price
-Rating
-Product comments 
