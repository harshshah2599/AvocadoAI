import streamlit as st
from extraction import extract_data
import json
import requests

# Set page configuration with wide layout
st.set_page_config(
    page_title="Avocado Health",
    page_icon=":bar_chart:",
    layout="wide",  # Set layout to wide
    initial_sidebar_state="expanded"
)

def show_homepage():
    st.title("Welcome to the AvocadoAI 🥑")
    st.write("""
    Welcome to the Article Analysis Application! This tool helps you extract, analyze, and review articles using state-of-the-art technologies.

    **Features:**
    - **Extraction**: Extracts data from various articles using scraping techniques.
    - **Analysis**: Analyzes the extracted content using advanced generative AI models to identify main topics, claims, medical terms, conditions, and treatments.
    - **FastAPI Integration**: Provides a REST API endpoint for analyzing article content programmatically.

    **How to Use:**
    1. Navigate to the "Extraction, Analysis, FastAPI" page to explore each functionality.
    2. Use the tabs on that page to switch between different sections and learn more about their features.

    **Getting Started:**
    - Ensure that all necessary components are set up, including the extraction script, analysis script, and FastAPI server.
    - Follow the instructions in each section to perform article analysis and explore the features.

    If you have any questions or need further assistance, feel free to contact support or refer to the documentation.

    Enjoy exploring and analyzing your articles!
    """)

def show_extraction():
    st.header("Extraction Functionality")
    st.write("""
    **Extraction (extraction.py):**
    - The `extract_data()` function retrieves article links from a predefined category, fetches each article's content, and compiles it into a JSON format.
    - It uses web scraping techniques to gather titles, publication dates, and content from the articles.

    **How It Works:**
    - The `extract_data()` function fetches article links from a main page.
    - For each link, it extracts the title, publication date, and content, then compiles this information into a structured JSON format.
    """)

    if st.button("Extract Data from 5 Articles", key="button1"):
        with st.spinner("Extracting data..."):
            # Call the extraction function
            extracted_data = extract_data()
            
            # Display the extracted data
            st.subheader("Extracted Data")
            st.json(extracted_data)  # Display JSON data



def show_fastapi():
    st.header("FastAPI Server Functionality")
    st.write("""
    **FastAPI Integration:**
    - The FastAPI server provides an endpoint to analyze article content programmatically.

    **Endpoint: POST /analyze**
    
    **Request Body:**
    ```json
    {
        "text": "string"
    }
    ```

    **Response:**
    ```json
    {
        "analysis": "string"
    }
    ```

    **How It Works:**
    - The server receives a POST request with the article text.
    - It uses the `analyze_content_with_llm` function to process the text and returns the analysis result.
    - Ensure that the FastAPI server is running locally to interact with this endpoint.
    """)

    # Create a form for user input
    with st.form(key='analysis_form'):
        st.header("Submit your article")
        # Text input for the article content
        text = st.text_area("Article Text", height=200)
        # Submit button
        submit_button = st.form_submit_button(label='Analyze')

    # If the submit button is pressed
    if submit_button:
        if text:
            
            # Define the API endpoint URL
            api_url = "http://127.0.0.1:8000/analyze"
            # Prepare the data payload
            payload = {
                "text": text
            }
            try:
                # Send a POST request to the FastAPI endpoint
                response = requests.post(api_url, json=payload)
                # Check if the request was successful
                if response.status_code == 200:
                    # Get the analysis result
                    try:
                        analysis_str = json.loads(response.text)
                        # analysis = json.loads(analysis_str)  # Attempt to parse the analysis JSON
                        # st.write(analysis_str)

                        print_analysis = analysis_str['analysis']['candidates'][0]['content']['parts'][0]['text']

                        st.write(print_analysis)
                        # Extract text content
                        text_content = "No text content available."
                        candidates = analysis_str.get('candidates', [])
                        for candidate in candidates:
                            content = candidate.get('content', {})
                            parts = content.get('parts', [])
                            for part in parts:
                                text = part.get('text', '')
                                if text:
                                    text_content = text
                                    break
                            if text_content != "No text content available.":
                                break

                        # show_analysis = response.text
                        
                        # # Parse the JSON data
                        # data = json.loads(show_analysis)

                        # # Access the text field
                        # candidates = data.get('candidates', [])
                        # if candidates:
                        #     content = candidates[0].get('content', {})
                        #     parts = content.get('parts', [])
                        #     if parts:
                        #         text = parts[0].get('text', '')
                        #     else:
                        #         print("No content parts available.")
                        # else:
                        #     print("No candidates available.")
                        st.success("Analysis Complete")
                        st.write("**Analysis Result:**")
                        st.markdown(text_content) 
                        
                        
                    except (json.JSONDecodeError, TypeError) as e:
                        st.error(f"Error decoding JSON response: {e}")
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter the article text before submitting.")


    
def show_analysis():
    st.header("Analysis Functionality")
    st.write("""
    **Analysis (analysis.py):**
    - The `analyze_content_with_llm(text)` function uses a generative AI model to analyze the content of articles.
    - It identifies main topics, claims, medical terms, conditions, and treatments in the text.

    **How It Works:**
    - The function sends a prompt to the AI model, requesting an analysis of the article content.
    - The response is processed to extract relevant information and returned in a structured format.
    - The function also includes a mechanism to update JSON files with analysis results.
    """)

    if st.button("Analyze Articles", key="button2"):
        with st.spinner("Extracting data..."):
            # Call the analalyze function
            from analysis import main
            main()
            
            with open("articles.json", "r") as file:
                analysis_data = json.load(file)
                
            st.subheader("Analyzed Data")
            st.json(analysis_data)



def main():
    st.title("Avocado Health")

    # Sidebar for navigation
    page = st.sidebar.selectbox("Select a Page", ["Homepage", "AvocadoAI"])

    if page == "Homepage":
        show_homepage()
    elif page == "AvocadoAI":
        tabs = st.tabs(["Extraction", "Analysis", "FastAPI"])

        with tabs[0]:
            show_extraction()

        with tabs[1]:
            show_analysis()

        with tabs[2]:
            show_fastapi()

if __name__ == "__main__":
    main()