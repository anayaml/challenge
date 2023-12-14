import re

def extract_values(input_string):
    match = re.search(r'(\d+) \(seconds\) / "(.*?)" \(type\)', input_string)
    try:
        if match:
            seconds = int(match.group(1))
            planet = match.group(2)
            return seconds, planet
    except Exception as e:
        raise Exception(f"Invalid input string: {input_string}") from e