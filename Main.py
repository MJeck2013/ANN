import streamlit as st
import time
st.title("Talk to ANN your own personal AI assistant Version 1.0")
input = st.text_input("Type in anything: ", placeholder="Ask me anything...")
if st.button("Submit Question"):
    if input:
        output = "yo dude im still making the back end for ANN sorry"
        st.write("")
        output_placeholder = st.empty()
        displayed_text = ""
        for word in output.split(" "):
            displayed_text += word + " "
            output_placeholder.markdown(displayed_text)
            time.sleep(0.15)
    else:
        st.warning("You can't type in nothing lol")
