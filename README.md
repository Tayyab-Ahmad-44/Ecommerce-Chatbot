# Methods Used:
Finetuned Phi3 \n
RAG App Using LangChain \n
Using CSV-Agent
## 1. Finetuning:
My original idea was to finetune Llama3-7b on the dataset and then use that finetuned model as an LLM in the RAG application to answer queries efficiently. As we all know, nothing ever goes as planned in this cursed world 😅. I finetuned the model, but when it came time to deploy it on Hugging Face, I ran short on GPU RAM, and the whole 4-5 hours went for nothing. I never thought 16 GB of GPU RAM would be insufficient. So, I searched for other models and found Phi3-mini (3B parameters), which is also really good. I then finetuned that model and deployed it on Hugging Face so that I could use it in the RAG pipeline.

## 2. RAG Pipeline:
This is what I used in the deployed model as well. Here, I converted the dataset from JSON to CSV for ease of use. Then, I created vector embeddings and set up a retriever and chain. However, when the time came to use my finetuned model, I faced some issues 😩. My deployed model was slow as a snail. There was a way to make the Inference API for my finetuned model on Hugging Face, but unfortunately, it was charging $10, which is quite a lot. So, I decided to move forward, leaving my model behind and used the Llama3-70B parameter model. Thanks to Groq API, which helped me a lot in finishing the task quickly 🙌.

## 3. Using CSV-Agent:
One of the methods that came to mind was using a CSV or PD agent in LangChain. This was the easiest way I found to complete this task, but after using it, I found it slower than our RAG model. So, I decided to leave that behind; there was no fun in using the agent 🤷‍♂️.

# User Interface:
The UI is made using Streamlit due to its simplicity and time management. It's just a simple user interface where the user has to write a query in the text field and click a button—that's all, and you will get the desired answer to your question.

# Deployment:
The real fun began there. Before that, I was already acquainted with how to deploy a Streamlit website using App Service in Azure and Streamlit Cloud. I had two options in Azure: either create a Dockerfile and upload it or let the cloud do that work for you by providing a GitHub repo. It’s not like I wasn’t familiar with Docker (I used Docker in a semester project), but I chose option 2 because time was short and things were getting complicated. Everything was going well, but it was the first time I faced an error in deploying a web application (I had never seen that before) 😳, and I didn’t know what it was. If I had known, I might have been able to solve it. Anyhow, here is the link to the website if you want to visit: "https://tayyabmaktek.azurewebsites.net/".

Then I went with my last but not least option, which was to deploy it on Streamlit Cloud. After some time, I was able to accomplish that. Here is the link if you want to visit: "https://tayyab-maktek.streamlit.app/".

# Conclusion
The most efficient way that I found was to use finetuning because, in a website or any other place where users ask something from a chatbot, the most important factor is response time ⏱️. The latency of the finetuned model is very good, making it ideal for this type of application. However, I finetuned the model, but unfortunately, I wasn't able to integrate it into the chatbot due to a lack of resources. We can also use RAG here for simplicity.

