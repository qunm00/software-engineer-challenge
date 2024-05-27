import pytest
from unittest.mock import patch


@patch(
    "app.input",
    return_value="https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression",
)
def test_get_wikipedia_link(self):
    from app import get_wikipedia_link

    # Given
    expected_output = (
        "https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression"
    )
    # When
    wikipedia_link = get_wikipedia_link()
    # Then
    assert wikipedia_link == expected_output


@patch("app.input", return_value="not a wikipedia link")
def test_should_return_error_when_wikipedia_link_is_incorrect(self):
    from app import get_wikipedia_link

    # Given
    expected_output = "Invalid Wikipedia link. Please provide a valid link starting with 'https://<language>.wikipedia.org/wiki/'"
    # When
    with pytest.raises(ValueError) as error:
        get_wikipedia_link()
    # Then
    assert str(error.value) == expected_output


def test_should_display_no_tables_found_error_when_no_tables_are_found():
    from app import get_tables

    # Given
    wikipedia_link = "assets/Wikipedia, the free encyclopedia.html"
    expected_output = "No tables found"
    # When
    with pytest.raises(ValueError) as error:
        get_tables(wikipedia_link)
    # Then
    assert str(error.value) == expected_output


def test_should_get_tables_from_wikipedia_link():
    from app import get_tables

    # Given
    wikipedia_link = (
        "assets/Women's high jump world record progression - Wikipedia.html"
    )
    expected_output = 1
    # When
    tables = get_tables(wikipedia_link)
    # Then
    assert len(tables) == expected_output


def test_extract_numerical_value_from_alpha_numeric_value():
    from app import extract_numerical_value

    # Given
    alpha_numeric = "1.46m (4ft 9 1/2 in)"
    # When
    numeric_value = extract_numerical_value(alpha_numeric)
    # Then
    assert numeric_value == 1.46

    # Given
    alpha_numeric = "46%"
    # When
    numeric_value = extract_numerical_value(alpha_numeric)
    # Then
    assert numeric_value == 46

    # Given
    alpha_numeric = "46"
    # When
    numeric_value = extract_numerical_value(alpha_numeric)
    # Then
    assert numeric_value == 46

    # Given
    alpha_numeric = 46
    # When
    numeric_value = extract_numerical_value(alpha_numeric)
    # Then
    assert numeric_value == 46

    # Given
    alpha_numeric = 46.0
    # When
    numeric_value = extract_numerical_value(alpha_numeric)
    # Then
    assert numeric_value == 46


def test_should_return_the_first_column_with_numeric_data():
    import pandas as pd

    from app import get_numerical_column_from_a_table

    # Given
    table = pd.read_csv("assets/women_high_jump.csv")
    expected_output = pd.Series(
        [
            1.460,
            1.485,
            1.485,
            1.524,
            1.552,
            1.580,
            1.580,
            1.595,
            1.605,
            1.620,
            1.650,
            1.650,
            1.660,
            1.660,
            1.660,
            1.710,
            1.720,
            1.730,
            1.740,
            1.750,
            1.760,
            1.760,
            1.770,
            1.780,
            1.800,
            1.810,
            1.820,
            1.830,
            1.840,
            1.850,
            1.860,
            1.870,
            1.880,
            1.900,
            1.910,
            1.920,
            1.920,
            1.940,
            1.940,
            1.950,
            1.960,
            1.960,
            1.970,
            1.970,
            2.000,
            2.010,
            2.010,
            2.020,
            2.030,
            2.030,
            2.040,
            2.050,
            2.070,
            2.070,
            2.080,
            2.090,
        ]
    )
    # When
    numerical_column = get_numerical_column_from_a_table(table)
    # Then
    assert numerical_column is not None
    assert numerical_column.equals(expected_output)


