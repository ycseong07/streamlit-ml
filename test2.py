import streamlit as st

st.title("Streamlit Test")

input_user_name = st.text_input(label="User Name", value="default value")
radio_gender = st.radio(label="Gender", options=["Male", "Female"])
check_1 = st.checkbox(label="agree", value=False)
memo = st.text_area(label="memo", value="")

if st.button("Confirm"):
    con = st.container()
    con.caption("Result")
    con.write(f"User Name is {str(input_user_name)}")
    con.write(str(radio_gender))
    con.write(f"agree : {check_1}")
    con.write(f"memo : {str(memo)}")