
import streamlit as st

# Set page configuration
st.set_page_config(page_title="LawTech Solutions", page_icon="⚖️", layout="wide")

# Define Navigation Menu
menu = ["Home", "Services", "About Us", "Insights", "Contact Us"]
choice = st.sidebar.selectbox("Navigate", menu)

# Home Page
if choice == "Home":
    st.title("Welcome to LawTech Solutions ⚖️")
    st.write("We revolutionize the legal industry by providing cutting-edge technological solutions tailored to the needs of modern law firms.")
    st.image("https://via.placeholder.com/800x400", caption="Your Trusted Legal Tech Partner", use_column_width=True)
    st.subheader("Why Choose Us?")
    st.write("- Innovative solutions for legal challenges\n- Expertise in legal technology\n- Dedicated support for law firms")

# Services Page
elif choice == "Services":
    st.title("Our Services")
    st.write("Explore the wide range of technological services we provide for law firms:")

    services = {
        "Document Automation": "Streamline document drafting and management with automated tools.",
        "Case Management Systems": "Organize and track cases efficiently.",
        "AI-Powered Legal Research": "Leverage AI for faster and more accurate legal research.",
        "Data Security": "Ensure secure handling of sensitive legal information.",
    }

    for service, description in services.items():
        st.subheader(service)
        st.write(description)

# About Us Page
elif choice == "About Us":
    st.title("About Us")
    st.write("We are a team of passionate technologists and legal experts dedicated to transforming the legal industry.")
    st.image("https://via.placeholder.com/600x300", caption="Meet Our Team", use_column_width=True)
    st.subheader("Our Mission")
    st.write("To empower law firms with innovative technological solutions and technical advisory services.")
    st.subheader("Our Vision")
    st.write("To be the leading provider of tech solutions for the legal industry.")

# Insights Page
elif choice == "Insights":
    st.title("Insights")
    st.write("Stay updated with the latest trends and insights in legal technology.")

    articles = [
        {"title": "5 Ways AI is Revolutionizing Legal Research", "date": "January 2025"},
        {"title": "The Future of Document Automation in Law Firms", "date": "December 2024"},
        {"title": "How to Enhance Data Security in Legal Practices", "date": "November 2024"},
    ]

    for article in articles:
        st.subheader(article["title"])
        st.write(f"Published on: {article['date']}")
        st.write("[Read More](#)")

# Contact Us Page
elif choice == "Contact Us":
    st.title("Contact Us")
    st.write("We would love to hear from you. Fill out the form below to get in touch!")

    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Thank you for reaching out! We will get back to you shortly.")

# Footer
st.markdown("---")
st.markdown("© 2025 LawTech Solutions. All Rights Reserved.")
