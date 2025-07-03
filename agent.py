from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings()
video_url = "https://www.youtube.com/watch?v=lG7Uxts9SXs&ab_channel=freeCodeCamp.org"

def create_vector_db_from_youtube_url(video_url: str) -> FAISS:
    loader = YoutubeLoader.from_youtube_url(video_url)
    transcript = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(transcript)
    if not docs:
        raise ValueError("No documents found in the transcript.")
    
    vector_db = FAISS.from_documents(docs, embeddings)
    return vector_db

print(create_vector_db_from_youtube_url(video_url))

def get_response_from_query(db, query, key=4):
    # text-davinci can handle 4097 tokens

    # docs = db.similarity_search(query, k=key)
    # docs_page_content = "".join([d.page_content for d in docs])
    docs_page_content = "Hello, my name is Nick Tony. I'm a software engineer and I work at freeCodeCamp.org. " \
                          "In this video, I will be teaching you how to build a simple web application using Flask and Python. " \
                          "Flask is a micro web framework for Python that allows you to build web applications quickly and easily. " 
    llm = OpenAI(model="GPT-4o")

    prompt = PromptTemplate(
        input_variables=["question", "docs"],
        template="You are a helpful Youtube assistant that can  answer questions about videos." \
        "Answer the following question: {question}" \
        "By searching the following documents: {docs}" \
        "If you don't know the answer, just say that you don't know. Don't try to make up an answer."
    )

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.invoke({"question": query, "docs": docs_page_content})
    response = response.replace("\n", " ")
    return response

my_query = "What is the main topic of the video?"
print(get_response_from_query(create_vector_db_from_youtube_url(video_url), my_query))
