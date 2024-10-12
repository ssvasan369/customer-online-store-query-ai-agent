
import os
from typing import Dict, TypedDict
from langgraph.graph import StateGraph, END
from support_handlers import support_handlers
import json


# Get the absolute path to the directory of the current script (app.py)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the config.json file
config_path = os.path.join(base_dir, 'config', 'config.json')

# Open the config file using the absolute path
with open(config_path) as config_file:
    config = json.load(config_file)


class State(TypedDict):
    query: str
    category: str
    sentiment: str
    sentiment_analysis: str
    response: str

class SupportWorkflow:
    def __init__(self):
        self.workflow = StateGraph(State)
        self._setup_workflow()
    
    def _setup_workflow(self):
        self.workflow.add_node("categorize", self._categorize)
        self.workflow.add_node("analyze_sentiment", self._analyze_sentiment)
        self.workflow.add_node("handle_technical", self._handle_technical)
        self.workflow.add_node("handle_billing", self._handle_billing)
        self.workflow.add_node("handle_general", self._handle_general)
        self.workflow.add_node("escalate", self._escalate)

        self.workflow.add_edge("categorize", "analyze_sentiment")

        self.workflow.add_conditional_edges(
            "analyze_sentiment",
            self._route_query,
            {
                "handle_technical": "handle_technical",
                "handle_billing": "handle_billing",
                "handle_general": "handle_general",
                "escalate": "escalate"

            }
        )

        self.workflow.add_edge("handle_technical", END)
        self.workflow.add_edge("handle_billing", END)
        self.workflow.add_edge("handle_general", END)
        self.workflow.add_edge("escalate", END)

        self.workflow.set_entry_point("categorize")
    
    def _categorize(self, state: State) -> Dict:
        return {"category": support_handlers.categorize_query(state["query"])}
    
    def _analyze_sentiment(self, state: State) -> Dict:
        return support_handlers.analyze_sentiment(state["query"])
    
    def _handle_technical(self, state: State) -> Dict:
        return {"response": support_handlers.handle_technical(state["query"])}

    def _handle_billing(self, state: State) -> Dict:
        return {"response": support_handlers.handle_billing(state["query"])}
    
    def _handle_general(self, state: State) -> Dict:
        return {"response": support_handlers.handle_general(state["query"])}
    
    def _escalate(self, state: State) -> Dict:
        return {"response": config['escalation_message']}
    

    def _route_query(self, state: State) -> str:
        if state["sentiment"] == "Negative":
            return "escalate"
        elif state["category"] == "Technical":
            return "handle_technical"
        elif state["category"] == "Billing":
            return "handle_billing"
        else:
            return "handle_general"

    
    

    def run(self, query: str) -> Dict[str, str]:
        app = self.workflow.compile()
        initial_state = {"query": query}
        results = app.invoke(initial_state)

        print(results)

        return {
            "query": query,
            "category": results.get("category", "Unknown"),
            "sentiment": results.get("sentiment", "Unknown"),
            "sentiment_analysis": results.get("sentiment_analysis", "No analysis available"),
            "response": results.get("response", config['default_response'])
        }


support_workflow = SupportWorkflow()