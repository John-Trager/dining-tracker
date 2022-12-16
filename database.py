# database.py

import csv

user_params = ['id','name', 'plates','bowls','cups', 'mugs']

class Database:
    def __init__(self, filename):
        self.filename = filename
        self.last_id = 0

    def read_users(self):
        # Open the CSV file in read mode
        with open(self.filename, 'r') as csv_file:
            # Create a CSV reader
            reader = csv.reader(csv_file)

            # Read the rows from the CSV file
            rows = list(reader)

            # Update the last user ID
            if rows:
                self.last_id = int(rows[-1][0])

            # Return the rows as a list of users
            return rows

    def add_user(self, user):
        # Generate a new user ID
        self.last_id += 1
        user_id = self.last_id

        # Add the user ID to the user data
        user = [user_id] + user

        print("user created:")
        print(user)

        # Open the CSV file in append mode
        with open(self.filename, 'a') as csv_file:
            # Create a CSV writer
            writer = csv.writer(csv_file)

            # Write the user to the CSV file
            writer.writerow(user)

    def delete_user(self, user_id):
        # Read the users from the CSV file
        users = self.read_users()

        # Remove the user from the list of users
        users = [user for user in users if int(user[0]) != int(user_id)]

        # Open the CSV file in write mode
        with open(self.filename, 'w') as csv_file:
            # Create a CSV writer
            writer = csv.writer(csv_file)

            # Write the updated list of users to the CSV file
            writer.writerows(users)


    def modify_user(self, user, val, param):

        # Read the users from the CSV file
        users = self.read_users()

        param_index = user_params.index(param)
        id_index = user_params.index('id')
        # read in user ID
        print(user, id_index, user[id_index], type(user))
        user_id = user[id_index]

        print("modify user method")
        for u in users:
            # if user ids match 
            if int(u[id_index]) == int(user_id) and (int(val) + int(u[param_index])) >= 0:
                print("modified user:", user)
                u[param_index] = int(val) + int(u[param_index])
                print(user)

        # Open the CSV file in write mode
        with open(self.filename, 'w') as csv_file:
            # Create a CSV writer
            writer = csv.writer(csv_file)

            # Write the updated list of users to the CSV file
            writer.writerows(users)