import streamlit as st
from utils import load_json_file, format_thoughts, get_response_type
from support_workflow import support_workflow

# Load settings and config
settings = load_json_file('config/settings.json')
config = load_json_file('config/config.json')

print(f"settings: {settings}")

def main():
    st.set_page_config(
        page_title=settings['ui']['page_title'],
        page_icon=settings['ui']['page_icon'],
        layout=config['layout']
    )

    st.title(f"🎧 {settings['ui']['page_title']}")

    query = st.text_input("Please enter your query:")

    if st.button("Submit"):
        if query:
            with st.spinner("Processing your query..."):
                 result = support_workflow.run(query)
                 print(f"result: {result}")

                 st.subheader("Query Analysis")
            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Category", result['category'])

            with col2:
                st.metric("Sentiment", result['sentiment'])

            with col3:
                st.metric("Query Handled By", get_response_type(result['sentiment']))

            st.subheader("Sentiment Analysis")
            st.info(result['sentiment_analysis'])

            st.subheader("Support Response")
            st.success(result['response'])

            st.subheader("AI Agent Thoughts...")
            thoughts = format_thoughts(result['category'], result['sentiment'])
            st.text(thoughts)


        else:
            st.warning("Please enter a query before submitting.")

if __name__ == "__main__":
    main()