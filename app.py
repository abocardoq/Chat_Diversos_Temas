# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 20:29:22 2025

@author: aboca
"""

#importar librerias

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import GoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Inicializa el modelo de lenguaje
llm = GoogleGenerativeAI(model="gemini-2.0-flash") # la API se configuro en las variables de entorno

st.sidebar.image(r'C:\Users\aboca\Streamlit_LLM\SmartBI.png')
tema = st.sidebar.selectbox('Seleccione tema',['Diagnóstico Médico', 'Ingeniería Petrolera'])

if tema == 'Diagnóstico Médico':
   st.subheader('Diagnóstico Médico')
   st.subheader('Deberás proporcionar la especialidad medica y los sintomas que presentas')
   st.subheader('Para que te ayude a dar un diagnóstico')
   st.write('Recuerda siempre, validar el diagóstico con un médico')
     

   especialidad = st.text_input('Especialidad')  
   sintoma= st.text_input('Sintomas') 
                       
    
   if especialidad and sintoma:
        st.write(f'La especialidad proporcionada es: **{especialidad}**') 
        st.write(f'El sintoma proporcionado es: **{sintoma}**')
        st.write("Procesando...")    

        # Definir un prompt avanzado para diagnóstico médico
        prompt = PromptTemplate(
        template="Eres un médico experto en {especialidad}. Un paciente presenta los siguientes síntomas: {sintoma}. ¿Cuál podría ser el diagnóstico?",
        input_variables=["especialidad", "sintoma"])

        # Crea una cadena con el prompt y el modelo
        chain = LLMChain(llm=llm, prompt=prompt)

        # Ejecuta la cadena con variables específicas
        respuesta = chain.run({
            "especialidad": especialidad,
            "sintoma": sintoma})

        st.write(respuesta)

       
elif tema == 'Ingeniería Petrolera':
   st.subheader('Industria Petrolera')
   st.subheader('Deberás proporcionar la especialidad y el tema')
   st.subheader('Para que te ayude a dar mi opinión como experto')
        

   especialidad_ip = st.text_input('Especialidad petolera')  
   tema = st.text_input('tema') 
                       
    
   if especialidad_ip and tema:
        st.write(f'La especialidad proporcionada es: **{especialidad_ip}**') 
        st.write(f'El tema proporcionado es: **{tema}**')
        st.write("Procesando...")    

        # Definir un prompt avanzado para diagnóstico médico
        prompt = PromptTemplate(
        template="Eres un ingeniero de la industria petolera, experto en {especialidad_ip}. Dame información referente a esta tema: {tema}. ¿y donde consultar más información?",
        input_variables=["especialidad_ip", "tema"])

        # Crea una cadena con el prompt y el modelo
        chain = LLMChain(llm=llm, prompt=prompt)

        # Ejecuta la cadena con variables específicas
        respuesta = chain.run({
            "especialidad_ip": especialidad_ip,
            "tema": tema})

        st.write(respuesta)



