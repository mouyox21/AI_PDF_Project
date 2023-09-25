import streamlit as st
import sqlite3
from hashlib import sha256

# Connect to the database
conn = sqlite3.connect('2')
c = conn.cursor()

# Streamlit UI
st.title("User Authentication and Avatar Upload")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if menu == "Register":
    avatar = st.sidebar.file_uploader("Choose an image for your avatar", type=["jpg", "png", "jpeg"])
    register_button = st.sidebar.button("Register")
    
    if register_button and username and password:
        hashed_password = sha256(password.encode()).hexdigest()
        
        # Insert user data into the database
        c.execute('INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)',
                  (username, hashed_password, f'avatars/{username}_avatar.jpg'))
        conn.commit()
        
        if avatar:
            avatar_path = f'avatars/{username}_avatar.jpg'
            with open(avatar_path, "wb") as f:
                f.write(avatar.getbuffer())

        st.sidebar.success("User registered successfully!")

# ...
elif menu == "Login":
    login_button = st.sidebar.button("Login")

    if login_button and username and password:
        hashed_password = sha256(password.encode()).hexdigest()
        c.execute('SELECT id, username, avatar FROM users WHERE username=? AND password=?', (username, hashed_password))
        user = c.fetchone()

        if user:
            user_id, _, avatar_path = user
            st.sidebar.image(avatar_path, caption=f"Avatar for {username}", use_column_width=True)
            st.sidebar.success("Login successful!")

            # Display user details
            st.title("User Details")
            st.image(avatar_path, caption=f"Avatar for {username}", use_column_width=True)
            st.write(f"User ID: {user_id}")
            st.write(f"Username: {username}")
            st.write(f"Avatar Path: {avatar_path}")

        else:
            st.sidebar.error("Invalid credentials")

# ...

# Close the connection
conn.close()
