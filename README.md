# Users-Management
A simple Dockerized app for managing users.
This is a simple Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API.

## Requirements
* Python 3.11
* Docker 

## Setup
1. Clone the repository:

   `git clone https://github.com/your_username/users-management.git`

   `cd users-management`

2. Create a new Python virtual environment and activate it:

   `python3 -m venv venv`

   `source venv/bin/activate`  

On Windows, use ``venv\Scripts\activate``


## MongoDB Setup
1. Headover to the link `https://cloud.mongodb.com/` and create a mongodb account.
2. Choose free tier(Possibly) and create a cluster
3. Copy the connection string by clicking the connect button which shiuld be pasted in the .env file
4. Create a database(Here, Users) and a collection (Here, users)

   Or,

1. Install MongoDB on your machine if you haven't already. You can download it from the official website: `https://www.mongodb.com/try/download/community`

2. Create a new MongoDB database and collection for the application. You can use MongoDB Compass or any MongoDB management tool to do this.

## env setup
1. Create a file called .env which should resemble .env.sample and the values should be replaced with your original values
   
## Running the Application

1. Build the Docker container:

   `sudo docker build -t users .`

2. Run the Docker container:

   `sudo docker run users`

The application will start running on http://<ip>:5001. The url will be specified in the terminal.

