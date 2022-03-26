hr_style = 'style5'
code_language = '<pre class="python">'

with open('output.html', 'w', encoding='utf-8') as f:
    my_input = open('input.html', 'r', encoding='utf-8')
    lines = my_input.readlines()
    for i in range(len(lines)):
        if lines[i].startswith('<hr'):
            lines[i] = lines[i].replace('style1', hr_style)
        elif lines[i].startswith('<pre class="'):
            code_hightlight = lines[i][:lines[i].find('<code>')]
            lines[i] = lines[i].replace(code_hightlight, code_language)
    f.writelines(lines)
f.close()
