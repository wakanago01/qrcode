import streamlit as st
import qrcode
import io

st.title( "URL を QRCode に 変 換 " )

with st.form( key="url-input", clear_on_submit= True ):
    url = st. text_input("URL:")
    button = st.form_submit_button("変換")


if url:
    img= qrcode. make( url)
    with io. BytesIO() as f:
        img.save( f,format="PNG") # BytesIO に 書 き 出 す
        png = f. getvalue() # 実 体 を 代 入
    st. write( url) # URL を 表 示
    st. image( png) # 画 像 を 表 示
    st. download_button( "Download", data= png ,file_name="urlqr.png" )
