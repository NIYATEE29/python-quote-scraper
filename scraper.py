import requests
from bs4 import BeautifulSoup
import csv
import time

base_url = "http://quotes.toscrape.com"
next_page_url = "/"


all_quotes_data = []

while next_page_url:
    current_url = base_url + next_page_url
    print(f"Scraping page: {current_url}")
    
    response = requests.get(current_url)

    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code} for URL {current_url}")
        break

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    quote_elements = soup.select(".quote")

    if not quote_elements and not all_quotes_data:
        print("No quotes found on the first page. Exiting.")
        break

    for quote_element in quote_elements:
        text = quote_element.select_one(".text").get_text(strip=True)
        author = quote_element.select_one(".author").get_text(strip=True)
        tag_elements = quote_element.select(".tag")
        tags = [tag.get_text(strip=True) for tag in tag_elements]
        
        all_quotes_data.append({
            "text": text,
            "author": author,
            "tags": ", ".join(tags)
        })

    next_button = soup.select_one("li.next > a")
    
    if next_button:
        next_page_url = next_button['href']
    else:
        print("No more pages found. Scraping complete.")
        next_page_url = None
    time.sleep(1)

if all_quotes_data:
    filename = "scraped_quotes.csv"
    print(f"\nSaving {len(all_quotes_data)} quotes to {filename}...")
    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["text", "author", "tags"])
        writer.writeheader()
        writer.writerows(all_quotes_data)

    print(f"Successfully saved quotes to {filename}")
else:
    print("\nNo quotes were scraped.")