def test_should_return_the_first_column_with_numeric_data_but_there_a_some_nan_data():
    import pandas as pd

    from app import get_numerical_column_from_a_table

    # Given
    table = pd.read_csv("assets/table_with_nan.csv")
    expected_output = pd.Series([1.460, 1.485, 1.840])
    # When
    numerical_column = get_numerical_column_from_a_table(table)
    # Then
    assert numerical_column is not None
    assert numerical_column.equals(expected_output)


def test_column_with_first_row_non_numeric_is_not_identified_as_numeric():
    import pandas as pd

    from app import get_numerical_column_from_a_table

    # Given
    table = pd.read_csv("assets/table_with_first_column_not_numeric.csv")
    # When
    numerical_column = get_numerical_column_from_a_table(table)
    # Then
    assert numerical_column is None


def test_should_return_none_when_no_numeric_column_is_found_in_a_table():
    import pandas as pd

    from app import get_numerical_column_from_a_table

    # Given
    table = pd.read_csv("assets/foreign_relations_macau.csv")
    # When
    numerical_column = get_numerical_column_from_a_table(table)
    # Then
    assert numerical_column is None


def test_should_return_numeric_column_when_it_is_found_from_a_list_of_tables():
    import pandas as pd
    from app import get_tables, get_numerical_data_from_a_list_of_tables

    # Given
    tables = get_tables(
        "assets/Women's high jump world record progression - Wikipedia.html"
    )
    expected_output = pd.Series(
        [
            1.460,
            1.485,
            1.485,
            1.524,
            1.552,
            1.580,
            1.580,
            1.595,
            1.605,
            1.620,
            1.650,
            1.650,
            1.660,
            1.660,
            1.660,
            1.710,
            1.720,
            1.730,
            1.740,
            1.750,
            1.760,
            1.760,
            1.770,
            1.780,
            1.800,
            1.810,
            1.820,
            1.830,
            1.840,
            1.850,
            1.860,
            1.870,
            1.880,
            1.900,
            1.910,
            1.920,
            1.920,
            1.940,
            1.940,
            1.950,
            1.960,
            1.960,
            1.970,
            1.970,
            2.000,
            2.010,
            2.010,
            2.020,
            2.030,
            2.030,
            2.040,
            2.050,
            2.070,
            2.070,
            2.080,
            2.090,
        ]
    )
    # When
    numerical_column = get_numerical_data_from_a_list_of_tables(tables)
    # Then
    if numerical_column is None:
        assert False
    numerical_column.equals(expected_output)


def test_should_return_none_when_no_numeric_column_is_found_from_a_list_of_tables():
    from app import get_tables, get_numerical_data_from_a_list_of_tables

    # Given
    tables = get_tables("assets/Foreign relations of Macau - Wikipedia.html")
    expected_output = "No numerical data found"
    # When
    with pytest.raises(ValueError) as error:
        get_numerical_data_from_a_list_of_tables(tables)
    # Then
    assert str(error.value) == expected_output


def test_should_not_generate_graph_if_there_is_no_data(image_diff):
    import pandas as pd
    from app import visualize_data
    import os

    # Clean up existing test files
    if os.path.exists("output/visualized_data.png"):
        os.remove("output/visualized_data.png")

    # Given
    numerical_column = None
    # When
    visualize_data(numerical_column)
    # Then
    assert os.path.exists("output/visualized_data.png") is False

    # Given
    numerical_column = pd.Series()
    # When
    visualize_data(numerical_column)
    # Then
    assert os.path.exists("output/visualized_data.png") is False


def test_generated_graph(image_diff):
    import pandas as pd
    from app import get_numerical_column_from_a_table, visualize_data
    import os

    # Clean up existing test files
    if os.path.exists("output/visualized_data.png"):
        os.remove("output/visualized_data.png")

    # Given
    table = pd.read_csv("assets/women_high_jump.csv")
    # When
    numerical_column = get_numerical_column_from_a_table(table)
    visualize_data(numerical_column, "output/")
    image1 = "output/visualized_data.png"
    # Then
    image2 = "assets/visualized_data.png"
    assert image_diff(image1, image2)
