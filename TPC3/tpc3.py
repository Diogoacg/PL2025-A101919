import re
import sys

def markdown_to_html(input_lines):
    output = []
    in_list = False
    in_ulist = False
    in_code_block = False
    in_table = False
    list_stack = []

    for line in input_lines:
        stripped = line.rstrip()

        # Check for code block
        if stripped.startswith("```"):
            if in_code_block:
                output.append("</pre>")
                in_code_block = False
            else:
                output.append("<pre>")
                in_code_block = True
            continue

        if in_code_block:
            output.append(stripped)
            continue

        # Check for headers
        header_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if header_match:
            if in_list:
                output.append('</ol>')
                in_list = False
            if in_ulist:
                output.append('</ul>')
                in_ulist = False
            if in_table:
                output.append('</table>')
                in_table = False
            level = len(header_match.group(1))
            content = process_inline(header_match.group(2))
            output.append(f'<h{level}>{content}</h{level}>')
            continue

        # Check for ordered list items
        list_match = re.match(r'^(\d+)\.\s+(.*)', stripped)
        if list_match:
            content = process_inline(list_match.group(2))
            if not in_list:
                output.append('<ol>')
                in_list = True
            output.append(f'<li>{content}</li>')
            continue
        else:
            if in_list:
                output.append('</ol>')
                in_list = False

        # Check for blockquote
        blockquote_match = re.match(r'^>\s+(.*)', stripped)
        if blockquote_match:
            content = process_inline(blockquote_match.group(1))
            output.append(f'<blockquote>{content}</blockquote>')
            continue

        # Check for horizontal rules
        if re.match(r'^-{3,}$', stripped) or re.match(r'^\*{3,}$', stripped) or re.match(r'^_{3,}$', stripped):
            output.append('<hr>')
            continue

        # Check for table rows
        if re.match(r'^\|.*\|$', stripped):
            if not in_table:
                output.append('<table>')
                in_table = True
            row = '<tr>' + ''.join(f'<td>{process_inline(cell.strip())}</td>' for cell in stripped.split('|')[1:-1]) + '</tr>'
            output.append(row)
            continue
        else:
            if in_table:
                output.append('</table>')
                in_table = False

        # Process other lines (ignoring empty lines)
        if stripped:
            processed_line = process_inline(stripped)
            output.append(f'{processed_line}<br>')

    # Close any remaining open list or table
    if in_list:
        output.append('</ol>')
    if in_ulist:
        output.append('</ul>')
    if in_table:
        output.append('</table>')

    return '\n'.join(output)

def process_inline(text):
    # Order matters: process images before links, then bold, then italic
    text = re.sub(r'!\[([^\]]*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', text)
    text = re.sub(r'\[([^\]]*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
    text = re.sub(r'~~(.*?)~~', r'<del>\1</del>', text)
    text = re.sub(r'<u>(.*?)</u>', r'<u>\1</u>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\|', r'&#124;', text)  # Escape pipe characters in tables
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python tpc3.py input.md")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r', encoding='utf-8') as f:
        input_lines = f.readlines()

    html_output = markdown_to_html(input_lines)
    #open html file in browser
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(html_output)
    

if __name__ == '__main__':
    main()