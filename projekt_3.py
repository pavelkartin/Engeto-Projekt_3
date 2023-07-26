"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Pavel Kartin
email: pevelkartin@seznam.cz
discord: capitan_alex
"""

from bs4 import BeautifulSoup as bs
import requests
import re
import pandas as pd
import argparse
import os


def main(url: str, output_file: str) -> None:
    """
    Hlavní funkce, která provádí celý proces získávání dat z zadané URL a jejich ukládání do CSV souboru.
    """
    def load_page(page_url: str) -> bs:
        """
        Načte stránku pomocí požadavku GET a převede ji na objekt BeautifulSoup.
        """
        r = requests.get(page_url).text
        return bs(r, html_parser)

    def get_rows_with_values(web_page_soup: bs) -> list:
        """
        Získá řádky s hodnotami ze stránky pomocí BeautifulSoup.
        """
        rows_list = []
        rows = web_page_soup.find_all("tr")
        # Remove empty rows
        for row in rows:
            if row.find("td", class_="overflow_name") is not None:
                rows_list.append(row)
        return rows_list

    # Konstanty
    html_parser = "lxml"
    base_url = "https://volby.cz/pls/ps2017nss/"
    headers_pattern = re.compile(r".*sa2.*sb3")  # Shoda s jakýmkoli řetězcem, který má kdekoli "sa2" a "sb3"

    # Definování CSV
    district_data = []
    code_column = "Code"
    name_column = "Location"
    registered_column = "Registered"
    envelopes_column = "Envelopes"
    valid_column = "Valid"

    # [ ZÍSKÁNÍ DAT ]
    print("Loading data...")
    district_page = load_page(url)
    municipalities_table = get_rows_with_values(district_page)

    # Sledování průběhu
    total_municipalities = len(municipalities_table)
    completed_municipalities = 0

    # Získání dat z každé obce
    for municipality in municipalities_table:
        municipality_data = {}

        # Získání kódu a názvu
        municipality_data[code_column] = municipality.find("td", class_="cislo").text
        municipality_data[name_column] = municipality.find("td", class_="overflow_name").text

        # Získání dat o hlasování
        link = base_url + municipality.find("a")["href"]
        municipality_page = load_page(link)

        municipality_data[registered_column] = municipality_page.find("td", headers="sa2").text
        municipality_data[envelopes_column] = municipality_page.find("td", headers="sa5").text
        municipality_data[valid_column] = municipality_page.find("td", headers="sa6").text

        # Získat data pro každého kandidáta
        votes_table = get_rows_with_values(municipality_page)
        for political_party in votes_table:
            party_name_column = political_party.find("td", class_="overflow_name").text
            valid_votes_number = int(political_party.find("td", headers=headers_pattern).text.replace("\xa0", ""))
            municipality_data[party_name_column] = valid_votes_number

        district_data.append(municipality_data)

        # Po získání všech dat pro obec, inkrementace čítače
        completed_municipalities += 1
        percentage_completion = (completed_municipalities / total_municipalities) * 100
        print(f"{percentage_completion:.2f}%")

    # [ ULOŽENÍ ZÍSKANÝCH DAT DO CSV ]
    data_frame = pd.DataFrame(district_data)
    data_frame.to_csv(output_file, index=False, encoding="utf-8")

    print(f"Data saved to {output_file}")


if __name__ == "__main__":
    while True:
        try:
            # Přidání argumentů
            parser = argparse.ArgumentParser(description="Scrap data from given URL and save it to a CSV file.")
            parser.add_argument('url', type=str, help="URL to scrap data from")
            parser.add_argument('output_file', type=str, help="Output CSV file name")

            args = parser.parse_args()

            # Zkontroluje, zda zadané URL začíná očekávanou základní URL
            if not args.url.startswith("https://volby.cz/pls/ps2017nss/"):
                raise ValueError("URL must start with 'https://volby.cz/pls/ps2017nss/'")

            # Zkontrolujte, zda název výstupního souboru má příponu .csv
            if not args.output_file.lower().endswith(".csv"):
                raise ValueError("Output file must be a .csv file")

            # Zkontrolujte, zda výstupní soubor již existuje
            if os.path.isfile(args.output_file):
                overwrite = input(
                    f"File '{args.output_file}' already exists. Do you want to overwrite it? (yes/no) ")
                if overwrite.lower() != "yes":
                    print("Please, try again...")
                    continue

            main(args.url, args.output_file)
            break

        # Pokud dojde k chybě v bloku try, spustí se tento blok except
        except Exception as e:
            print(f"ERROR: {e}")
            print("Please, try again...")
