# coding=utf-8
__author__ = 'Boot'

import os
import markdown_gen.MardownGen as mdg
from datetime import datetime as dt

OUTPUT_FILE = os.path.realpath(__file__)
OUTPUT_FILE = os.path.split(OUTPUT_FILE)[0]
OUTPUT_FILE = os.path.join(OUTPUT_FILE, "README.md")

str = ""

str += mdg.gen_heading("Markdown Generator for Python", 1, True)

str += mdg.gen_heading("Objective", 2, True)

str += "This is a small Python library that helps generating " + \
                mdg.gen_link("http://en.wikipedia.org/wiki/Markdown", "Markdown") + " documents."

str += mdg.gen_section()

str += mdg.gen_heading("Examples", 2, True)
str += mdg.gen_heading("Text Attributes", 3)
str += "Text can be formatted with the attributes " + mdg.gen_italic("italc") + " and " + mdg.gen_bold("bold") + ".\n"
str += "There is also " + mdg.gen_monospace("momospace text") + " or " + mdg.gen_strikethrough("striketrough") + ".\n"


str += mdg.gen_section()
str += mdg.gen_heading("Features", 2, True)


features = [
    ["Feature",         "Implemented",      "Tested"],
    ["Headers",         "✓",                "✓"],
    ["Links",           "✓",                "✓"],
    ["References",      "✓",                "✓"],
    ["Images",          "✓",                "✓"],
    ["Tables",          "✓ (partially)",    "✓"],
    ["Lists",           "✓",                "✓"],
    ["Nested Lists",    "✗",                "✗"],
    ["Blockquotes",     "✓",                "✓"],
    ["Emphasis",        "✓",                "✓"],
    ["Code and Syntax", "✗",                "✗"]
]


str += mdg.gen_table(features)


str += mdg.gen_section()

str += mdg.gen_heading("Further Notes", 2, True)

str += "This Markdown file is generated by the Python script: " + mdg.gen_monospace(os.path.split(__file__)[1]) + "."

str += mdg.gen_section()

actual_date = dt.strftime(dt.now(), "%c")

str += "Last generation: " + actual_date + "."



with open(OUTPUT_FILE, "w") as readme_file:
    readme_file.write(str)