import streamlit as st      # (without css)
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



    

 # (with css)
import random
import string


st.set_page_config(page_title="Password Generator", page_icon="🔒", layout="centered")

# Apply Custom CSS
st.markdown("""
<style>
    .stApp { background-color: #f5f5f5; }
    .big-font { font-size: 28px !important; font-weight: bold; color: #1E3D59; }
    .stButton>button { 
    background-color: #17B794 !important; color: white !important; font-weight: bold; border: none; padding: 15px !important; font-size: 16px !important; width: 100% !important;
    margin-top: 30px !important;  /* Added spacing between buttons */ }
    .stSlider label, .standard-text { color: #1E3D59 !important; font-size: 16px !important; font-weight: 500 !important; }
    
    /* Darker Background for Password Display */
    .password-box {
        background-color: #1E3D59 !important;
        color: white !important;
        padding: 12px !important;
        border-radius: 5px !important;
        font-family: monospace !important;
        font-size: 18px !important;
        text-align: center !important;
        margin-top: 10px !important;
    }
            
     /* Style for "Your Password" heading */
    .password-heading {
        font-size: 20px !important;
        font-weight: bold !important;
        color: #1E3D59 !important;
        margin-top: 20px !important;
        text-align: left !important;
    }
     .footer {
        margin-top:40px !important
        text-align: center !important
            }
</style>
""", unsafe_allow_html=True)

# Function to generate password
def generate_password(length, use_digits, use_special):
    characters = ""
    
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if not (use_digits or use_special):  
        characters += string.ascii_letters  # Default to letters if no option is selected
    
    if not characters:  # If no character set is selected
        return "Select at least one option!"
    
    return ''.join(random.choice(characters) for _ in range(length))

# UI Components
st.markdown('<p class="big-font">🔒 Password Generator</p>', unsafe_allow_html=True)
st.markdown("Create strong and secure passwords for your accounts")

st.markdown("---")

# Length slider
col1, col2 = st.columns([3, 1])
with col1:
    length = st.slider("Password Length", min_value=6, max_value=32, value=12)
with col2:
    st.write(f"Length: {length}")

# Checkboxes
col3, col4 = st.columns(2)
with col3:
    use_digits = st.checkbox("🔢 Include Numbers (0-9)")
with col4:
    use_special = st.checkbox("🔣 Include Special Characters")

st.markdown("---")

# Session state to store password
if "password" not in st.session_state:
    st.session_state["password"] = ""

# Generate Password Button
if st.button("🔐 Generate Strong Password", use_container_width=True):
    st.session_state["password"] = generate_password(length, use_digits, use_special)

# Display password
if st.session_state["password"]:
    st.markdown('<p class="password-heading">🔑 Your Password:</p>', unsafe_allow_html=True)  # Added heading
    st.markdown(f"""
        <div class="password-box">{st.session_state['password']}</div>
    """, unsafe_allow_html=True)

st.markdown("""
<p class="footer" style="margin-top: 40px; text-align: center;">
    Made with 💕 by <a href="https://github.com/AshwariyaGopal" target="_blank" style="color: #17B794; font-weight: bold; text-decoration: none;">Ashwariya</a>
</p>
""", unsafe_allow_html=True)