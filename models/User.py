import sqlite3

class User:
    def __init__(self, age, email, full_name, gender, height, password_hash, shoe_size, weight):
        self.age = age
        self.email = email
        self.full_name = full_name
        self.gender = gender
        self.height = height
        self.is_active = True
        self.is_employee = False
        self.password_hash = password_hash
        self.shoe_size = shoe_size
        self.weight = weight

    def create_user(self):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()

        user_data = (self.email, self.full_name, self.age, self.gender, self.height, self.weight, self.shoe_size, self.is_active, self.is_employee, self.password_hash)
        
        cursor.execute('''
        INSERT INTO Users (email, full_name, age, gender, height, weight, shoe_size, is_active, is_employee, password_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', user_data)

        conn.commit()
        conn.close()