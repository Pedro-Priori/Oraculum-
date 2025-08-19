import streamlit as st 

MENSAGENS_EXEMPLO = [
    ('user', 'olá'),
    ('assistent', 'Tudo bem ?'),
    ('user', 'Tudo Otimo'),
]

def pagina_chat():
    st.header("Welcome to the Oraculum 🦉 ", divider=True)

    mensagens = st.session_state.get('mensagens', MENSAGENS_EXEMPLO )
    for mensangem in mensagens:
        chat =  st.chat_message(mensangem[0])
        chat.markdown(mensangem[1])

    input_usuario = st.chat_input('Fale com o Oraculum ')
    if input_usuario:
        mensagens.append(('user',input_usuario))

        st.session_state['mensagens']= mensagens
        st.rerun()

def main():
    pagina_chat()

if __name__ == '__main__':
    main() 

 