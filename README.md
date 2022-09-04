# Module 12: Web Scraping Challenge 

# Step 1: Scraping

Initial scraping of the following websites was completed using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter:

    - NASA Mars News Site:
        The latest news title
        The latest news paragraph text

    - JPL Mars Space Featured Image:
        The image url for the current Featured Space image
        The title of the current Featured Space image

    - Mars Facts:
        Retreive Mars facts table and use Pandas to convert the data to a HTML table string

    - Mars Hemispheres:
        The full-resolution image url of each hemisphere
        The title of the hemisphere name
        The above two were saved into a Python dictionary

#  Step 2: MongoDB and Flask Application

    Use MongoDB with Flask templating to create a new HTML page that displays all the information that was scraped from the URLs above.
    
    Create a root route / that will query your Mongo database and pass the Mars data into an HTML template for displaying the data.
    
    Create a template HTML file called index.html that will take the Mars data dictionary and display all the data in the appropriate HTML elements. 

## Screenshots

### Landing page ('/')

Bootstrap CSS was used to create an initial landing page with a single button to begin scraping data by calling the /scrape route.

landing-page

### Data display ('/data')

The /scrape route redirects to a /data route that renders a second html template, created to display the scraped data using Bootstrap and custom CSS. This page also has a 'Scrape New Data' button that calls the /scrape route again if needed.

data-page