#!/usr/bin/env python3
# coding: utf-8
import csv


def sanetize(html):
    entities = {
        "&agrave;": "à",
        "&acirc;": "â",
        "&eacute;": "é",
        "&egrave;": "è",
        "&ecirc;": "ê",
        "&rsquo;": "'",
        "&ocirc;": "ô",
        "&ugrave;": "ù",
        "&ucirc;": "û",
        "&icirc;": "î",
        "&hellip;": "...",
        "<br>": "\n\n",
        "<p>": "\n\n",
        "</p>": "\n\n",
        "<i>": "",
        "</i>": "",
        "&nbsp;": "",
        "<strong> ": "",
        "</strong> ": "",
        "&quot;": "\"",
        "« ": "\"",
        " »": "\"",
        "<ul>": "\n\n",
        "<li>": "- ",
        "</li>": "\n",
        "</ul>": "\n\n",
    }

    for old, new in entities.items():
        html = html.replace(old, new)
    return html


def run():
    with open('/Users/jc/Downloads/sceptre.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            numero = row['numero']
            text = row['texte']
            filename = f'{numero}.md'
            links = row['lien'].split(',')
            links = [l for l in links if l != '0']

            # On transforme le html en texte brit
            text = sanetize(text)

            # On remplace tous les liens par des liens markdowns
            for link_raw in links:
                link_mkdown = f'[{link_raw}]({link_raw})'
                text = text.replace(link_raw, link_mkdown)

            with open(filename, "wt") as f:
                f.write(text)

if __name__ == '__main__':
    run()
