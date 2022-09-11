# Module 12: Web Scraping Challenge 

![image1](./Missions_to_Mars/images/mission_to_mars.png)  

# Mission to Mars 

Resources

    Web pages scraped:
        https://data-class-mars.s3.amazonaws.com/Mars/index.html
        https://spaceimages-mars.com
        https://galaxyfacts-mars.com
        https://marshemispheres.com/

    Programs used:
        Python
        Jupyter Notebook
        Pandas, BeautifulSoup, Splinter, ChromeDriverManager, Flask, PyMongo
        MongoDB
        HTML
        Bootstrap 


# Step 1: Scraping

Initial scraping of the above websites was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter:

    - NASA Mars News Site:
        The latest news title and the paragraph text
        Assign the text to variables that you can reference later.

    - JPL Mars Space Featured Image:
        Title and the image url for the current Featured Space image
        Use Splinter to navigate the site and find the image URL for the current Featured Mars Image, then assign the URL string to a variable called featured_image_url.

    - Mars Facts:
        Retreive Mars facts table and use Pandas to convert the data to a HTML table string

    - Mars Hemispheres:
        Title and image url of each hemisphere.
        Used Python dictionary to store the data using the keys img_url and title.

### Work Sample
 ![image](./Missions_to_Mars/images/pandas.png)    

#  Step 2: MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.


    Start by converting your Jupyter notebook into a Python script called scrape_mars.py by using a function called scrape. This function should  execute all your scraping code from above and return one Python dictionary containing all the scraped data.

    Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

    Store the return value in Mongo as a Python dictionary.

    Create a root route / that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.

    Create a template HTML file called index.html that will take the Mars data dictionary and display all the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

### Work Sample
![image1](./Missions_to_Mars/images/scrape.png)  
![image2](./Missions_to_Mars/images/mongo.png)

### Landing page ('/')

Create an initial landing page with a function button to scrape the data by calling the /scrape route. Use Bootstrap to structure your HTML template.

### Work Sample
![image3](./Missions_to_Mars/images/index.png)

### Data display ('/data')

The /scrape route redirects to a new route which renders the html template, creates the display of scraped data using Bootstrap. This page also has a 'Scrape New Data' button that calls the /scrape route again if needed.

### Work Sample
![landing_page_image](./Missions_to_Mars/images/landing.png)
