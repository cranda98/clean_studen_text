import json
import pandas as pd
import argparse

def extract_text(json_obj):
    """Recursively extract 'text' entries from a JSON-like structure."""
    if isinstance(json_obj, dict):
        if 'text' in json_obj and isinstance(json_obj['text'], str):
            return [json_obj['text']]
        return [text for value in json_obj.values() for text in extract_text(value)]
    elif isinstance(json_obj, list):
        return [text for item in json_obj for text in extract_text(item)]
    return []

def text_change_text(row):
    """Extract and concatenate all 'text' entries from the 'parameters' column."""
    try:
        parameters = json.loads(row['parameters'])
        
        # Check for the specific event and conditions
        if row['event'] == 'TEXT_TOOL_CHANGE' and isinstance(parameters.get('args'), list):
            if isinstance(parameters['args'][0].get('text'), list):
                return ''
            
            # Extract and concatenate all 'text' entries
            raw_text = json.loads(parameters['args'][0]['text'])
            extracted_texts = extract_text(raw_text)
            return ' '.join(extracted_texts).strip()
        
    except (json.JSONDecodeError, KeyError, TypeError):
        pass
    
    return ''

def process_student_logs(input_file, output_file):
    """Process student logs to extract text and save the results."""
    df = pd.read_csv(input_file)

    # Apply the text_change_text function to each row
    df['combined_text'] = df.apply(text_change_text, axis=1)

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process student logs to extract and combine text.")
    parser.add_argument("input_file", help="Path to the input CSV file containing student logs.")
    parser.add_argument("output_file", help="Path to save the processed CSV file.")
    args = parser.parse_args()

    process_student_logs(args.input_file, args.output_file)