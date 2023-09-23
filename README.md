# Language Detection Model using fastText

## Description

This project aims to build a language detection model using the fastText library. The model is trained on the European Parliament Proceedings Parallel Corpus and can identify one of 21 languages.

## Languages Supported


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
4. Run the scripts in the `scripts` folder to prepare the data and train the model.

## Scripts

- `prepare_data.sh`: Downloads and prepares the European Parliament corpus.
- `preprocess_data.py`: Cleans and preprocesses the text data.
- `train_model.sh`: Trains the fastText model.
- `evaluate_model.py`: Evaluates the trained model and makes predictions.

## Usage

To train and evaluate the model, execute the following commands in order:

1. `bash scripts/prepare_data.sh`
2. `python scripts/preprocess_data.py`
3. `bash scripts/train_model.sh`
4. `python scripts/evaluate_model.py`

## Requirements

- Python 3.x
- fastText
- pandas

