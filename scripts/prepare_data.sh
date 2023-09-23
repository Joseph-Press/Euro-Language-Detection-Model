#!/bin/bash

# Download and prepare the Europarl dataset for training and evaluation

# Create directory to store downloaded files
mkdir -p downloaded

# Download europarl dataset if it doesn't exist
target="downloaded/europarl.tgz"
if [ ! -f "$target" ]; then
    echo "Downloading Europarl dataset..."
    # Please download the dataset manually as wget is disabled in this environment
fi

# Extract the downloaded dataset
FOLDER="txt"
if [ ! -d "$FOLDER" ]; then
    tar xzf "$target"
fi

# Merge individual language files and clean up
for lang_dir in $(ls txt); do
    find txt/$lang_dir -name "*.txt" -print0 | xargs -0 cat > "txt/${lang_dir}.txt"
    rm -rf "txt/$lang_dir"
done

echo "Data preparation completed."
