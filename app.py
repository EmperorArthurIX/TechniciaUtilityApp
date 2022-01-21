from ctypes import resize
import streamlit as st

st.title("Technicia Registration Utility App")

event_heads = st.container()
event_heads.header("Event Heads")
event_heads.subheader("Send participant details to event heads")
text = event_heads.text_input("Enter participant details")
text_cats = ["SNo", 'Category', 'CategoryType', 'Name', 'Mobile Number', 'Email', 'Institute', 'Team Size', 'Amount', 'TransactionId', 'PaymentStatus', 'PaymentDate']
text_elems = text.strip().split("\t")
result = dict(zip(text_cats, text_elems))
for i in result:
    event_heads.write("{} : {}".format(i, result[i]))

