# Lab 2: ALU Transcript Generator

A Python application that calculates a student's final academic standing from a CSV of course grades, plus a Bash script that archives the grades file and logs the action. Built for the Introduction to Python Programming and Databases course at African Leadership University (BSE Year 1, Trimester 2).

## Files

| File | Purpose |
|---|---|
| `grade-evaluator.py` | Reads a grades CSV, validates it, and prints the GPA, PASSED/FAILED status and resubmission options |
| `organizer.sh` | Archives `grades.csv` with a timestamp, creates a fresh empty `grades.csv`, and logs the action |
| `grades.csv` | The course grades data |
| `tests/` | Test CSVs: six scenarios from the provided transcript (`v1` to `v6`) and three error cases |

No external libraries are used. The Python script only imports `csv`, `sys` and `os` from the standard library.

## CSV format

```
assignment,group,score,weight
Quiz,Formative,85,20
```

- `group` must be `Formative` or `Summative`.
- `score` is a percentage from 0 to 100.
- `weight` is the assignment's weight out of 100 overall.

## Running the grade evaluator

```bash
python3 grade-evaluator.py
```

Type the CSV file name when prompted, for example `grades.csv`.

### What it does

1. **Score validation:** every score must be between 0 and 100.
2. **Weight validation:** all weights must total 100, Formative must total 60 and Summative must total 40.
3. **Grade calculation:** each assignment contributes `score * weight / 100`.
4. **GPA:** `(total grade / 100) * 5.0`.
5. **Pass/Fail:** a student passes only with at least 50% in both categories. The category percentage is the points earned divided by the category weight (60 for Formative, 40 for Summative).
6. **Resubmission:** among failed Formative assignments (score below 50), the one(s) with the highest weight are eligible. If several share the highest weight, all are listed.

### Sample output

```
--- Processing Grades ---
Formative: 34.00 / 60 (56.67%)
Summative: 26.00 / 40 (65.00%)
Total Grade: 60.00 / 100
GPA: 3.0000
Status: PASSED
Eligible for resubmission (failed formative with the highest weight):
  - Group Exercise (score 40, weight 20)
  - Functions and Debugging Lab (score 45, weight 20)
```

### Error handling

| Problem | Message |
|---|---|
| File not found | `Error: The file '<name>' was not found.` |
| Score outside 0 to 100 | `Error: 'Quiz' has score 150.0, expected 0 to 100.` |
| Wrong weight totals | `Error: Total weight is 105.0, expected 100.` |
| Unknown group name | `Error: Unknown group '<name>' for '<assignment>'. Use Formative or Summative.` |
| No data rows | `Error: grades.csv has no assignment records.` |

## Testing

The six scenarios in `tests/v1.csv` to `tests/v6.csv` come from the provided transcript workbook and their results were cross-checked against it. Run all tests:

```bash
for f in tests/*.csv; do echo "=== $f"; echo "$f" | python3 grade-evaluator.py; done
```

| File | GPA | Status | Resubmission |
|---|---|---|---|
| v1 | 3.8450 | PASSED | Discussion Board |
| v2 | 3.8300 | PASSED | Discussion Board, General Quiz |
| v3 | 3.9725 | PASSED | None |
| v4 | 3.1575 | FAILED | None |
| v5 | 2.1075 | FAILED | General Quiz |
| v6 | 1.8350 | FAILED | Group Coding Lab |

## Running the organizer

```bash
bash organizer.sh
```

It will:
1. Create an `archive/` directory if it does not exist.
2. Move `grades.csv` into `archive/` as `grades_<YYYYMMDD-HHMMSS>.csv`.
3. Create a new empty `grades.csv` in the current directory.
4. Append a line to `organizer.log` with the timestamp, the original file name and the archived file name.

If `grades.csv` does not exist, it prints an error and exits with code 1.

**Warning:** this script empties `grades.csv`. Test it in a copy of the folder, and put your data back before running the Python script again.

Example `organizer.log` line:

```
[20261116-160213] original: grades.csv | archived as: archive/grades_20261116-160213.csv
```