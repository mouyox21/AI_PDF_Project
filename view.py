import streamlit as st
import sqlite3

# Connect to the database
conn = sqlite3.connect('user_credentials.db')
c = conn.cursor()

# Streamlit UI
st.title("View Users")

# Retrieve and display user information
c.execute('SELECT id, username, avatar FROM users')
users = c.fetchall()

if users:
    st.write("List of Users:")
    for user in users:
        user_id, username, avatar = user
        st.write(f"User ID: {user_id}, Username: {username}, ava : {avatar}")
        st.image(avatar, caption=f"Avatar for {username}", use_column_width=True, output_format="JPEG")
        st.write("-" * 50)
else:
    st.warning("No users found in the database.")

# Close the connection
conn.close()
