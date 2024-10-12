from typing import Dict
from llm_interface import llm_interface
from utils import load_yaml_file


class SupportHandlers:
    def __init__(self):
        self.prompts = load_yaml_file('config/prompts.yml')

    def categorize_query(self, query: str) -> str:
        template = self.prompts['categorize_query']
        return llm_interface.invoke_llm(template, query=query)

    def analyze_sentiment(self, query: str) -> Dict[str, str]:
        template = self.prompts['analyze_sentiment']
        result = llm_interface.invoke_llm(template, query=query)
        print(f"result from sentiment analysis : {result}")
        sentiment, analysis = result.split(":", 1)
        sentiment = analysis.split('\n\n')[0]
        return {"sentiment": sentiment.strip(), "sentiment_analysis": analysis.strip()}

    def handle_technical(self, query: str) -> str:
        template = self.prompts['handle_technical']
        return llm_interface.invoke_llm(template, query=query)

    def handle_billing(self, query: str) -> str:
        template = self.prompts['handle_billing']
        return llm_interface.invoke_llm(template, query=query)

    def handle_general(self, query: str) -> str:
        template = self.prompts['handle_general']
        return llm_interface.invoke_llm(template, query=query)

support_handlers = SupportHandlers()