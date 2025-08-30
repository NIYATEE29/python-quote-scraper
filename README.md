# python-quote-scraper
A Python web scraper that extracts all quotes, authors, and tags from quotes.toscrape.com and saves them to a CSV file.

Features
1. Complete Data Extraction: Scrapes quote text, author names, and all corresponding tags for every entry.
2. Automated Pagination: Automatically detects and navigates through all pages of the website to ensure a comprehensive data collection.
3. Structured Output: Organizes the scraped data and saves it into a clean, well-formatted CSV file named scraped_quotes.csv for easy analysis and use.
4. Robust and Polite: Includes error handling for web requests and a delay between page loads to ensure responsible scraping practices.
   
Technologies used
1. Python
2. BeautifulSoup
3. Requests
4. CSV
5. Time
   
How to Run
1. Clone the repository
2. Install the required libraries
3. Run the script

Output
After the script successfully finishes running, a file named scraped_quotes.csv will be created in the same directory. This file will contain all the quotes scraped from the website, with columns for text, author, and tags.
