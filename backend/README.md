# Backend for chatbot  
* Navigate to the backend's root dir (/backend) and create a virtual environment for this service: ```python -m venv venv```
* Start the virtual environment: ```source venv/bin/activate```
* Install requirements: ```pip install -r requirements.txt```
* Create .env file with mongo uri stored under ```MONGO_URI``` and openAI api key under ```OPENAI_API_KEY```  
* Make sure you create an assistant on open AI and update the assistant id in the code  
* Run the server: ```uvicorn app.main:app --reload```