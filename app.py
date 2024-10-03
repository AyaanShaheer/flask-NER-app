from flask import Flask, render_template, request
import spacy

# Initialize the Flask app
app = Flask(__name__)

# Load the spaCy pre-trained NER model
nlp = spacy.load("en_core_web_sm")

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and perform NER
@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        # Get the input text from the form
        input_text = request.form['text']
        
        # Perform NER using spaCy
        doc = nlp(input_text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        # Render the result
        return render_template('result.html', entities=entities, text=input_text)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
