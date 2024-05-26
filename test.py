import pytest


def test_should_display_no_tables_found_error_when_no_tables_are_found():
    from app import get_tables

    # Given
    wikipedia_link = "docs/Wikipedia, the free encyclopedia.html"
    expected_output = "No tables found"
    # When
    with pytest.raises(ValueError) as error:
        get_tables(wikipedia_link)
    # Then
    assert str(error.value) == expected_output


def test_should_get_tables_from_wikipedia_link():
    from app import get_tables

    # Given
    wikipedia_link = "docs/Women's high jump world record progression - Wikipedia.html"
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

    from app import get_numerical_column

    # Given
    table = pd.read_csv("docs/women_high_jump.csv")
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
    numerical_column = get_numerical_column(table)
    # Then
    assert numerical_column is not None
    assert numerical_column.equals(expected_output)


def test_should_return_none_when_no_numeric_column_is_found():
    import pandas as pd

    from app import get_numerical_column

    # Given
    table = pd.read_csv("docs/foreign_relations_macau.csv")
    # When
    numerical_column = get_numerical_column(table)
    # Then
    assert numerical_column is None
