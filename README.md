# Chatbot  
## Backend  
* Create .env file with mongo uri stored under ```MONGO_URI``` and openAI api key under ```OPENAI_API_KEY``` and your assistant id under ```OPENAI_ASSISTANT_ID``` 
* Mongo uri should be mongodb://mongo:27017/ if you're using the mongo in the docker-compose file, otherwise use the appropriate mongo uri for your use case  
* From the root (/chatbot) directory run ```docker-compose up -d``` to run the db and backend in the background - make sure you have docker and docker-compose installed  
* For the frontend follow instructions under the README in the frontend directory