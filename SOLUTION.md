# Solution to Detector Inspector Engineering Challenge

## Tasks

- Write a program in any language you prefer using any frameworks you feel are appropriate
- The input is a URL and the output is an image file
- The input should be a Wikipedia page such as https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression
- Your program should scan the page for a table
- Inside the table the program should identify a numeric column
- The program should then plot a graph of the values in the numeric column
- The graph should be saved as an image file which is the output

## Assumptions

- The only input user can enter to the program is a wikipedia link. Thus, user can't choose which table and which column to graph.
- First row indicates the data type of the column. If the first row is numeric, then data type of the column is numeric. Thus, any following rows are not numeric, it will be dropped. If the first row is not numeric, then data type of the column is not numeric. Column will be skipped.

## Usage

- Prerequisite:

  - [Poetry](https://python-poetry.org/)

- Install dependencies

```python
poetry install
```

- Run the application

```python
poetry run python app.py
```

Visualization will be saved in `visualized_data.png` in root folder.
`visualized_data.png` in `assets/` is a fixture for testing.

## Run Tests

```python
poetry run pytest test.py
```

with coverage

```python
poetry run pytest --cov-report term-missing --cov=. test.py
```

generated graph will be stored in `output/visualized_data.png`
