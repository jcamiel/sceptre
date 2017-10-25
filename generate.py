#!/usr/bin/env python3
# coding: utf-8
from pathlib import Path
from markdown2 import markdown_path


class Page:

    def __init__(self, filename):
        self.src_filename = filename

        name = Path(filename).stem + ".html"
        self.dst_filename = Path(filename).parent.joinpath("output", name)

    def to_html(self):
        html = markdown_path(self.src_filename)
        html = escape_accents(html)
        return html

    def write_html(self):
        with open(self.dst_filename, "wt") as f:
            f.write(self.to_html())


def escape_accents(html):
    entities = {
        "à": "&agrave;",
        "é": "&eacute;",
        "è": "&egrave;",
        "ê": "&ecirc;",
        }

    for old, new in entities.items():
        html = html.replace(old, new)
    return html


def generate_book():

    for f in Path(".").glob("*.md"):
        p = Page(filename=f)
        p.write_html()


if __name__ == "__main__":
    generate_book()
