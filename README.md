# Process Student Logs

This script processes student logs from a CSV file, extracting and organizing specific text entries from JSON-like structures within the log data. It is particularly useful for educational or research scenarios where text analysis is required to understand user interactions or event sequences.

## Features
- **Event Filtering**: Focuses on specific events such as `TEXT_TOOL_CHANGE` to isolate relevant data.
- **Text Extraction**: Recursively extracts all `text` entries from JSON-encoded parameters.
- **Data Enrichment**: Adds a `combined_text` column to the output, consolidating extracted text for easier analysis.
- **Customizable Output**: Saves the processed data to a user-specified CSV file for further use.

## Requirements
- Python 3.x
- Libraries: `pandas`, `argparse`

Install dependencies via pip:
```bash
pip install pandas
```

## Usage
### Command-Line Interface
Run the script from the command line with the following syntax:

```bash
python process_student_logs.py <input_file> <output_file>
```

### Arguments
- `<input_file>`: Path to the input CSV file containing student logs.
- `<output_file>`: Path to save the processed CSV file.

### Example
```bash
python process_student_logs.py student_logs.csv processed_logs.csv
```

This processes `student_logs.csv` and saves the output to `processed_logs.csv`.

### Functions
1. **`extract_text(json_obj)`**
   - Recursively extracts all `text` entries from a JSON-like object (dictionaries, lists, etc.).

2. **`text_change_text(row)`**
   - Processes each row of the input DataFrame to extract and concatenate `text` entries based on specific conditions, particularly for `TEXT_TOOL_CHANGE` events.

3. **`process_student_logs(input_file, output_file)`**
   - Main function that:
     1. Loads the input CSV file.
     2. Applies the `text_change_text` function to enrich data.
     3. Saves the results to the specified output file.
