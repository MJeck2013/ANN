try:
    import streamlit as st
    import time
    import numpy
    def relu(var):
        if var < 0 or var > 100:
            return 0
        return var
    def Neuron(Input, bias, weights=[0.9, 1.2, 2.1]):
        rt = []
        for num in weights:
            rt.append(Input * num + bias)
        return relu(sum(rt))
    st.title("Talk to ANN your own personal AI assistant Version 1.0")
    input = st.text_input("Type in anything: ", placeholder="Ask me anything...")
    if st.button("Submit Question"):
        if input:
            output = "yo dude im still making the back end for ANN sorry"
            st.write("A AI Has Been Generated")
            output_placeholder = st.empty()
            displayed_text = ""
            for word in output.split(" "):
                displayed_text += word + " "
                output_placeholder.markdown(displayed_text)
                time.sleep(0.15)
        else:
            st.warning("You can't type in nothing lol")
except Exception as e:
    st.title("OOPS! Sorry Something went Wrong.")
