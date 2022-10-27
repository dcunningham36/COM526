import requests
from bs4 import BeautifulSoup
import time


def create_abs_link(route):
    if route.startswith("/"):
        return f"https://www.solent.ac.uk{route}"
    return route


def link_valid(link):
    if link not in closed_list and link not in open_list and "www.solent.ac.uk" in link and link.startswith("http"):
        return True
    return False


open_list = ["https://www.solent.ac.uk"]
closed_list = []

target = "https://www.solent.ac.uk/courses/undergraduate/software-engineering-bsc"
done = False

while open_list and not done:
    print(f"Looking at: {open_list[0]}")

    try:
        response = requests.get(open_list[0])

        soup = BeautifulSoup(response.text, 'html.parser')

        links = soup.find_all('a', href=True)

        for link in links:
            url = create_abs_link(link["href"])
            if link_valid(url):
                open_list.append(url)

            if url == target:
                done = True
                print(f"found {target}!")
    except:
        print("connection error... skipping :( ")

    closed_list.append(open_list[0])
    open_list.pop(0)
    time.sleep(1)

print("done")