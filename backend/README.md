# Backend for chatbot  
* Navigate to the backend's root dir (/backend) and create a virtual environment for this service: ```python -m venv venv```
* Start the virtual environment: ```source venv/bin/activate```
* Install requirements: ```pip install -r requirements.txt```
* Run the server: ```uvicorn app.main:app --reload```