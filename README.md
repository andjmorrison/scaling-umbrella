# Getting Started
1. Clone this repo. It contains:

     * a .gitignore file for Python
     * a requirements.txt to tell Heroku what your libraries your app needs
        * you will generate your own req file below
     * a Procfile to tell how Heroku how to run your app

2. Create an .env file and add your database settings:
```python
MONGO_URI = "<MongoDatabaseConnectionString>"
```

3. Create a new conda environment:
```python
conda create -n <NewEnvironmentName> python=3.6
```
4. Activate the new environment:
```python
conda activate <NewEnvironmentName>
```

5. Install libraries in the new environment/generate requirements file:
```python
pip install flask
pip install flask-pymongo
pip install gunicorn
pip install dnspython
pip install python-dotenv
pip freeze <NewEnvironmentName> > requirements.txt
```

6. Test the application locally:
```
python app.py
```

7. Setup a database in the cloud:

   [MongoDB Atlas](https://www.mongodb.com/atlas) (use the free option)

8. Create Heroku account.

   [Heroku](https://www.heroku.com)

9. Create a new app in Heroku.

10. In Heroku in your app settings you'll find:
     * config variables.
     * your app URL.

11. Add your config variable

```
MONGO_URI = "<MongoDatabaseConnectionString>"
```

12. Deploy your app to Heroku using the CLI or connect to your GitHub repo.
    * using the web-interface and connecting a GitHub repo will "build" whatever you push to that repo, which is why we need a Procfile.

*If you're having trouble, see the [Heroku documentation](https://devcenter.heroku.com/articles/getting-started-with-python).*
