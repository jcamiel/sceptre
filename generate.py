#!/usr/bin/env python3
# coding: utf-8
from pathlib import Path
from markdown2 import markdown_path
from string import Template
import re


class Paragraph:

    def __init__(self, filename):
        self.src_filename = filename
        self.number = int(Path(filename).stem)
        name = str(self.number) + ".html"
        self.dst_filename = Path(filename).parent.parent.joinpath("www", name)

    def to_html(self):
        body = markdown_path(self.src_filename)
        body = self.post_process(body)

        title = self.number
        with open("template/page.html", "rt") as f:
            template = f.read()

        html = Template(template).substitute(title=title, body=body, page=self.number)
        return html

    def post_process(self, txt):
        txt = sanetize_html(txt)
        txt = re.sub('<a href="\d+">(\d+)</a>', r'<a href="\1" class="pagelink">\1</a>', txt)
        return txt

    def write_html(self):
        with open(self.dst_filename, "wt") as f:
            f.write(self.to_html())


def sanetize_html(html):
    entities = {
        "à": "&agrave;",
        "â": "&acirc;",
        "é": "&eacute;",
        "è": "&egrave;",
        "ê": "&ecirc;",
        "î": "&icirc;",
        "ô": "&ocirc;",
        "ù": "&ugrave;",
        "û": "&ucirc;",
        "'": "&rsquo;",
        "...": "&hellip;",
        " ?": "&nbsp;?",
        " :": "&nbsp;:"
    }

    for old, new in entities.items():
        html = html.replace(old, new)
    return html


def generate_book():
    for f in Path(".").glob("paragraphes/*.md"):
        p = Paragraph(filename=f)
        p.write_html()


if __name__ == "__main__":
    generate_book()
