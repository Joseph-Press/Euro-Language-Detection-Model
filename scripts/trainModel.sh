#!/bin/bash

# Compile and train the fastText model

# Navigate to fastText directory and compile the source code
# Commented out due to environment limitations
# cd fastText/
# make

# Train the fastText model
TRAIN="data/europarl.train"
MODEL_OUTPUT="model/europarl_model"
./fastText/fasttext supervised -input $TRAIN -output $MODEL_OUTPUT

echo "Model training completed."
