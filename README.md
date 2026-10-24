
# AI Text Summarization Using Hugging Face and Streamlit

## Project Overview

AI Text Summarization is a web-based application that converts long paragraphs into short and meaningful summaries using Artificial Intelligence.

This application is developed using Python, Streamlit, and Hugging Face Transformers. It uses a pretrained DistilBART model to generate summaries automatically.

## Objectives

- To summarize long text into short and meaningful content.
- To use Hugging Face pretrained models for text summarization.
- To develop a simple and user-friendly web application using Streamlit.
- To reduce the time required to read lengthy content.

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- DistilBART Model

## Model Used

Model Name: sshleifer/distilbart-cnn-12-6

Task: Text Summarization

## Features

- Simple and user-friendly interface.
- Accepts long text as input.
- Generates short summaries automatically.
- Uses a pretrained AI model.
- Displays summarized text instantly.

## Project Structure

Text_Summarization/
- app.py
- requirements.txt
- README.md

## Installation

Step 1: Clone the repository.

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2: Open the project folder.

cd Text_Summarization

Step 3: Install the required libraries.

pip install -r requirements.txt

Step 4: Run the Streamlit application.

streamlit run app.py

## Requirements

- streamlit
- transformers<5
- torch
- sentencepiece

## How It Works

1. Open the Streamlit application.
2. Enter or paste the text into the input box.
3. Click the Generate Summary button.
4. The Hugging Face model processes the input text.
5. The summarized text is displayed on the screen.

## Applications

- Summarizing educational materials.
- Summarizing articles and reports.
- Shortening lengthy documents.
- Quick understanding of large text content.

## Conclusion

The AI Text Summarization application helps users understand lengthy content quickly by generating short and meaningful summaries. By combining Hugging Face Transformers and Streamlit, this project provides a simple and effective AI-powered summarization solution.

## Future Enhancements

- Upload PDF and text files.
- Support multiple languages.
- Add summary length selection.
- Download the generated summary.
