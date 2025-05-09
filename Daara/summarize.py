from langchain_community.document_loaders import PyPDFLoader
from langchain.chat_models import init_chat_model
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.llm import LLMChain
from langchain_core.prompts import ChatPromptTemplate
import getpass
import os
from Tidjani_Daara.settings import MEDIA_ROOT, MISTRAL_API_KEY

# loading model
if not os.environ.get("MISTRAL_API_KEY"):
  os.environ["MISTRAL_API_KEY"] = getpass.getpass("Enter API key for Mistral AI: ")

llm = init_chat_model("mistral-large-latest", model_provider="mistralai")

# Define prompt
prompt = ChatPromptTemplate.from_messages(
    [("system", "Write a summary of the following:\\n\\n{context}")]
)

def summarization(file_path):
 
  loader = PyPDFLoader(file_path)
  docs = loader.load()

  chain =create_stuff_documents_chain(llm, prompt)
  summary =  chain.invoke({"context":docs})
  print(summary)
  return summary