#!/bin/bash

# Evaluate the trained fastText model

# Specify model and test data paths
# Adjust these paths to point to your actual model and test data
MODEL="./model/europarl_model.bin"
TEST="./data/europarl.csv"

# Path to the fastText executable
# Replace this with the actual path to your fastText executable if it's different
FASTTEXT_EXEC="./fastText/fasttext"

# Run the evaluation
$FASTTEXT_EXEC test $MODEL $TEST

echo "Model evaluation completed."
