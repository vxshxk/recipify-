# Recipify

A Computer Vision based application to detect food ingredients uploaded as image data and then suggest recipes based on the same, along with nutritional information and suggestions

----------------------------------------------------------------------------

## Installation

### Local Installation

1. Clone the repository with 
```
git clone https://github.com/vxshxk/recipify.git
```
2. Install the required packages with the command
```
python -m pip install -r requirements.txt
```
5. `cd` into the `recipify/` directory
6. Copy the environment file by doing
```
cp env.example .env
```
8. Get API keys from [Unsplash](https://unsplash.com/developers) and [Gemini](https://ai.google.dev/) and past them in the .env file
9. To do the migrations, enter the command (needs to be entered only once)
```
python manage.py migrate
```
7. To run the server, enter the command (needs to be entered everytime the app server is to be started)
```
python manage.py runserver
```
8. Head to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) to see the webpage

### Docker Installation

1. Clone the repository with 
```
git clone https://github.com/vxshxk/recipify.git
```
2. Enter the command to start up the docker container
```
docker compose up
```
3. Head to [`http://127.0.0.1:8000`](http://127.0.0.1:8000) to see the webpage

----------------------------------------------------------------------------
## Contributing
1. Make a new branch for every single change, do NOT push to main
2. Once all your changes are done, make a pull request to main
3. Request approval from necessary contributors
4. Pray for it to be merged

----------------------------------------------------------------------------
## References
1. [Django Documentation](https://docs.djangoproject.com/en/5.0/)
2. [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
3. [Unsplash API Documentation](https://unsplash.com/documentation)



