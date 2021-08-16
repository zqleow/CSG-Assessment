# CSG Assessment
This submission is for the CSG Assessment and comprises 2 parts. 

## Part 1: Online Store for Uncle Roger 

There are 2 websites that are developed and included in this repository. The crudapp folder comprises the codes for the online store where customers would be able to order food from Uncle Roger's store. The adminapp folder comprises the codes for deployment of a admin website at Uncle Roger's store where he and his staff would be able to view the orders placed by customers who ordered via the online store.The admin website also allows the updating, creation and deletion of menu items.

The backend infrastructure supporting all operations are a backend API server hosted in Heroku and a cloud database hosted in MongoDB. The source code of the API server is not included inside but can be shown during the demo/walkthrough session for better clarity. 

## Installation (crudapp)

The dependencies of the program are already documented in requirements.txt. Please install the dependencies by executing pip install requirements.txt.

```sh
pip install requirements.txt
```
## Running the program (crudapp)

Please ensure python is installed and just run the program using the command below:

```sh
streamlit run app.py
```
Please go to localhost:8501 to access the website. 

## Installation (adminapp)

The dependencies of the program are already documented in requirements.txt. Please install the dependencies by executing pip install requirements.txt.

```sh
pip install requirements.txt
```
## Running the program (adminapp)

Please ensure python is installed and just run the program using the command below:

```sh
streamlit run app.py --server.port 8503
```
Please go to localhost:8503 to access the website. 

## Part 2: Find the bad actor(s) on the network 

Answers to the questions are available in word document in this repository.
