# Backend for chatbot  
* Navigate to the backend's root dir (/backend) and create a virtual environment for this service: ```python -m venv venv```
* Start the virtual environment: ```source venv/bin/activate```
* Install requirements: ```pip install -r requirements.txt```
* Make sure you create an assistant on open AI and note down your assistant id  
* Create .env file with mongo uri stored under ```MONGO_URI``` and openAI api key under ```OPENAI_API_KEY``` and your assistant id under ```OPENAI_ASSISTANT_ID```  
* Run the server: ```uvicorn app.main:app --reload```