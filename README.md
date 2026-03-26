Sentiment Analyzer App

A web application that analyzes the sentiment of text reviews using Natural Language Processing (NLP). 

Check out the live website https://sentiment-analyzer-rmic.onrender.com/

Features
* Upload a file with multiple reviews
* Automatic sentiment classification
* Outputs results with:
    * Review text
    * Sentiment score
    * Sentiment label (Positive / Negative / Neutral)
* Download results as a CSV file
* Clean and user-friendly UI

Tech Stack
* Python
* Flask
* NLTK (VADER Sentiment Analysis)
* HTML, CSS

File Input Format
* The uploaded file should contain reviews (one per line or CSV format)
* First row can be a header (it will be ignored)

How It Works
1. User uploads a file (CSV or text with reviews)
2. App reads each review
3. Uses VADER to calculate sentiment score
4. Assigns label:
    * Positive (score ≥ 0.05)
    * Negative (score ≤ -0.05)
    * Neutral (between -0.05 and 0.05)
5. Generates a new CSV file with results
6. File is downloaded automatically
