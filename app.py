import logging
import re

import pandas as pd


def get_tables(wikipedia_link: str) -> list[pd.DataFrame]:
    """
    Get tables from a wikipedia link.
    """

    # there will be cases where the table is not a table but a graph
    # e.g. https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Vietnam
    # COVID-19 cases in Vietnam is a graph, not a table but still gets parsed
    # so that, class attribute should have wikitable to filter out the tables
    try:
        tables = pd.read_html(wikipedia_link, attrs={"class": "wikitable"})
    except ValueError as error:
        logging.error(error)
        raise error

    return tables


def visualize_data(data: pd.Series):
    """
    Graph numerical data from a wikipedia page and export it to a .png file.
    """
    pass


def get_numerical_data(tables: list[pd.DataFrame]) -> pd.Series:
    """
    Get the first numerical column in the tables from a wikipedia link.
    """
    return pd.Series()


def convert_object_data_type_to_floats(data: pd.Series) -> pd.Series:
    """
    Convert the numerical data floats
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
        raise ValueError(
            "Invalid Wikipedia link. Please provide a valid link starting with 'https://<language>.wikipedia.org/wiki/'"
        )

    # Get data from the Wikipedia link
    tables = get_tables(wikipedia_link)

    # Get numerical data
    numerical_column = get_numerical_data(tables)

    # Since dtype in numerical_data is object, we need to convert it to float
    processed_data = convert_object_data_type_to_floats(numerical_column)

    # Visualize the data
    visualize_data(processed_data)


if __name__ == "__main__":
    main()
