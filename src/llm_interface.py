import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama


class LLMInterface:
    def __init__(self):
        self.llm = Ollama(base_url="http://127.0.0.1:11434", model="gemma:2b")

    def invoke_llm(self, template: str, **kwargs) -> str:
        prompt = ChatPromptTemplate.from_template(template)
        chain = prompt | self.llm
        # return chain.invoke(kwargs).content
        return chain.invoke(kwargs)

llm_interface = LLMInterface()