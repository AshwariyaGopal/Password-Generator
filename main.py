# (without css)
# import streamlit as st
# import random 
# import string

# def generate_password(Lenght, use_digits, use_special):
#     charcters = string.ascii_letters

#     if use_digits:
#         charcters += string.digits

#     if use_special:
#         charcters += string.punctuation

#     return ''.join(random.choice(charcters) for _ in range(Lenght))

# st.title("🔑 Password Generator")

# Lenght = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# use_digits = st.checkbox("Include Digits")

# use_special = st.checkbox("Include Special Characters")

# if st.button("Generate Password"):
#     password = generate_password(Lenght, use_digits, use_special)
#     st.write(f"Generated Password: `{password}`")

# st.write("")

# st.write("Made with 💕 by [Ashwariya](https://github.com/AshwariyaGopal)")



    



#(with css)
import streamlit as st
import random 
import string

# Set basic page config
st.set_page_config(
    page_title="Password Generator",
    page_icon="🔒",
    layout="centered"
)

# Professional color scheme and improved CSS
st.markdown("""
<style>
    /* Main container styling */
    .stApp {
        background-color: #f5f5f5;
    }
    
    /* Title styling */
    .big-font {
        font-size: 28px !important;
        font-weight: bold;
        color: #1E3D59;
        margin-bottom: 20px;
    }
    
    /* Button styling */
    .stButton>button {
        background-color: #17B794 !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 15px !important;
        font-size: 16px !important;
        width: 100% !important;
    }
    
    /* Slider and label styling */
    .stSlider label, .standard-text {
        color: #1E3D59 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }
    
    /* Checkbox styling */
    .stCheckbox {
        color: #1E3D59 !important;
    }
    
    /* Divider styling */
    hr {
        margin: 20px 0 !important;
    }
</style>
""", unsafe_allow_html=True)

def generate_password(Lenght, use_digits, use_special):
    charcters = string.ascii_letters
    if use_digits:
        charcters += string.digits
    if use_special:
        charcters += string.punctuation
    return ''.join(random.choice(charcters) for _ in range(Lenght))

# Main UI
st.markdown('<p class="big-font">🔒 Password Generator</p>', unsafe_allow_html=True)
st.markdown('<p class="standard-text">Create strong and secure passwords for your accounts</p>', 
            unsafe_allow_html=True)

st.markdown("---")

# Password Length slider and display in same row
col1, col2 = st.columns([3, 1])
with col1:
    Lenght = st.slider("Password Length", min_value=6, max_value=32, value=12)
with col2:
    st.write("")  # For alignment
    st.write(f"Length: {Lenght}")

# Checkboxes
col3, col4 = st.columns(2)
with col3:
    use_digits = st.checkbox("🔢 Include Numbers (0-9)")
with col4:
    use_special = st.checkbox("🔣 Include Special Characters")

st.markdown("---")

# Generate Password Button and Display
if st.button("🔐 Generate Strong Password", use_container_width=True):
    password = generate_password(Lenght, use_digits, use_special)
    
    # Single password display with copy functionality
    st.markdown("""
        <div style='background-color: #E8F3F1; padding: 20px; border-radius: 5px; margin: 20px 0;'>
            <h3 style='color: #1E3D59; margin: 0 0 10px 0;'>Your Generated Password:</h3>
            <div style='background-color: #1E3D59; color: white; padding: 15px; border-radius: 5px; 
                      font-family: monospace; font-size: 18px; text-align: center; margin-bottom: 15px;'>
                {password}
            </div>
            <div style='text-align: center;'>
                <button onclick="navigator.clipboard.writeText('{password}'); alert('Password copied!');" 
                        style='background-color: #17B794; color: white; padding: 8px 16px; 
                               border: none; border-radius: 4px; cursor: pointer;'>
                    📋 Copy Password
                </button>
            </div>
        </div>
    """.format(password=password), unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #1E3D59;'>"
    "Made with 💕 by "
    "<a href='https://github.com/AshwariyaGopal' style='color: #17B794; text-decoration: none;'>"
    "Ashwariya</a></div>", 
    unsafe_allow_html=True
)