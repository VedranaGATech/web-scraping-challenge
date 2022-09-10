from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt


def scrape_all():
    executable_path = {"executable_path" : ChromeDriverManager().install()}
    browser = Browser("chrome", **executable_path, headless=False)

    news_title, news_paragraph = scrape_news(browser)

    MarsData = {
        "newsTitle" : news_title, 
        "newsParagraph" : news_paragraph,
        "featuredImage" : scrape_featured_image(browser), 
        "facts" : scrape_facts_page(browser), 
        "hemispheres" : scrape_hemispheres(browser),
        "lastUpdated" : dt.datetime.now()
    }

    browser.quit()

    #display output 
    return MarsData

def scrape_news(browser):
    
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html=browser.html
    news_soup = soup(html, 'html.parser')

    slide_elem = news_soup.select_one('div.list_text')
    # Get the news title
    news_title = slide_elem.find('div', class_='content_title').get_text()

    # Get the paragraph text
    news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    return news_title, news_p



#scrape through the feature image     
def scrape_featured_image(browser):   

    # Visit the URL for the Featured Space Image 
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    full_image_link = browser.find_by_tag('button')[1]
    full_image_link.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup (html,'html.parser')

    # Find the featured image url
    img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    # Assign the URL for featured_image_url.
    image_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return image_url

#scrape through the facts page     
def scrape_facts_page(browser):   
    url = 'https://galaxyfacts-mars.com'
    browser.visit(url)

    # Parse the resulting html with soup
    html = browser.html
    fact_soup = soup(html,'html.parser')
    

    factsLocation = fact_soup.find('div', class_='diagram mt-4')
    factsTable = factsLocation.find('table')

    facts = ""

    facts += str(factsTable)

    return facts
   

# scrape through the hempshare  
def scrape_hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    hemisphere_image_urls = []

# Clink the links and retrieve the image urls and titles
    for i in range(4):
        
        hemisphereInfo = {}
        
        browser.find_by_css('a.product-item img')[i].click()
        
        sample = browser.links.find_by_text('Sample').first
        hemisphereInfo["img_url"] = sample['href']
        
        # Title
        hemisphereInfo['title'] = browser.find_by_css('h2.title').text
        
        # Append to list
        hemisphere_image_urls.append(hemisphereInfo)   
        
        # Browse back to repeat
        browser.back()

    return hemisphere_image_urls
        

if __name__ == "__main__":
        print(scrape_all())    


