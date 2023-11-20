import sys
import argparse

def word_count(file_content, options):
    lines = file_content.split('\n')
    total_lines = len(lines)
    
    total_words = sum(len(line.split()) for line in lines)
    
    total_characters = sum(len(line) for line in lines)
    
    result = []
    if options.lines:
        result.append(total_lines)
    if options.words:
        result.append(total_words)
    if options.characters:
        result.append(total_characters)
    
    return tuple(result)

def main():
    parser = argparse.ArgumentParser(description='Word count utility')
    parser.add_argument('file', nargs='?', default=None, help='File to process')
    parser.add_argument('-l', '--lines', action='store_true', help='Display the number of lines')
    parser.add_argument('-w', '--words', action='store_true', help='Display the number of words')
    parser.add_argument('-c', '--characters', action='store_true', help='Display the number of characters')
    
    args = parser.parse_args()
    
    if args.file is None:
        # No file provided, read from stdin
        file_content = sys.stdin.read()
        counts = word_count(file_content, args)
        print('\t'.join(map(str, counts)))
    else:
        # File provided, read from the file
        try:
            with open(args.file, 'r') as file:
                file_content = file.read()
                counts = word_count(file_content, args)
                result_str = '\t'.join(map(str, counts))
                if args.file:
                    result_str += f'\t{args.file}'
                print(result_str)
        except FileNotFoundError:
            print(f"wc: {args.file}: No such file or directory")

if __name__ == "__main__":
    main()
