from flask import Flask, request, render_template
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load summarization model (BART or T5)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Use T5 if needed

# Define home page route
@app.route('/')
def home():
    return render_template('index.html')

# Define route for summarization
@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        input_text = request.form['input_text']
        # Define max and min summary length
        min_length = int(request.form['min_length'])
        max_length = int(request.form['max_length'])
        
        # Perform summarization
        summary = summarizer(input_text, min_length=min_length, max_length=max_length, do_sample=False)
        return render_template('index.html', input_text=input_text, summary=summary[0]['summary_text'])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
