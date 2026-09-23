import json
import streamlit as st
from packaging_parser import calc_total_units, get_unit, parse_packaging


st.title("Process File of Packages")

uploaded_file = st.file_uploader("Choose a file", key="package_file")

packages = []

if uploaded_file:
    filename = uploaded_file.name
    text = uploaded_file.getvalue().decode('utf-8')
    words = text.split("\n")
    for i in words:
        if i != "":
            package = parse_packaging(i)
            total = calc_total_units(package)
            unit = get_unit(package)
            st.info(f"{i} -> Total Box Size: {total} {unit}")
            packages.append(package)
    with open(f"data/{filename[:-4]}.json", "w") as f:
        json.dump(packages, f)

    st.success(f"{len(packages)} packages written to data/{filename[:-4]}.json")
