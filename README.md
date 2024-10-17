# Text Summarization Tool

This is a web-based **Text Summarization Tool** that leverages the power of advanced Natural Language Processing (NLP) models to summarize long pieces of text, such as articles or documents, into concise summaries. The tool allows users to input a block of text and receive a shortened, summarized version based on customizable parameters.

## Features
- Summarizes large blocks of text into shorter, meaningful summaries.
- Allows users to specify the minimum and maximum length of the summary.
- Uses state-of-the-art NLP models for accurate and fluent summarization.
- Simple web interface built with Flask.
- Supports **BART** (Facebook's `bart-large-cnn`) as the default summarization model.
- Easy to switch to other models like **T5** for different summarization approaches.

## Technologies Used
- **Python**: Main programming language.
- **Flask**: Lightweight web framework to create the frontend and backend.
- **Hugging Face Transformers**: For using pre-trained models like BART and T5.
- **PyTorch**: Backend for model execution and inference.

## Pre-Trained Models
The summarization is powered by the following pre-trained models available on Hugging Face:
- **BART (Bidirectional and Auto-Regressive Transformers)**: We use the `facebook/bart-large-cnn` model, which is fine-tuned for summarization tasks.
- **T5 (Text-to-Text Transfer Transformer)**: You can switch to this model by changing a line in the code to try another approach to text summarization.

## Installation

To run this project on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/text-summarization-tool.git
   cd text-summarization-tool
