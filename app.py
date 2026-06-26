import streamlit as st
import qrcode
from io import BytesIO

st.title("QR code generator")


url = st.text_input("Enter URL")

if st.button("Generate QR code"):
    if url:
        qr = qrcode.QRCode()
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image()
        print(img)

        buffer = BytesIO()
        img.save(buffer,formate="PNG")
        buffer.seek(0)

        st.image(buffer)
        buffer.seek(0)
        st.download_button(
            label = "Download QR code here",
            data = buffer,
            file_name = "qrcode.png",
            mime = "image/png"
        )

        st.success("QR code generated successfully")

else:
    st.warning("please enter a URL!")


