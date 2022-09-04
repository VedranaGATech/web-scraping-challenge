#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Set the path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# # Part 1: Scraping 
# 
# ## Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.
# 
# ###  Scrape the Mars News Site and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.
# 

# In[3]:


# Visit the NASA Mars News Site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Add time delay
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')


# In[5]:


# Assign the text to variables that you can reference later
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


# Get the news title 
#news_title = news_soup.find('div', class_='content_title').find('a').text

# Get the paragraph text
#news_p = soup.find('div', class_='article_teaser_body').text


# In[7]:


# Find the title tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[9]:


print(f"Title:\n\n{news_title}")
print("\n----------------------------------------------------------\n")
print(f"Paragraph:\n\n{news_p}")


# # JPL Mars Space Images: Featured Image

# In[10]:


#Visit the URL for the Featured Space Image site here.
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


#Use Splinter to navigate the site and find the image URL for the current Featured Mars Image
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[13]:


# find the featured image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
print(f"Featured Image: {img_url_rel}")


# In[14]:


# Assign the URL string to a variable called featured_image_url.
featured_image_url = f'https://spaceimages-mars.com/{img_url_rel}'
print(f"Featured Image URL: {featured_image_url}")


# # Mars Facts

# In[15]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head


# In[16]:


# Visit the Mars Facts webpage and use Pandas to scrape the table containing facts about the planet including diameter, mass, etc.
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[17]:


# Use Pandas to convert the data to a HTML table string.
df.to_html()


# In[18]:


facts_url = 'http://space-facts.com/mars/'

browser.visit(facts_url)

mars_facts = pd.read_html(facts_url)

mars_df = mars_facts[0]

mars_df.rename(columns={0 : "Attribute", 1 : "Value"}).set_index(["Attribute"])


# In[19]:


mars_df.to_html()


# # Mars Hemispheres

# In[20]:


# Visit the astrogeology site to obtain high-resolution images for each hemisphere of Mars.
url = 'https://marshemispheres.com/'
browser.visit(url)


# In[21]:


# You will need to click each of the links to the hemispheres in order to find the image URL to the full-resolution image.
# Append the dictionary with the image URL string and the hemisphere title to a list. 
# This list will contain one dictionary for each hemisphere.
# Save the image URL string for the full resolution hemisphere image and the hemisphere title containing the hemisphere name. 
# Use a Python dictionary to store the data using the keys img_url and title.

# Create a list to hold the images and titles
hemisphere_image_urls = []

# Retrieve the image urls and titles
for h in range(4):
    browser.links.find_by_partial_text('Hemisphere')[h].click()
    
    html = browser.html
    h_soup = soup(html,'html.parser')
    
    # Scraping
    title = h_soup.find('h2', class_='title').text
    img_url = h_soup.find('li').a.get('href')
    
    # Store images into a dictionary and append to list
    hemispheres = {}
    hemispheres['img_url'] = f'https://marshemispheres.com/{img_url}'
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
    
    # Browse back to repeat
    browser.back()

# Quit browser
browser.quit()


# In[22]:


# print(f"HEMISPHERE IMAGE URLS:\n{hemisphere_image_urls[0]}\n{hemisphere_image_urls[1]}\n{hemisphere_image_urls[2]}\n{hemisphere_image_urls[3]}")
print(f"Hemisphere Image URLs\n")
print(f"Cerberus Hemisphere Enhanced:\n{hemisphere_image_urls[0]}\n")
print(f"Schiaparelli Hemisphere Enhanced:\n{hemisphere_image_urls[1]}\n")
print(f"Syrtis Major Hemisphere Enhanced:\n{hemisphere_image_urls[2]}\n")
print(f"Valles Marineris Hemisphere Enhanced:\n{hemisphere_image_urls[3]}")


# In[23]:


hemisphere_image_urls

