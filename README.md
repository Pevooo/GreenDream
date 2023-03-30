# GreenDream

kaggle dataset used: https://www.kaggle.com/datasets/mostafaabla/garbage-classification (we used only 8 types)

### 1.How to use:
1.1 Download all of the source code included in the reposatory.

1.2 python3 with libraries Flask, Tensorflow, numpy, scikit-learn, cv2, flask, firebase_admin is required.

1.3 After installing the libraries, open cmd in Green Dream directory (the root directory) and type "flask run" without the quotes.

1.4 Open the link that will be displaye after clicking Enter.

### 2.Files:
app.py: The python file that has all the backend and firebase related code.

helpers.py: A small python file with some useful functions

predict.py: The python file that has the function responsible for loading the model, reading the image, resizing it, and classifying the image.

green-dream-56ce5-firebase-adminsdk-33z10-b31fb21b8e.json: The firebase key.

8-cat-66.h5: The model used for classifying images.

/templates: Has the html of the web application.

/static: Has the JavaScript, CSS and images used in the web application.

/ml: includes train.py which was used in training the model (to test train.py, download the dataset we used from kaggle (https://www.kaggle.com/datasets/mostafaabla/garbage-classification), and include the dataset folder with train.py with the name "dataset" and label each garbage type to a number starting from 0.

### 3.How it works:
3.1 The user is introduced to our homepage

3.2 The user can log in or register (The accounts information is stored in firebase realtime database).

3.3 After logging in, the user can make an order by clicking on 'order' on the navbar.

3.4 The user now is asked to fill a form of the recyclable object they want to recycle.

3.5 The user can provide an image of the object they want to be recycled and the image is passed to our trained model, and the model returns the type of the object given.

3.6 The photo uploaded by the user (if any) will be uploaded to firebase storage and the order details will be stored in firebase realtime database.
