import requests
from bs4 import BeautifulSoup

def scrape_headlines(url, output_file="headlines.txt"):
    # Step 1: Fetch the webpage
    response = requests.get(url)
    response.raise_for_status()  # Ensure the request was successful

    # Step 2: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Find headline tags (h1, h2, h3)
    headline_tags = soup.find_all(["h1", "h2", "h3"])

    # Step 4: Extract text and remove duplicates/empty lines
    headlines = []
    for tag in headline_tags:
        text = tag.get_text().strip()
        if text and text not in headlines:
            headlines.append(text)

    # Step 5: Save headlines to file with numbering
    with open(output_file, "w", encoding="utf-8") as f:
        for i, line in enumerate(headlines, start=1):
            f.write(f"{i}. {line}\n")

    print(f"✔ Saved {len(headlines)} headlines to {output_file}")

# --- Main Execution ---
if __name__ == "__main__":
    # Replace this URL with the news website you want to scrape
    url = "https://www.bbc.com/news"
    scrape_headlines(url)
