"""
Streamlit page for processing a single packaging description.

The user enters a packaging hierarchy as text (for example,
"12 eggs in 1 carton / 3 cartons in 1 box"). The page parses it into its
levels, shows each level's details, and reports the total number of base
units in the full package.

Parsing and calculation live in `packaging_parser`, so this file only
handles input and display.
"""

import streamlit as st
from packaging_parser import calc_total_units, get_unit, parse_packaging

st.title("Process One Package")

# The placeholder shows the expected format: levels separated by "/",
# each written as "<qty> <item> in <qty> <container>".
package_data = st.text_input(
    "Enter package data:",
    key="package_data",
    placeholder="12 eggs in 1 carton / 3 cartons in 1 box",
)

# Guard: Streamlit reruns the whole script on every interaction, so the
# input is empty on first load. Skipping empty input avoids passing a blank
# string to the parser and showing errors or empty results before the user
# has typed anything.
if package_data:
    # Parse the text into a list of dicts, one per packaging level.
    package = parse_packaging(package_data)

    # Multiply through the levels to get the total count of base units,
    # and get the unit name (e.g. "eggs") for the summary.
    total = calc_total_units(package)
    unit = get_unit(package)

    # Show each parsed level so the user can check the input was read
    # correctly before relying on the total.
    for level in package:
        for key, value in level.items():
            st.info(f"{key} ➡️ {value}")

    # Show the final total in a success box to set it apart from the details.
    st.success(f"Total 📦 Size: {total} {unit}")