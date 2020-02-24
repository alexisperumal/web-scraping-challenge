# UCSD Data Science Bootcamp, HW12 Mission to Mars (Web scraping and hosting)
# 
# scrape_mars.py
#
# This Python 3 script, derived from the jupyter notebook,
# mission_to_mars_splinter, scrapes several web sources on demand and puts
# the results into a local db that will be used to serve up a new page
# showing the aggregation of the content.
#
# Alexis Perumal, 2/24/20

from splinter import Browser
from bs4 import BeautifulSoup
import time
import pandas as pd
import pprint as pp

def scrape():

    d = {}

    # Mac Users
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    # !which chromedriver

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Step 1.1: Retrieve NASA Mars News
    print("Step 1.1: Mars News")
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(5)  # Give time for the browser to come up.
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    title_txt = soup.find_all('div', class_='content_title')[0].text
    print(title_txt)
    body_txt = soup.find_all('div', class_='article_teaser_body')[0].text
    print(body_txt)
    print()
    d['news'] = {'title':title_txt, 'text':body_txt}



    # Step 1.2: Retrieve JPL Space Images
    print("Step 1.2: Retrieve JPL Space Images")
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)
    # time.sleep(5)  # Give time for the browser to come up.
    soup = BeautifulSoup(browser.html, 'lxml')
    result = soup.find_all('a', class_="fancybox")
    result[1]  # result[0] is the page banner image which isn't necessarily Mars! Therefore, use the next image.
    jpg_url = 'https://www.jpl.nasa.gov' + result[1].get('data-fancybox-href')
    print(jpg_url)
    print()
    d['JPL_image_URL'] = jpg_url



    # Step 1.3: Retrieve JPL Space Images
    print("Step 1.3: Retrieve Mars Weather from Twitter")
    tweet_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(tweet_url)
    # browser.click_link_by_partial_text('Mars Weather')
    browser.links.find_by_partial_text('Mars Weather').click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    result = soup.find_all('div', class_="css-901oao r-jwli3a r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
    result[0]
    result = result[0].find('span')
    weather = result.text
    print(weather)
    print()
    d['weather'] = weather



    # Step 1.4: Mars Facts

    print("Step 1.4: Mars Facts")
    url = 'https://space-facts.com/mars/'
    mars_facts_df = pd.read_html(url)[0]
    mars_facts_html = mars_facts_df.to_html()
    print(mars_facts_df)
    print()
    d['facts_table_html'] = mars_facts_html



    # Step 1.5: Mars Hemispheres
    print("Step 1.5: Mars Hemisphers")
    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    # browser.click_link_by_partial_text('Products')
    html = browser.html
    soup = BeautifulSoup(html, 'lxml')
    hemisphere_image_urls = []
    result_list = soup.find_all('div', class_='item')

    # Get Image Titles
    for result in result_list:
        title = result.find('h3').text
        browser.links.find_by_partial_text(title).click()
        inside_result = BeautifulSoup(browser.html, 'lxml')
        img_url = "https://astrogeology.usgs.gov" + inside_result.find('img', class_='wide-image').get('src')
        browser.back()
        hemisphere_image_urls.append({'title':title, 'img_url':img_url})

    print(hemisphere_image_urls)
    print()
    d['hemispheres'] = hemisphere_image_urls


    # Step 1.final: Close the splinter-invoked browser.
    browser.quit()

    return d


if (__name__ == "__main__"):
    result = scrape()
    pp.pprint(result)
    print()
