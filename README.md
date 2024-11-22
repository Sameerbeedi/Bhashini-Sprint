# Emotion Recognition from Text<br>
## Overview : <br>
This project aims to recognize emotions from text. The dataset consists of various text entries, each labeled with an emotion. The project involves preprocessing the text data and using a neural network model to predict the emotion of a given phrase.<br>
## Dataset:<br>
The dataset contains different text entries, each labeled with an emotion. The preprocessing step includes ignoring words that do not repeat in phrases more than 10 times. This helps in building a more robust model by focusing on more frequent terms.<br>
## Preprocessing:<br>
Words that appear in phrases less than 10 times are ignored.<br>
The remaining words are used to build the model.<br>
## Model:<br>
A neural network model is used for emotion recognition. The model is trained on the preprocessed dataset.<br>
## Testing:<br>
When the model is tested with a phrase, it provides the output in terms of the percentage of each emotion present in the phrase.<br>
## Usage<br>
### Preprocessing:<br>
- Load the dataset.
- Run the preprocessing file 
### Model Training:<br>
- Train the neural network model on the preprocessed data.
### Emotion Recognition:<br>
- Input a phrase to the model.
- Get the emotion prediction in percentages.
