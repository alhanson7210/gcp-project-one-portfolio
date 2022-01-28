# My Portfolio website


<!-- TODO: Insert the link in between the parenthesis -->
👋  Hi! I'm Alex Hanson. I'm a programmer from [Los Angeles, United States](https://www.google.com/maps/place/Los+Angeles,+CA/@34.0201613,-118.6919205,10z/data=!3m1!4b1!4m5!3m4!1s0x80c2c75ddc27da13:0xe22fdf6f254608f4!8m2!3d34.0522342!4d-118.2436849).  

This is the repository for [my portfolio](#). 

<br>

## The project
### Technologies used
I've used the following technologies:
- [Google App Engine](https://cloud.google.com/appengine/docs/overview)
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)

## The app
The app is a simple website that I built to showcase my skills. It is a single page application that uses the [Flask](https://flask.palletsprojects.com/) framework. The app is deployed on Google App Engine. 

I've set some variables in `main.py` to make it easier to maintain the app. 

The variables are: 
- name
- role
- phone
- email
- location

## Folder structure
- Templated html files are located in `./templates/`
- App engine configuration is located in `./app.yaml` 
- The Flask code is located in `./main.py`
- Images are located in `./static/images/`
- My resume is located in `./General_Hanson_Alex_2021_Resume.pdf`

## Deployment
To deploy this app **live**:
- From a terminal, with Google Cloud SDK or from the Google Cloud Shell, run:
  ```
  gcloud app deploy
  ```

To test this app **locally**:
- From a terminal, run:
  ```
  python main.py
  ```

From a local machine:
- Create a virtual environment:
  ```
  python3 -m venv env
  ```  
- Activate the virtual environment:
    ```
    source env/bin/activate
    ```
- Install dependencies:
    ```
    pip install -r requirements.txt
    ```
- Run the app:
    ```
    python main.py 
    ```
    The url for the app will be displayed in the terminal (e.g.  Running on http://127.0.0.1:5000/ and ctrl + c to stop).
- Deactivate the virtual environment:
    ```
    deactivate
    ```
