import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import os


def get_list(url):
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return None
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.get_text().splitlines()
    except:
        return None


def format_list(lines):
    unique_lines = set(lines)
    formatted_lines = []
    for line in unique_lines:
        parts = line.split()
        # check if line starts with an IP
        if len(parts) == 2 and parts[0].count(".") == 3:
            formatted_lines.append(f"0.0.0.0 {parts[1]}")
        else:
            formatted_lines.append(line)
    return formatted_lines


def write_to_file(file, lines, header=None):
    with open(file, "a") as f:
        if header:
            f.write(f"# {header}\n")
        for line in lines:
            f.write(f"{line}\n")


def process_url(url, urls):
    lines = get_list(url)
    if not lines:
        with open("broken-urls.txt", "a") as f:
            f.write(f"{url}\n")
        urls.remove(url)
        return
    formatted_list = format_list(lines)
    write_to_file("adlists.list", formatted_list, header=url)


def main():
    with open("url.list") as f:
        urls = [url.strip() for url in f.readlines()]

    with Pool(2) as p:
        p.starmap(process_url, [(url, urls) for url in urls])

    with open("url.list", "w") as f:
        for url in urls:
            f.write(f"{url}\n")



if __name__ == "__main__":
    if os.path.isfile('adlists.list'):
        os.remove("adlists.list")

    with open("broken-urls.txt", "w") as f:
        f.write("")
    main()
