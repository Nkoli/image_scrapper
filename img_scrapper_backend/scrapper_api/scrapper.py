import os
import psycopg2
import requests

from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

base_url = 'https://www.formpl.us'
features_url = 'https://www.formpl.us/features'
page = requests.get(features_url)

soup = BeautifulSoup(page.content, 'html.parser')


def retrieve_lazy_loaded_images():
    conn = psycopg2.connect(
        host='localhost', database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    class_links = soup.find_all('img', attrs={'class': 'b-lazy'})
    for link in class_links:
        cur.execute(
            "INSERT INTO scrapper_api_image(image_link) VALUES ('{}{}')".format(
                base_url, link.get('data-src'))
        )
        conn.commit()
    conn.close()


def retrieve_regular_loaded_images():
    conn = psycopg2.connect(
        host='localhost', database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    image_links = soup.find_all('img')
    for link in image_links:
        if "static" in link.get('src'):
            cur.execute(
                "INSERT INTO scrapper_api_image(image_link) VALUES('{}{}')".format(base_url, link.get('src')))
            conn.commit()
    conn.close()


def delete_invalid_links():
    conn = psycopg2.connect(
        host='localhost', database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM scrapper_api_image WHERE image_link LIKE 'https://www.formpl.usdata:%'")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    retrieve_lazy_loaded_images()
    retrieve_regular_loaded_images()
    delete_invalid_links()
