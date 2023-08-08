# Scrapy Web Scraping Project

This project demonstrates how to use Scrapy to scrape data from the website http://pstrial-2019-12-16.toscrape.com/browse/. The goal is to extract information about various categories, including details about artists, titles, images, dimensions, and descriptions.

## Installation

1. Clone this repository to your local machine.

```bash
git clone https://github.com/bensouiciakram/toscrape.com-scraper.git
'''

2.Navigate to the project directory :

```bash
cd toscrape.com-scaper
'''

3. Install the required dependencies using pip.

```bash
pip install scrapy
'''

## Usage

1. on the root path of the project : 

```bash
scrapy crawl infos 
'''

2. The scraped data will be saved in the output.csv file in the project directory.

## Data Fields
The spider extracts the following fields for each item:

* URL: The URL of the item's page.
* Artist: The artist's name.
* Title: The title of the item.
* Image: The URL of the item's image.
* Height: The height of the image.
* Width: The width of the image.
* Description: A description of the item.
* Categories: The categories to which the item belongs

## License
This project is licensed under the MIT License.
