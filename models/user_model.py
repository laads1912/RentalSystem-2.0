import sqlite3

class UserModel:
    def __init__(self, db_name='RentalSystem.db'):
        self.db_name = db_name

    def create_user(self, user_data):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO Users (email, full_name, age, gender, height, weight, shoe_size, is_active, is_employee, password_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', user_data)

        conn.commit()
        conn.close()