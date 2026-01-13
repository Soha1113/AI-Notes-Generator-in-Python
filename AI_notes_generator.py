# ---------------------------------------------
# AI NOTES GENERATOR USING PYTHON
# ---------------------------------------------

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download required NLTK resources (run once)
nltk.download('punkt')
nltk.download('stopwords')


def preprocess_text(text):
    """
    Cleans and preprocesses input text
    """
    # Convert text to lowercase
    text = text.lower()

    # Tokenize words
    words = word_tokenize(text)

    # Remove punctuation and stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [
        word for word in words
        if word not in stop_words and word not in string.punctuation
    ]

    return filtered_words


def calculate_word_frequency(words):
    """
    Calculates frequency of each word
    """
    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1

    return word_frequency


def score_sentences(sentences, word_frequency):
    """
    Scores sentences based on word frequency
    """
    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequency:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequency[word]
                else:
                    sentence_scores[sentence] += word_frequency[word]

    return sentence_scores


def generate_notes(text, num_sentences=5):
    """
    Generates summarized notes
    """
    # Tokenize sentences
    sentences = sent_tokenize(text)

    # Preprocess text
    processed_words = preprocess_text(text)

    # Word frequency calculation
    word_frequency = calculate_word_frequency(processed_words)

    # Sentence scoring
    sentence_scores = score_sentences(sentences, word_frequency)

    # Sort sentences by score
    summarized_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )

    # Select top sentences
    notes = summarized_sentences[:num_sentences]

    return " ".join(notes)


# ---------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------

if __name__ == "__main__":
    print("===== AI NOTES GENERATOR =====\n")
    print("Enter/Paste your text below.")
    print("Type 'END' on a new line to finish input.\n")

    # Take multi-line input
    user_input = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        user_input.append(line)

    input_text = " ".join(user_input)

    notes = generate_notes(input_text, num_sentences=4)

    print("\n----- GENERATED NOTES -----\n")
    print(notes)