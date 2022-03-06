import markdown
with open('input.md', 'r') as in_file:
    text = in_file.read()
    html = markdown.markdown(text)
with open('output.html', 'w') as out_file:
    out_file.write(html)
