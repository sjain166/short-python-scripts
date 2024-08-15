import os
import requests
from bs4 import BeautifulSoup

# URL of the GitHub repository
repo_url = "https://github.com/kinshuk1312/OS-Notes-Code-Help/blob/main"

# Headers to mimic a browser request
headers = {'User-Agent': 'Mozilla/5.0'}

# Create a directory to save downloaded PDF files
download_dir = "/Users/sidpro/Desktop/Operating_Systems"
os.makedirs(download_dir, exist_ok=True)

def download_file(file_url, download_dir):
    response = requests.get(file_url, headers=headers)
    filename = file_url.split('/')[-1]
    file_path = os.path.join(download_dir, filename)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded: {filename}")

# Fetch the repository page
response = requests.get(repo_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all links ending with .pdf
pdf_links = soup.find_all('a', href=lambda href: href and href.endswith('.pdf'))

for link in pdf_links:
    file_url = "https://github.com" + link['href'].replace('/blob/', '/raw/')
    download_file(file_url, download_dir)

print("All PDF files have been downloaded.")
