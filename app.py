import streamlit as st

# Read the HTML file
with open("Project_Manager_Toolkit.html", "r") as html_file:
    html_content = html_file.read()

# Display the HTML using Streamlit
st.title("Project Manager Toolkit")
st.write("This is a deployment of the HTML file using Streamlit.")
st.components.v1.html(html_content, height=800, scrolling=True)
