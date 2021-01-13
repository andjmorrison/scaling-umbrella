# Getting Started
1. Clone this repo. It contains:

     * a .gitignore file for Python.
     * a requirements.txt to tell Heroku what your libraries your app needs.
     * a Procfile to tell how Heroku how to run your app.

2. Create an .env file and add your database settings to it:
```python
MONGO_URI = "<MongoDatabaseConnectionString>"
```

2. Create a new conda environment:
```python
conda create -n <NewEnvironmentName> python=3.6
```
3. Activate the new environment:
```python
conda activate <NewEnvironmentName>
```

4. Install libraries in the new environment:
```python
pip install flask
pip install flask-pymongo
pip install gunicorn
pip install dnspython
pip install python-dotenv
```

5. Test the application locally:
```
python app.py
```

6. Setup a database in the cloud:

   [MongoDB Atlas](https://www.mongodb.com/atlas) (use the free option)

7. Create Heroku account.

   [Heroku](https://www.heroku.com)

8. Create a new app in Heroku.

9. In Heroku in your app settings you'll find:
     * your git path.
     * config variables.
     * your app URL.

10. Add a remote for Heroku to your repo:

```
git remote add heroku <path to your Heroku git>
```

11. Deploy your app to Heroku:

```
git push heroku master
```
