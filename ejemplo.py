import streamlit as st
st.title("Mi primera aplicacion")

nombre = st.text_input("ingresa tu nombre")


if st.button("Saludar"):
    if nombre:

        st.write(f"hola, {nombre}!")
        st.balloons()
        st.success("saludo enviado con exito")
        st.info("disfruta de la aplicacion!")
        st.warning("recuerda cerrar la aplicacion cuando termines")
    else:
        st.error("Por favor ingresa tu nombre antes de saludar. ")
        st.error("Aun no has presionado el boton de saludo")
        st.info("Presiona el boton para recu=ibir un saludo")