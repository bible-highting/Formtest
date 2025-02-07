import streamlit as st
from streamlit_gsheets import GSheetsConnection


st.title("구글시트 불러오기")


url1 = st.secrets["googlesheet"]["url1"]
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url1)
st.write(df)

st.write("현재 신청자 수는", len(df), "명 입니다. ")
dates = df['신청 날짜'].str.split(', ').explode() # ➊
st.write(dates.value_counts()) # ➋
st.bar_chart(dates.value_counts())