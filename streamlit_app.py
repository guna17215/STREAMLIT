import streamlit as st
from datetime import datetime


st.title("Hello, My name is Gunavardhan Reddy, learning streamlit!")


st.header("Here we are learning how BUTTTONS work in streamlit.")

st.subheader("1. Normal Buttons.")
result = st.button(label = "Button.", help = "This is button where its default value is false and on click it turns boolean value true.")
res = str(result)
st.write("On Click, it becomes true: " + res)
if st.button(
label = "Click Me.",
help = "This button has its own content to display, other than true false."
):
	st.write("Hey there, I am button. :heart:")
else:
	st.write("you haven't clicked the button. :point_up:")
	
st.subheader("2.Download Buttons.")
st.download_button(
	label = "Download a csv file.",
	data = 'csv',
	file_name = 'IPL 2022.csv',
	mime = 'txt/csv',
	help = "Not only csv files you can create dowload buttons for directing to dowload images, binaryfiles, textfiles.",
)

st.subheader("3.Check Boxes, Radio Buttons, Select Buttons, Multi Select.")
# st.latex("If have any doubts or forgot syntax refer documentation for above topics.") 
value = st.checkbox("I will complete streamlit doucmentation by this month.")
if value:
	st.write("That's Great. :sunglasses:")
else:
	st.write("Very poor. :sleepy:")
	
languages = ['PYTHON', 'C', 'C++', 'JAVA', 'JAVASCRIPT']
language = st.radio("Which language do you like the most.", languages)
st.write("you like to code in "+ language + ".")

st.subheader("4.sliders")
start_time = st.slider(
	label = "When did you start learning streamlit?",
        value = datetime(2022, 11, 25, 5, 30),
	format = "MM/DD/YY - hh:mm",
        help = "Similarly, you have select sliders also. Select sliders take any datatype as input where as sliders don't.")
st.write("You started learning streamlit : ", start_time)

st.subheader("5.text, number, time, date, camera inputs, file_uploader and text area")
st .write("**Refer streamlit Documentation.**")

	
