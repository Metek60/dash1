import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Dash1",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Dash1")
st.subheader("Borsa Strateji Takip Dashboard")

DATA_FILE = "data.csv"

# Data dosyası yoksa oluştur
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=[
        "Tarih",
        "Tip",
        "Overall",
        "Xu100"
    ])
    df.to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)

st.divider()

st.header("Yeni Veri Girişi")

tip = st.radio(
    "Kayıt Tipi",
    ["Ara Kontrol", "Gün Sonu"],
    horizontal=True
)

overall = st.number_input(
    "Overall",
    value=0.0,
    step=1.0
)

xu100 = st.number_input(
    "Xu100 (%)",
    value=0.0,
    step=0.01
)

st.divider()

if st.button("💾 Kaydet", use_container_width=True):

    yeni_kayit = pd.DataFrame([{
        "Tarih": datetime.now().strftime("%d.%m.%Y %H:%M"),
        "Tip": tip,
        "Overall": overall,
        "Xu100": xu100
    }])

    df = pd.concat([df, yeni_kayit], ignore_index=True)

    df.to_csv(DATA_FILE, index=False)

    st.success("Kayıt başarıyla eklendi.")

st.divider()

st.header("Kayıtlar")

if len(df) == 0:
    st.info("Henüz kayıt bulunmuyor.")
else:
    st.dataframe(
        df.iloc[::-1],
        use_container_width=True
    )
