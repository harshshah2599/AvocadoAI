# AvocadoAI 🥑

AvocadoAI is a cutting-edge app aimed at leveraging advanced generative AI models to analyze and extract meaningful insights from article texts focusing on medical blogs online. The project includes functionalities to process data, interact with AI models, and store analysis results.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)


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
    Ensure you have a valid API key for the Google Gemini API. Update the api_key parameter in the relevant script.
    Update the .env file and replace "your-api-key" with your actual API key.


## Usage
For each end user to test the functionalities and see the results, the application is wrapped around Streamlit as its frontend. To run the application, simply use the command below:

```sh
streamlit run hello.py
```

## Code Structure

The project includes the following main components:

- `analysis.py`: Script for analyzing content using the generative AI model and saving the results.
- `extraction.py`: Contains the `extract_data()` function for data extraction.
- `requirements.txt`: Lists all Python dependencies required for the project.
- `fastapi_app`: Contains the FastAPI endpoint created.
- `articles.json`: Output file where analyzed data is stored.
- `hello.py`: The main file which should be executed and consists of the Streamlit frontend.
