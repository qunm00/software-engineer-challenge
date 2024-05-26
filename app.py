import re

import pandas as pd


def get_data(wikipedia_link: str) -> pd.Series:
    """
    Get the first numerical column in the tables from a wikipedia link.
    """
    return pd.Series()


def visualize_data(data: pd.Series):
    """
    Graph numerical data from a wikipedia page and export it to a .png file.
    """
    pass


def process_numerical_data(data: pd.Series) -> pd.Series:
    """
    Convert the data parsed from the wikipedia page to floats.
    """
    return pd.Series()


def main():
    """
    Get the first numerical column in the tables from a wikipedia link, visualize it, and process it.
    """
    # Get Wikipedia link from user input
    wikipedia_link = input("Enter the Wikipedia link: ")
    # Validate the Wikipedia link
    if not re.match(r"https?://\w+\.wikipedia\.org/wiki/.*", wikipedia_link):
        print(
            "Invalid Wikipedia link. Please provide a valid link starting with 'https://<language>.wikipedia.org/wiki/'"
        )

    # Get data from the Wikipedia link
    table = get_data(wikipedia_link)

    # Process the numerical data
    processed_data = process_numerical_data(table)

    # Visualize the data
    visualize_data(processed_data)


if __name__ == "__main__":
    main()
