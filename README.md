# 📧 Cold Email Generator

An AI-powered Cold Email Generator that automatically extracts job details from career pages and generates personalized outreach emails using Large Language Models (LLMs).

## 🚀 Features

* Extracts job descriptions directly from career page URLs
* Uses LangChain and Groq Llama models for intelligent email generation
* Performs semantic portfolio matching using ChromaDB
* Generates personalized cold emails tailored to job requirements
* Implements in-memory caching to reduce redundant LLM calls
* Implements rate limiting to prevent excessive API usage
* Interactive Streamlit web interface

## 🛠️ Tech Stack

* Python
* LangChain
* Groq API
* Llama 3.3 70B Versatile
* ChromaDB
* Streamlit
* Pandas
* BeautifulSoup
* Python Dotenv


## 📂 Project Structure

cold-email-generator/
│
├── chains.py
├── main.py
├── portfolio.py
├── utils.py
├── my_portfolio.csv
├── requirements.txt
├── .env.example
├── README.md
│
├── vectorstore/
├── venv/
└── __pycache__/

## ⚙️ Installation

### Clone Repository

git clone <your-repository-url>
cd cold-email-generator


### Create Virtual Environment


python -m venv venv


### Activate Virtual Environment

Windows:


venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


### Install Dependencies

pip install -r requirements.txt


Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

Example template:

```env
GROQ_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxx


Start the Streamlit application:


streamlit run main.py


The application will be available at:


http://localhost:8501

1. User enters a job posting URL.
2. The application scrapes the job description.
3. LangChain extracts structured job information.
4. ChromaDB identifies the most relevant portfolio projects.
5. Llama 3.3 generates a personalized cold email.
6. Responses are cached to reduce repeated LLM requests.
7. Rate limiting prevents excessive API calls.

Job URL
   ↓
Web Scraping
   ↓
Job Extraction
   ↓
ChromaDB Retrieval
   ↓
LLM Email Generation
   ↓
Personalized Cold Email


Rakesh

AI & Software Engineering Enthusiast
