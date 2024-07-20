from users import User
import mysql.connector

def get_database_details():
    # Replace the placeholders with your MySQL server details
    host = 'localhost'
    user = 'root'
    password = 'root'
    database = 'appliance_mangement'

    # Establish a connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection

def fetch_data(user):
    connection=get_database_details()
    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    email=user.email
    # Example: Execute a query
    query="SELECT id FROM user_details WHERE email = %s"
    cursor.execute(query, (email,))

    # Fetch the results
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    if not results:
        return False
    else:
        return True

def store_data(user):
    connection=get_database_details()
    cursor = connection.cursor()
    name=user.name
    password=user.password
    email=user.email
    userType=user.user_type
    query="INSERT INTO `user_details` (`name`,`email`,`password`,`userType`) VALUES(%s, %s, %s, %s)"
    cursor.execute(query, (name,email,password,userType,))
    connection.commit()
    cursor.close()
    connection.close()

def isUserAvailable(user):
    connection=get_database_details()
    cursor=connection.cursor()
    email=user.email
    query="SELECT name from user_details where ('email')"
    