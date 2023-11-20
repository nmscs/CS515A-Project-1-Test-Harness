import json
import sys
import argparse

def flatten_json(json_obj, parent_key='', separator='.'):
    flattened = {}
    for key, value in json_obj.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else key
        if isinstance(value, dict):
            flattened.update(flatten_json(value, new_key, separator=separator))
        else:
            flattened[new_key] = value
    return flattened

def gron(json_content, options):
    json_obj = json.loads(json_content)
    flattened = flatten_json(json_obj, separator=options.separator)
    result = []
    for key, value in flattened.items():
        formatted_value = json.dumps(value, indent=options.indent)
        result.append(f"{key} = {formatted_value};")
    return '\n'.join(result)

def main():
    parser = argparse.ArgumentParser(description='JSON flattening utility (gron)')
    parser.add_argument('file', nargs='?', default=None, help='File to process')
    parser.add_argument('-s', '--separator', default='.', help='Separator for keys (default is ".")')
    parser.add_argument('-i', '--indent', type=int, default=None, help='Indentation level for values')

    args = parser.parse_args()

    if args.file is None:
        # No file provided, read from stdin
        json_content = sys.stdin.read()
        result = gron(json_content, args)
        print(result)
    else:
        # File provided, read from the file
        file_path = args.file
        try:
            with open(file_path, 'r') as file:
                json_content = file.read()
                result = gron(json_content, args)
                print(result)
        except FileNotFoundError:
            print(f"gron: {file_path}: No such file or directory")

if __name__ == "__main__":
    main()
