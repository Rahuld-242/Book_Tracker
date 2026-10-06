# Book Tracker

A Python project for tracking books, reading progress, and reading history.

## Project status

The current implementation focuses on the core domain model for book metadata and reading-state tracking.

## Implemented features

### Book

`Book` currently stores and validates:

- title
- author
- book type (`fiction` or `non_fiction`)
- total pages

Current validation includes:

- title and author must be strings;
- blank or whitespace-only title/author values are rejected;
- title and author are stored after trimming surrounding whitespace;
- book type is restricted to `fiction` or `non_fiction`;
- `total_pages` must be an exact positive integer.

### ReadingRecord

`ReadingRecord` represents the user's reading state for a `Book`.

A new record begins with:

- `status = "TBR"`
- `current_page = None`
- `start_date = None`
- `finish_date = None`

Implemented behaviors include:

- `start_reading()`
  - moves `TBR` to `Currently Reading`;
  - sets the current page to `0`;
  - records the start date;
  - rejects invalid repeated or terminal transitions.

- `update_progress(new_page)`
  - works only while `Currently Reading`;
  - validates page type and bounds;
  - allows backward corrections;
  - automatically marks the record `Finished` when the page reaches `book.total_pages`;
  - records the finish date on automatic completion.

- `mark_finished(finish_date=None)`
  - supports both `TBR -> Finished` and `Currently Reading -> Finished`;
  - accepts an optional supplied finish date;
  - otherwise uses the current date;
  - does not require the current page to equal the physical last page.

- `mark_dnf()`
  - works only from `Currently Reading`;
  - changes status to `DNF`;
  - preserves the last recorded page and start date;
  - leaves `finish_date` as `None`.

## Reading-state model

The current single-reading lifecycle is:

```text
TBR
 |
 v
Currently Reading
 |             |
 v             v
Finished      DNF
```

Reading progress and reading outcome are treated as separate concepts.

A reader may manually mark a book as `Finished` before the physical last page, since many editions contain previews, advertisements, appendices, or other material after the main content.

`DNF` means the reader started the book and deliberately stopped reading it. A book that was never started remains `TBR`.
