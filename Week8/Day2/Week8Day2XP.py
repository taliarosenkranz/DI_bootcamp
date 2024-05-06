import dataclasses
import string
from nltk.tokenize import word_tokenize
import nltk
import json
import spacy
from nltk.corpus import stopwords
from nltk.corpus import stopwords
import string
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec


# Read the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)
    #print(data)

data = [
        "At McDonald's the food was ok and the service was bad.",
        "I would not recommend this Japanese restaurant to anyone.",
        "I loved this restaurant when I traveled to Thailand last summer.",
        "The menu of Loving has a wide variety of options.",
        "The staff was friendly and helpful at Google's employees restaurant.",
        "The ambiance at Bella Italia is amazing, and the pasta dishes are delicious.",
        "I had a terrible experience at Pizza Hut. The pizza was burnt, and the service was slow.",
        "The sushi at Sushi Express is always fresh and flavorful.",
        "The steakhouse on Main Street has a cozy atmosphere and excellent steaks.",
        "The dessert selection at Sweet Treats is to die for!"
    ]

nltk.download('punkt')
nltk.download('stopwords')


def preprocess_text(data):
    lemmatizer = WordNetLemmatizer()
    # Tokenize the text and convert to lowercase
    tokenized_data = [word_tokenize(sentence.lower()) for sentence in data]
    # Remove punctuation
    no_punct_data = [[word for word in sentence if word not in string.punctuation] for sentence in tokenized_data]
    # Lemmatize words
    lemmatized_data = [[lemmatizer.lemmatize(word) for word in sentence] for sentence in no_punct_data]
    # Join the lemmatized words into strings
    preprocessed_data = [" ".join(sentence) for sentence in lemmatized_data]
    
    return preprocessed_data
preprocessed_data = preprocess_text(data)
print("preprocessing:", preprocessed_data)
#3
def perform_ner(text):
    # Load the SpaCy model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Extract entities and their labels
    entities_text = [entity.text for entity in doc.ents]
    entities_label = [entity.label_ for entity in doc.ents]
    
    return entities_text, entities_label

# Example usage:
text = "Apple is headquartered in Cupertino, California. It was founded by Steve Jobs."
entities_text, entities_label = perform_ner(text)
print("Entities Text:", entities_text)
print("Entities Label:", entities_label)

def perform_pos_tagging(text):
    nltk.download('averaged_perceptron_tagger')
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Perform POS tagging
    pos_tags = nltk.pos_tag(words)
    
    return pos_tags

# Example usage:
text = "Hi. This is some sentence."
pos_tags = perform_pos_tagging(text)
print(pos_tags)

def perform_pos_tagging(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Perform POS tagging
    pos_tags = nltk.pos_tag(words)
    
    return pos_tags

# Example usage:
text = "Lorem Ipsum Some Sentence."
pos_tags = perform_pos_tagging(text)
print(pos_tags)

nltk.download('tagsets')
nltk.help.upenn_tagset('NN')

# Apply POS tagging on preprocessed data
preprocessed_pos_tags = [perform_pos_tagging(" ".join(review)) for review in preprocessed_reviews]

# Apply POS tagging on raw data
raw_pos_tags = [perform_pos_tagging(review) for review in data["Review"]]

# Print POS tags for the first review in preprocessed and raw data
print("POS tags for the first review in preprocessed data:")
print(preprocessed_pos_tags[0])

print("\nPOS tags for the first review in raw data:")
print(raw_pos_tags[0])

#PART 2
word2vec_model = Word2Vec(sentences=preprocessed_data, vector_size=100, window=5, min_count=1, workers=4)

# Print dimensions of the Word2Vec model
print("Dimensions of Word2Vec model:", word2vec_model.wv.vector_size)

# Analysis
# The vector dimensions represent the size of the feature vectors used to represent each word in the model.
# In this case, we have chosen the vector size to be 100.
# Each word in the vocabulary will be represented as a dense vector of length 100.
# These vectors are learned during the training process and capture semantic similarities between words.
