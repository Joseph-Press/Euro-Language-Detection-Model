import fasttext

# Load the trained model
model = fasttext.load_model('model/europarl_model.bin')

# Sample sentences in different languages
sample_sentences = [
    "This is very cool.",  # English
    "esto es genial.",     # Spanish
    "isso é legal.",       # Portuguese
    "това е готино.",      # Bulgarian
    "det her er sejt."     # Danish
]

# Make predictions
predictions = model.predict(sample_sentences)
for sentence, label in zip(sample_sentences, predictions[0]):
    print(f"Sentence: {sentence}")
    print(f"Predicted label: {label[0]}")
