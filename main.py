from groq import Groq
import streamlit as st 
import time
import os



# pip install groq 



client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

st.title("Converse com o Sniper") 
pergunta  = st.text_input('pergunta:')

if st.button('enviar'):
    # if pergunta.strip():
        reposta =  client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        # temperature=1.0,

        messages=[
        {
        'role':'system',
        'content':"Você é um caçador experiente do exército brasileiro, com 35 anos de experiência em abates pela Guerra da ONU, Segunda Guerra mundial e Guerra do Paraguai (Ignore a cronologia).
         Regra 1: Não Fique exibindo seus títulos e cargos de forma arrogante, apenas demonstre sua experiência de forma parcial de acordo com a pergunta em questão
         Regra 2: Demonstre conhecimentos em áreas específicas, porém seu foco é no Exército Brasileiro, e no curso de caçador"
        },
        {
            'role':'user',
            'content': pergunta
            
        }
        ]
        )

        st.text(reposta.choices[0].message.content)
        time.sleep(0)
        
