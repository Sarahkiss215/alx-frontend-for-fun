#!/usr/bin/python3
'''
Script to changes a Markdown file to HTML
'''


import pathlib
import argparse
import re


def change_md_to_html(input_file, output_file):
    '''
    Changes markdown file to HTML file
    '''
    # Read the contents of the input file
    with open(input_file, encoding='utf-8') as f:
        md_file = f.readlines()

    html_file = []
    for line in md_file:
        # If the line is a heading
        match = re.match(r'(#){1,6} (.*)', line)
        if match:
            h_level = len(match.group(1))
            h_content = match.group(2)
            html_file.append(f'<h{h_level}>{h_content}</h{h_level}>\n')
        else:
            html_file.append(line)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(html_file)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Convert markdown to HTML')
    parser.add_argument('input_file', help='path to input markdown file')
    parser.add_argument('output_file', help='path to output HTML file')
    args = parser.parse_args()

    # If the input file exists
    input_path = pathlib.Path(args.input_file)
    if not input_path.is_file():
        print(f'Missing {input_path}', file=sys.stderr)
        sys.exit(1)

    # Change the markdown file to HTML
    change_md_to_html(args.input_file, args.output_file)
