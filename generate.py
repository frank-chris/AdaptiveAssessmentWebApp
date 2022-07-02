from vae.generate_qa import get_qa
import pandas as pd
from transformers import BertTokenizer
from ast import literal_eval

args_bert_model = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(args_bert_model)

df = pd.read_csv('data/adaptive_assess_1.csv')

contexts = []

for i in ['history', 'geography', 'economics']:
    for j in range(3):
        contexts.append(literal_eval(df[i][j])[0])

contexts, questions, answers = get_qa(contexts, tokenizer)

new_df = pd.DataFrame()

new_df['context'] = contexts
new_df['question'] = questions
new_df['answer'] = answers

new_df.to_csv('data/generated.csv')
