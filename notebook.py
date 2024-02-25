!huggingface-cli login
from transformers import pipeline 
classifier = pipeline("sentiment-analysis")
res = classifier("i'm good")
print(res)  
