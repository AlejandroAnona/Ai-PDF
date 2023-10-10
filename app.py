from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

gif_url = "https://www.gifsanimados.org/data/media/56/computadora-y-ordenador-imagen-animada-0178.gif"

def main():
    load_dotenv()
    st.set_page_config(page_title="Q&A", page_icon="📚")
    container = st.container()
    st.markdown("<p style='color: green; font-size: 35px;'>Haz tus preguntas 💬</p>", unsafe_allow_html=True)
    st.image(gif_url, caption="", use_column_width=False)
    
    # Para subir el archivo PDF
    st.markdown("<p style='color: skyblue; font-size: 30px;'>Sube tu PDF:</p>", unsafe_allow_html=True)
    pdf = st.file_uploader("", type="pdf", help="Aqui puedes cargar tu archivo PDF")
    
    # Extraer el texto, y lo divide por paginas en la linea 24
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
        
      # split convertido a chunks
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
      # creación de los embeddings
      embeddings = OpenAIEmbeddings()
      knowledge_base = FAISS.from_texts(chunks, embeddings)
      
      # lo que verá el usuario
      st.markdown("<p style='color: skyblue; font-size: 30px;'>Preguntame algo acerca del PDF!:</p>", unsafe_allow_html=True)
      user_question = st.text_input("")
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
          response = chain.run(input_documents=docs, question=user_question)
          print(cb)
           
        st.write(response)

        
if __name__ == '__main__':
    main()
