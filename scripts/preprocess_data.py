import pandas as pd
import re
import numpy as np

# clean text
def clean_text(text):
    return re.sub(r'<.*?>', '', text).lower()

# convert corpus to DataFrame
def corpus_to_df(filepath, lang):
    df = pd.read_table(filepath, error_bad_lines=False, header=None, names=['text'])
    df['lang'] = lang
    return df[['lang', 'text']]

# prepare text for fastText
def normalize_text(row):
    label = '__label__' + row['lang']
    text = row['text']
    return f"{label} , {text}"

# convert each language file to a CSV
languages = [lang.replace('.txt', '') for lang in os.listdir('txt/') if lang.endswith('.txt')]

for lang in languages:
    filepath = f'txt/{lang}.txt'
    print(f"Processing {filepath}...")
    
    # clean text
    with open(filepath, 'r') as f:
        cleaned_text = clean_text(f.read())
    
    # save text
    cleaned_filepath = filepath.replace('.txt', '-cleaned.txt')
    with open(cleaned_filepath, 'w') as f:
        f.write(cleaned_text)

    # convert to DataFrame and save as CSV
    df = corpus_to_df(cleaned_filepath, lang)
    df.to_csv(f'data/csv/{lang}.csv', index=False, header=False)

    print(f"Finished processing {filepath}.")

# concatenate samples from each language to create a large dataset
samples_per_lang = 40000
combined_df = pd.concat([
    pd.read_csv(f"data/csv/{lang}.csv", names=['lang', 'text']).sample(samples_per_lang, random_state=1)
    for lang in languages
], ignore_index=True)

# shuffle, normalize, and split the dataset
combined_df = combined_df.sample(frac=1, random_state=1).reset_index(drop=True)
combined_df['normalized'] = combined_df.apply(normalize_text, axis=1)

# slpit into training and test sets
split_idx = int(0.75 * len(combined_df))
train_df = combined_df.loc[:split_idx, 'normalized']
test_df = combined_df.loc[split_idx:, 'normalized']

# save training and test sets
train_df.to_csv('data/europarl.train', index=False, header=False)
test_df.to_csv('data/europarl.test', index=False, header=False)

print("Data preprocessing completed.")
