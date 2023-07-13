import requests
from bs4 import BeautifulSoup

# Define the URL of the cybersecurity news source
news_url = "https://thehackernews.com/"

# Send a GET request to the news website and retrieve the HTML content
response = requests.get(news_url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find the relevant elements containing news articles
articles = soup.find_all("div", class_="body-post clear")

# Iterate through the articles and print the titles and summaries
for article in articles:
    title = article.find("h2", class_="home-title").text.strip()
    summary = article.find("div", class_="home-desc").text.strip()
    
    print("Title:", title)
    print("Summary:", summary)
    print()
