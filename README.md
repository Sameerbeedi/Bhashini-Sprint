Emotion Recognition from Text


Overview : 
This project aims to recognize emotions from text. The dataset consists of various text entries, each labeled with an emotion. The project involves preprocessing the text data and using a neural network model to predict the emotion of a given phrase.

Dataset
The dataset contains different text entries, each labeled with an emotion. The preprocessing step includes ignoring words that do not repeat in phrases more than 10 times. This helps in building a more robust model by focusing on more frequent terms.

Preprocessing
Words that appear in phrases less than 10 times are ignored.
The remaining words are used to build the model.
Model
A neural network model is used for emotion recognition. The model is trained on the preprocessed dataset.

Testing
When the model is tested with a phrase, it provides the output in terms of the percentage of each emotion present in the phrase.

Usage
Preprocessing:

Load the dataset.
Apply preprocessing to filter out infrequent words.
Model Training:

Train the neural network model on the preprocessed data.
Emotion Recognition:

Input a phrase to the model.
Get the emotion prediction in percentages.
