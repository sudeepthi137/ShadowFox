import requests
from bs4 import BeautifulSoup

try:
    url = "https://www.shadowfox.org.in"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    unique_links = set()

    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            unique_links.add(href)

    with open("shadowfox_links.txt", "w") as file:
        for link in sorted(unique_links):
            file.write(link + "\n")

    print("Data saved successfully!")

except Exception as e:
    print("Error:", e)