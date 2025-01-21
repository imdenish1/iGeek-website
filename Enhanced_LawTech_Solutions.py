import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="LawTech Solutions", page_icon="⚖️", layout="wide")

# Define Navigation Menu
menu = ["Home", "Services", "About Us", "Insights", "Contact Us"]
choice = st.sidebar.selectbox("Navigate", menu)

# Load images
hero_image = "https://via.placeholder.com/1200x600"
team_image = "https://via.placeholder.com/800x400"

# CSS Styling for enhanced layout
st.markdown(
    """
    <style>
    .main-header {font-size: 3rem; font-weight: bold; color: #2C3E50;}
    .sub-header {font-size: 1.5rem; color: #34495E;}
    .cta-button {background-color: #3498DB; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;}
    .cta-button:hover {background-color: #2C3E50;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Home Page
if choice == "Home":
    st.markdown('<div class="main-header">Welcome to LawTech Solutions ⚖️</div>', unsafe_allow_html=True)
    st.image(hero_image, caption="Empowering Legal Innovation", use_column_width=True)
    st.write(
        """
        At LawTech Solutions, we combine legal expertise with cutting-edge technology to
        deliver innovative solutions tailored to modern law firms' needs. Join us in redefining
        the future of legal services.
        """
    )
    st.markdown('<a class="cta-button" href="#">Learn More</a>', unsafe_allow_html=True)

# Services Page
elif choice == "Services":
    st.markdown('<div class="main-header">Our Services</div>', unsafe_allow_html=True)
    st.write("Explore how our solutions can revolutionize your legal practice.")

    services = [
        ("Document Automation", "Automate your legal documents to save time and reduce errors."),
        ("Case Management Systems", "Streamline case tracking and client management."),
        ("AI-Powered Legal Research", "Harness AI to access precise and relevant legal data quickly."),
        ("Data Security Solutions", "Safeguard sensitive legal data with cutting-edge encryption."),
    ]

    for service, description in services:
        st.subheader(service)
        st.write(description)

# About Us Page
elif choice == "About Us":
    st.markdown('<div class="main-header">About Us</div>', unsafe_allow_html=True)
    st.write("At LawTech Solutions, we blend legal expertise with technology to empower law firms.")
    st.image(team_image, caption="Meet Our Expert Team", use_column_width=True)
    st.subheader("Our Mission")
    st.write("To revolutionize the legal industry with innovative tech solutions.")
    st.subheader("Our Vision")
    st.write("To be the global leader in legal technology solutions.")

# Insights Page
elif choice == "Insights":
    st.markdown('<div class="main-header">Insights</div>', unsafe_allow_html=True)
    st.write("Stay ahead with the latest trends and innovations in legal technology.")

    articles = [
        ("5 Ways AI is Transforming Legal Practices", "January 2025"),
        ("The Future of Document Automation", "December 2024"),
        ("Enhancing Data Security in Law Firms", "November 2024"),
    ]

    for title, date in articles:
        st.subheader(title)
        st.write(f"Published: {date}")
        st.markdown('<a class="cta-button" href="#">Read More</a>', unsafe_allow_html=True)

# Contact Us Page
elif choice == "Contact Us":
    st.markdown('<div class="main-header">Contact Us</div>', unsafe_allow_html=True)
    st.write("We'd love to hear from you! Please fill out the form below to get in touch.")

    with st.form("contact_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.success("Thank you for reaching out! We'll get back to you soon.")

# Footer
st.markdown("---")
st.markdown("© 2025 LawTech Solutions. All Rights Reserved.")
