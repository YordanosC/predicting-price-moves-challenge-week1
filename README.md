Financial News Sentiment Analysis
This project analyzes the Financial News and Stock Price Integration Dataset (FNSPID) to explore correlations between news sentiment and stock price movements for Nova Financial Solutions.
Project Structure
financial-news-analysis/
├── .gitignore
├── requirements.txt
├── README.md
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── src/
│   ├── __init__.py
├── notebooks/
│   ├── __init__.py
│   ├── README.md
│   ├── eda.ipynb
├── tests/
│   ├── __init__.py
├── scripts/
│   ├── __init__.py
│   ├── README.md
├── data/
│   ├── fnspid.csv

Setup

Clone Repository:git clone https://github.com/YordanosC/predicting-price-moves-challenge-week1
cd predicting-price-moves-challenge-week1


Set Up Virtual Environment:python -m venv env


Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate


Install Dependencies:pip install -r requirements.txt


Run EDA:jupyter notebook notebooks/eda.ipynb



Tasks

Task 1: Git setup, EDA (descriptive stats, text analysis, time series, publisher analysis).
Task 2: Technical indicators (MA, RSI, MACD) using TA-Lib, PyNance.
Task 3: Sentiment analysis (NLTK, TextBlob), Pearson correlation between sentiment and stock returns.

References

Pandas
NLTK
TextBlob
TA-Lib
PyNance

