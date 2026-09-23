import json
import streamlit as st
from packaging_parser import calc_total_units, get_unit, parse_packaging


st.title("Process Package Files")

uploaded_file = st.file_uploader("Choose a file", key="package_file")
packages = []
if "count_files" not in st.session_state:
    st.session_state.count_files = 0
    st.session_state.count_packages = 0
    st.session_state.summaries = []


if st.button("Process file", key = "process") == True and uploaded_file:
    filename = uploaded_file.name
    text = uploaded_file.getvalue().decode('utf-8')
    words = text.split("\n")
    for i in words:
        if i != "":
            package = parse_packaging(i)
            total = calc_total_units(package)
            unit = get_unit(package)
            packages.append(package)
    with open(f"data/{filename[:-4]}.json", "w") as f:
        json.dump(packages, f)
    st.session_state.count_files += 1
    st.session_state.count_packages += len(packages)
    st.session_state.summaries.append(
        f"{len(packages)} packages written to data/{filename[:-4]}.json"
        )

col1, col2 = st.columns(2)
col1.metric("Files processed", st.session_state.count_files)
col2.metric("Packages processed", st.session_state.count_packages)

for i in st.session_state.summaries:
        st.info(i)