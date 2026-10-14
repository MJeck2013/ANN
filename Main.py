import streamlit as st
import time
import numpy as np

try:
    def TSPL(var):
        word_to_num = {"hello": 0.1, "user": 0.2, " ": 0.3, "ANN": 0.4}
        num_to_word = {v: k for k, v in word_to_num.items()}
        try:
            var + 1
            return num_to_word[var]
        except:
            return word_to_num.get(var, 0)
            
    def relu(var, max_cap=float("inf")):
        if var < 0 or var > max_cap:
            return 0
        return var
        
    def Neuron(Input, bias, weights=[0.9, 1.2, 2.1]):
        rt = []
        for num in weights:
            rt.append(Input * num + bias)
        return relu(sum(rt))
    
    def MB(input, bias_base):
        for num in input:
            IL = np.array([Neuron(input, bias_base)] * 24)
            
    st.title("Talk to ANN your own personal AI assistant Version 1.0")
    
    user_input = st.text_input("Type in anything: ", placeholder="Ask me anything...")
    
    if st.button("Submit Question"):
        if user_input.strip():
            nui_list = []
            for word in user_input.split(" "):
                nui_list.append(TSPL(word))
                
            NUI = np.array(nui_list)
            ILB = 1
            while True:
                
            
            st.write("An AI Response Has Been Generated")
            
            output = "yo dude im still making the back end for ANN sorry"
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
    st.exception(e)
