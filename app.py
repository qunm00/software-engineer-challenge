import logging
import re

import pandas as pd


def get_wikipedia_link() -> str:
    wikipedia_link = input("Enter the Wikipedia link: ")
    # Validate the Wikipedia link
    if not re.match(r"https?://\w+\.wikipedia\.org/wiki/.*", wikipedia_link):
        raise ValueError(
            "Invalid Wikipedia link. Please provide a valid link starting with 'https://<language>.wikipedia.org/wiki/'"
        )

    return wikipedia_link


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


def extract_numerical_value(alpha_numeric: str | int | float) -> float | None:
    """
    Extract numerical value from an alpha-numeric value.

    Caveats:
    - If the string is date time, it will also be parse if the string begins with number.
    """
    if isinstance(alpha_numeric, (int, float)):
        return alpha_numeric

    match = re.match(r"([-+]?\d+\.?\d+)", alpha_numeric)
    if match:
        return float(match.group(1))

    return None


def get_numerical_column(table: pd.DataFrame) -> pd.Series | None:
    """
    Get the first numerical column in the tables from a wikipedia link.

    - Assumption:
    First row indicates the data type of the column.

    If the first row is numeric, then data type of the column is numeric.
    Thus, any following rows are not numeric, it will be dropped.

    If the first row is not numeric, then data type of the column is not numeric.
    Column will be skipped.
    """
    numeric_column = None
    for column in table.columns:
        first_row = table[column][0]
        if extract_numerical_value(first_row) is None:
            continue
        numeric_column = table[column].apply(extract_numerical_value)
        break
    if numeric_column is None:
        return None
    return numeric_column


def visualize_data(data: pd.Series):
    """
    Graph numerical data from a wikipedia page and export it to a .png file.
    """
    pass


def main():
    """
    Get the first numerical column in the tables from a wikipedia link, visualize it, and process it.
    """
    # Get Wikipedia link from user input
    wikipedia_link = get_wikipedia_link()

    # Get data from the Wikipedia link
    tables = get_tables(wikipedia_link)

    # Get numerical data
    numerical_column = None
    for table in tables:
        numerical_column = get_numerical_column(table)
        if numerical_column is not None:
            break
    if numerical_column is None:
        raise ValueError("No numerical data found")

    # Visualize the data
    visualize_data(numerical_column)


if __name__ == "__main__":
    main()
