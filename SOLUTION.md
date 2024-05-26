# Solution to Detector Inspector Engineering Challenge

## Tasks

- Write a program in any language you prefer using any frameworks you feel are appropriate
- The input is a URL and the output is an image file
- The input should be a Wikipedia page such as https://en.wikipedia.org/wiki/Women%27s_high_jump_world_record_progression
- Your program should scan the page for a table
- Inside the table the program should identify a numeric column
- The program should then plot a graph of the values in the numeric column
- The graph should be saved as an image file which is the output

## TODOs

- [ ] Write a command line interface to allow user to paste in wikipedia link
- [ ] Use Pandas' read_html() to get tables from html
  - Loop through the tables and find the first numerical column
  - Export the graph of the found numerical column

## Assumptions

- The only input user can enter to the program is a wikipedia link. Thus, user can't choose which table and which column to graph.

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

## Run Tests

```python
poetry run pytest test.py
```