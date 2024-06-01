import streamlit as st
from wonderwords import RandomSentence
import time

# Initialize the random sentence generator
sen1 = RandomSentence()

# Define a function to convert generated and user input sentences into a colored string
def convert_to_colored(generated, user):
    colored_text = ''
    for gen_char, user_char in zip(generated, user):
        if gen_char == user_char:
            colored_text += f'<span style="color: green;">{user_char}</span>'
        else:
            colored_text += f'<span style="color: red;">{user_char}</span>'
    # Add remaining characters (if any) from the longer string without coloring
    if len(generated) > len(user):
        colored_text += generated[len(user):]
    elif len(user) > len(generated):
        colored_text += f'<span style="color: red;">{user[len(generated):]}</span>'
    return colored_text

# Generate a new sentence
if "generated_sentence" not in st.session_state:
    st.session_state["generated_sentence"] = sen1.sentence()

# Streamlit app
st.title("Typing Speed Test")

st.write(f"Generated Sentence: {st.session_state['generated_sentence']}")

if "start_time" not in st.session_state:
    st.session_state["start_time"] = None

# Start button to start the timer and user input text area
if st.button("Start Typing"):
    st.session_state["start_time"] = time.time()
    st.session_state["user_input"] = ""  # Clear previous input

user_input = st.text_area("Type the sentence here:", value=st.session_state.get("user_input", ""), on_change=lambda: st.session_state.update({"user_input": user_input}))

# Calculate typing speed and display results
if st.button("Submit"):
    if st.session_state["start_time"] is not None:
        stop_time = time.time()
        time_for_typing = stop_time - st.session_state["start_time"]
        minutes = time_for_typing / 60
        length_of_sentence = len(user_input)
        speed = int(length_of_sentence / minutes)

        colored_output = convert_to_colored(st.session_state["generated_sentence"], user_input)
        st.markdown(f"Your typed sentence: {colored_output}", unsafe_allow_html=True)
        st.write(f"Time taken: {time_for_typing:.2f} seconds")

        if user_input == st.session_state["generated_sentence"]:
            st.success(f"Speed of typing: {speed} characters per minute")
        else:
            st.error("The input does not match the generated sentence. Please retry!")
            # Retain the same sentence for retry
            st.session_state["start_time"] = None  # Reset the start time for retry
    else:
        st.error("Please start the typing test first.")
