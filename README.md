# Methods Used:
1- Finetuned Phi3
2- Rag App Using LangChain
3- Using Agent

## 1- Finetuning:
           Well my original Idea was to to finetune Llama3-7b on the dataset and then use that finetuned model as llm in Rag Application to answer the query. As we all know nothing goes as planned in this acursed world. I finetuned the model but when the time comes to deploy it on hugging face, I got short on GPU-Ram and whole 4-5 hours went for nothing. Well I never thought 16 gpu ram would last this much. So then I search for other models and then I find Phi3-mini(3b parameters model) which is also really good. So then I finetuned that model and deploy it on hugging face so that I can use that model in rag pipeline.

## 2- Rag PipeLine:
           
