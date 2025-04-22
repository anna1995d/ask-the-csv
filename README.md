# Ask the CSV

**Ask natural language questions about your CSV files using GPT.**  
This Streamlit app lets you upload a CSV file, view a summary of its structure, and ask GPT questions about the data — all in one clean interface.



## 🔧 Features

- Upload and parse CSV files with `pandas`
- Display basic dataset properties
- Prepare dataset summary and user queries for GPT input
- Generate responses using OpenAI's Chat API
- Maintain and display session-based Q&A history
- Clear chat history on demand



## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ask-the-csv.git
cd ask-the-csv
```

### 2. Set up the environment

Using the included `Makefile`:

```bash
make setup
```

Or manually:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure OpenAI API

Create a `.env` file in the root directory with your API key:

```
OPENAI_API_KEY=your_openai_api_key
```



## ▶️ Running the App

```bash
make run
```

Or directly:

```bash
streamlit run app.py
```



## 🛠️ Developer Utilities

```bash
make freeze     # Update requirements.txt
make format     # Format code using Black
make clean      # Remove cache and temp files
```



## 📦 Requirements

- Python 3.9+
- OpenAI account & API key
- Streamlit, pandas, openai, python-dotenv



## 🪪 License

This project is open source and available under the [MIT License](LICENSE).
