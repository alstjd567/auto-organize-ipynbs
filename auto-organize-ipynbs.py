## D0529_1_what-i-learned-on-the-way.ipynb 에서
import subprocess
import shlex
from bs4 import BeautifulSoup
import glob

# folder = 'folder-of-codes'
notebooks = glob.glob('*.ipynb')  # (folder+'\*.ipynb')
notebooks2 = []
for notebook in notebooks:
    notebook = notebook.replace('\\', '/')
    notebooks2.append(notebook)
print(notebooks2)

raw_html_w = open('\combined-code.html', 'w', encoding='UTF8')  # (folder+'\combined-code.html', 'w', encoding='UTF8')

html_strs = ""
for notebook in notebooks2:
    command = "jupyter nbconvert --to html " + notebook
    subprocess.call(shlex.split(command))
    
    raw_html = open(notebook[:-6]+'.html', encoding='UTF8').read()
    parsed_html = BeautifulSoup(raw_html, 'html.parser')
    html_str = str(parsed_html.select('html')[0])
    html_strs = html_strs + html_str

raw_html_w.write(html_str_attached)
raw_html_w.close()