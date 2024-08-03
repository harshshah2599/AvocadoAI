# AvocadoAI 🥑

AvocadoAI is a cutting-edge application designed to leverage advanced generative AI models for analyzing and extracting meaningful insights from medical or health related blog articles. The project encompasses functionalities for data processing, interaction with AI models, FastAPI for creating endpoints, and storage of analysis results.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Approach](#approach)
- [Challenges Faced](#challenges-faced)
- [Scaling](#ideas-for-scaling-the-system)
- [Conclusion](#conclusion)


## Project Overview

AvocadoAI integrates with Google's Gemini API to analyze medical texts. It extracts named entities and key phrases from given texts and saves the analysis results into a JSON file. The project includes scripts for data extraction, content analysis, and result storage.

## Features

- **Generative AI Analysis:** Utilizes Google's Gemini API to perform detailed text analysis.
- **JSON Data Handling:** Loads, processes, and stores data in JSON format.
- **Error Handling:** Provides meaningful error messages for failed analysis attempts.
- **Modular Design:** Easily extendable and maintainable code structure.

## Installation

To set up AvocadoAI, follow these steps:

1. **Clone the Repository:**
```sh
    git clone https://github.com/your-username/AvocadoAI.git
    cd AvocadoAI
```
3.	Create a Virtual Environment:
```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
```
5.	Install Dependencies:
```sh
   pip install -r requirements.txt
```
7.	Set Up API Key:
    - Ensure you have a valid API key for the Google Gemini API. Update the api_key parameter in the relevant script.
    - Update the .env file and replace "your-api-key" with your actual API key.


## Usage
For ease of end user to test the functionalities and see the results, the application is wrapped around Streamlit as its frontend. To run the application, simply use the commands below:

Make sure you are in the main directory:
```sh
cd AvocadoAI
```
Start your FastAPI server locally:
```sh
uvicorn fastapi_app:app --reload
```
Run the below command in a new terminal:
```sh
streamlit run hello.py
```

This will redirect you the port where streamlit is running. If not redirected, go to http://localhost:8501/ to view the application.

## Code Structure

The project includes the following main components:

- `analysis.py`: Script for analyzing content using the generative AI model and saving the results.
- `extraction.py`: Contains the `extract_data()` function for data extraction.
- `requirements.txt`: Lists all Python dependencies required for the project.
- `fastapi_app`: Contains the FastAPI endpoint created.
- `articles.json`: Output file where analyzed data is stored.
- `hello.py`: The main file which should be executed and consists of the Streamlit frontend.

## Approach

- ### Data Extraction
    The project starts with the extraction of article data using the `extraction.py` script. This script fetches and prepares the data for analysis.

- ### Generative AI Analysis
    Utilizing Google's Gemini API, the `analysis.py` script analyzes the extracted texts. The AI model identifies named entities and key phrases in the medical texts, providing detailed insights. The analyzed data is then saved into a JSON file for further use.

- ### Frontend Integration
    To facilitate user interaction, a Streamlit frontend (`hello.py`) is implemented. This allows users to run and test the functionalities seamlessly.

## Challenges Faced

1. **API Integration:** Integrating with the Gemini API posed initial challenges in handling responses and ensuring proper error handling.
2. **Data Serialization:** Managing the serialization of complex AI response objects into JSON format required careful structuring.
3. **Scalability:** Designing the system to handle a large volume of articles and ensuring efficient processing was a key challenge.
4. **Data Scraping:** Extracting data from medical blogs was challenging as the text was not directly accessible through normal HTML parsers. We had to implement custom scraping methods to accurately retrieve the content.

## Ideas for Scaling the System

1. **Parallel Processing:** Implement parallel processing to handle multiple article analyses simultaneously, reducing overall processing time.
2. **Cloud Deployment:** Deploy the system on a cloud platform to leverage scalable resources and handle increased load efficiently.
3. **Enhanced Caching:** Implement caching mechanisms to store intermediate results and reduce redundant processing.
4. **API Rate Limiting:** Introduce rate limiting and batching for API requests to manage quota limits effectively and ensure smooth operation.

## Conclusion

AvocadoAI presents a powerful tool for analyzing medical texts using advanced AI models. Despite the challenges faced, such as API integration and data scraping, the project successfully demonstrates the potential of leveraging AI for detailed text analysis. With further enhancements and scalability considerations, AvocadoAI can evolve into a robust solution for large-scale text analysis tasks.
