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
