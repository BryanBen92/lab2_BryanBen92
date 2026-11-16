#!/bin/bash
# organizer.sh: archives grades.csv with a timestamp, resets it, and logs the action.

ARCHIVE_DIR="archive"
ORIGINAL="grades.csv"
LOG_FILE="organizer.log"

# 1. Create the archive directory if it does not exist
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created directory: $ARCHIVE_DIR"
fi

# 2. Make sure there is a file to archive
if [ ! -f "$ORIGINAL" ]; then
    echo "Error: $ORIGINAL was not found in $(pwd). Nothing to archive."
    exit 1
fi

# 3. Build the timestamped name, e.g. grades_20251105-170000.csv
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
ARCHIVED="grades_${TIMESTAMP}.csv"

# 4. Move the file into the archive under its new name
if ! mv "$ORIGINAL" "$ARCHIVE_DIR/$ARCHIVED"; then
    echo "Error: could not move $ORIGINAL to $ARCHIVE_DIR/$ARCHIVED."
    exit 1
fi

# 5. Reset the workspace with a new empty grades.csv
touch "$ORIGINAL"

# 6. Append the details to the log (the log accumulates across runs)
echo "[$TIMESTAMP] original: $ORIGINAL | archived as: $ARCHIVE_DIR/$ARCHIVED" >> "$LOG_FILE"

echo "Archived $ORIGINAL as $ARCHIVE_DIR/$ARCHIVED"
echo "Created a new empty $ORIGINAL"
