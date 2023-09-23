# Language Detection Model using fastText

## Description

This project aims to build a language detection model using the fastText library. The model is trained on a modified version of the European Parliament Proceedings Parallel Corpus and can identify 11 languages.

- Danish (da)
- Dutch (nl)
- English (en)
- Finnish (fi)
- German (de)
- Greek (el)
- Italian (it)
- Portuguese (pt)
- Spanish (es)
- Swedish (sv)
- Spanish (es)

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install the requirements using `pip install -r requirements.txt`.
4. Download the data from [here](http://www.statmt.org/europarl/). Alternatively use the csv files in the `data` folder.
5. Run the scripts in the `scripts` folder to prepare the data and train the model.

## Scripts

- `evaluate_model.py`: Evaluates the trained model and makes predictions.
- `predict.py`: Makes predictions on the test data.
- `preprocess_data.py`: Cleans and preprocesses the text data.
- `train_model.sh`: Trains the fastText model.

## Requirements

- Python 3.x
- fastText
- pandas

