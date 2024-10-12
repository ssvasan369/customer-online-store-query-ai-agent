
# Streamlit AI Query Support System

This project is a **Streamlit-based AI-powered support system** designed to analyze user queries, classify them into categories, assess sentiment, and generate automated responses. The app uses natural language processing to provide technical, billing, or general support responses based on the sentiment and content of the user's query.

## Features

- **Query Categorization**: Automatically categorizes user queries into *Technical*, *Billing*, or *General* categories.
- **Sentiment Analysis**: Analyzes the sentiment of the query (Positive, Negative, or Neutral).
- **Automated Responses**: Provides automated responses based on the query category and sentiment.
- **AI Agent Thoughts**: Displays additional insights or thoughts from the AI agent.
- **Real-Time Response Handling**: Uses the support workflow to process user queries in real time.

## Prerequisites

Ensure that you have the following installed on your machine:

- [Python 3.7+](https://www.python.org/downloads/)
- [Streamlit](https://docs.streamlit.io/en/stable/getting_started.html)
- [LangChain](https://github.com/hwchase17/langchain) - for handling LLM prompts and workflows.
- [Ollama](https://github.com/Ollama) - for interacting with the language model.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ssvasan369/customer-online-store-query-ai-agent.git
   cd customer-online-store-query-ai-agent
   ```

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure the **config** files:

   - **`config/settings.json`**: Contains UI settings (page title, page icon).
   - **`config/config.json`**: Contains layout settings and other configurations.
   - **`config/prompts.yml`**: Defines prompt templates for various query types.

## Project Structure

```bash
.
├── app.py               # Main Streamlit app file
├── config/
│   ├── settings.json    # UI settings (page title, page icon)
│   ├── config.json      # Configuration settings
│   └── prompts.yml      # Prompt templates for LLM
├── support_workflow.py  # Workflow manager for query analysis and response generation
├── support_handlers.py  # Handles categorization, sentiment analysis, and responses
├── utils.py             # Utility functions for loading config files and formatting responses
├── llm_interface.py     # Interface for interacting with language models
└── requirements.txt     # Python package dependencies
```

## Configuration

### `settings.json`

This file contains UI-related settings:

```json
{
  "ui": {
    "page_title": "AI Support System",
    "page_icon": "🎧"
  }
}
```

### `config.json`

This file contains layout and general app settings:

```json
{
  "layout": "wide",
  "default_response": "Thank you for your query. Our support team will get back to you.",
  "escalation_message": "Your query is being escalated to our support team."
}
```

### `prompts.yml`

This YAML file stores prompt templates for handling different queries:

```yaml
categorize_query: |
  Please categorize the following query: {{ query }}
analyze_sentiment: |
  Please analyze the sentiment of the following query: {{ query }}
handle_technical: |
  Respond to this technical support query: {{ query }}
handle_billing: |
  Respond to this billing query: {{ query }}
handle_general: |
  Respond to this general query: {{ query }}
```

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Enter your query in the text input field and click **Submit**.

3. The app will:
   - Categorize the query.
   - Analyze its sentiment.
   - Display metrics such as category, sentiment, and the response handler.
   - Provide a support response based on the processed query.

## Workflow

The support workflow follows these steps:

1. **Categorize**: The query is categorized as *Technical*, *Billing*, or *General* using language models.
2. **Analyze Sentiment**: Sentiment analysis is performed to determine if the sentiment is *Positive*, *Negative*, or *Neutral*.
3. **Handle Query**: Based on the category and sentiment, a response is generated:
   - **Technical**: Handles technical queries.
   - **Billing**: Handles billing queries.
   - **General**: Handles general queries.
   - **Escalation**: If the sentiment is negative, the query is escalated to the support team.

## License

This project is licensed under the MIT License.