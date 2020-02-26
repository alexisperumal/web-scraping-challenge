# web-scraping-challenge
UCSD Data Science Bootcamp HW 12

Scape data on Mars from multiple websites, store it in a db, and with Flask and bootstrap create a new aggregator website publishing that data.

Key Files:

* mission_to_mars-splinter.ipynb - Jupyter notebook scraping websites for Mars data. https://github.com/alexisperumal/web-scraping-challenge/blob/master/Missions_to_Mars/mission_to_mars-splinter.ipynb

* scrape_mars.py - Scraping code from mission_to_mars-splinter.ipynb converted to a standalone python splinter app. https://github.com/alexisperumal/web-scraping-challenge/blob/master/Missions_to_Mars/scrape_mars.py

* scrape_mars_output.txt - Example results from scraping sent to an output txt file through print. https://github.com/alexisperumal/web-scraping-challenge/blob/master/Missions_to_Mars/scrape_mars_output.txt

* mars_flask_app.py - Flask app running the website, providing endpoints including / and /scrape, and serving up dynamic content. https://github.com/alexisperumal/web-scraping-challenge/blob/master/Missions_to_Mars/mars_flask_app.py

* Mars Conditions Website.pdf - Printout of website to PDF file. https://github.com/alexisperumal/web-scraping-challenge/blob/master/Missions_to_Mars/Mars%20Conditions%20Website.pdf
