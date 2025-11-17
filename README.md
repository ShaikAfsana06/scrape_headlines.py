# News Headline Scraper 📰

A Python script to automatically scrape **top headlines** from a news website and save them in a neatly formatted `.txt` file.  
This project demonstrates **web scraping** using `requests` and `BeautifulSoup` and can be used to gather trending news headlines for personal use or analysis.

---

## Features

- Scrapes main headlines from a news website (e.g., BBC News)  
- Cleans the data and removes duplicates  
- Saves headlines with **numbering** in a `.txt` file  
- Optional: Includes **links** to original articles (if using API-based version)  

---

## Tools & Libraries

- Python 3.x  
- `requests` – for fetching HTML content  
- `BeautifulSoup` (`bs4`) – for parsing HTML  

Install dependencies with:

```bash
pip install requests beautifulsoup4
