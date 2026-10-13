try:
  import streamlit as st
  
  st.title("Streamlit Input Showcase")
  
  st.subheader("Live Typing Output")
  # By default, st.text_input updates the variable 'live_input' on every press of the Enter key or when clicking outside the box
  live_input = st.text_input("Type here to see it live:", key="live_box")
  st.write("**Live Output:**", live_input)
  
  st.divider()
  
  # 2. Text Box Input with Submit Button
  st.subheader("Submit Button Input")
  
  # We use a form to prevent the text box from updating the app until the button is clicked
  with st.form(key="submit_form"):
      button_input = st.text_input("Type your answer here:")
      submit_button = st.form_submit_button(label="Submit Answer")
  
  # This only displays or updates after the user clicks the button
  if submit_button:
      st.success(f"Answer submitted: {button_input}")
except Exception as e:
  st.title("opps sorry")
  st.write(f"An error has occured: {e}")
