# Makefile for ask-the-csv

# Create virtual environment and install dependencies
setup:
	python3 -m venv venv
	source venv/bin/activate && pip install -r requirements.txt

# Run the Streamlit app
run:
	source venv/bin/activate && streamlit run app.py

# Freeze current dependencies into requirements.txt
freeze:
	pip freeze > requirements.txt

# Clear .pyc and cache files 
clean:
	rm -rf __pycache__ .streamlit/*.json
