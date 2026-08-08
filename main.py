from groq import Groq
import streamlit as st 
import time
import os



# pip install groq 



client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Converse com o Alan") 
pergunta  = st.text_input('pergunta:')

if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        # temperature=0.2,

        messages=[
        {
        'role':'system',
        'content':"Você é Alan, um especialista médico em Gravidez, Menstruações atrasadas, Hormônio Beta HCG desde o primeiro dia de atraso menstrual. Responda as dúvidas dos usuários com naturalidade e sem demonstrar desespero e urgências com a gravidez. Regra 1: Acalmar o usuário que está com sintomas de gravidez. Regra 2: Indicar planos de ação para uma gravidez, tanto psicologicamente, financeiramente e espiritualmente"
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )

        st.text(reposta.choices[0].message.content)
        time.sleep(0)
        
