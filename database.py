from config import DB_CONFIG
import mysql.connector


class Database:
    def __init__(self):
        """
        Initializes a new db.
        """
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cursor = self.conn.cursor()
        self.cursor.execute("ALTER DATABASE phonebook CHARACTER SET = utf8mb4 "
                        "COLLATE = utf8mb4_unicode_ci")
        self.create_tables()


    def create_tables(self):
        """
        Creates the necessary tables in the database if they do not already exist.
        This function creates the 'phonebook' table if it does not already exist. The table has the following columns:
        - id: an auto-incrementing integer that serves as the primary key.
        - first_name: a string that represents the first name of the person, with a maximum length of 255 characters.
        - last_name: a string that represents the last name of the person, with a maximum length of 255 characters.
        - phone: a string that represents the phone number of the person, with a maximum length of 255 characters.
        This function does not take any parameters and does not return any values.
        Example usage:
        create_tables()
        """
        # create_phonebook_table = "CREATE TABLE IF NOT EXISTS phonebook (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(255) DEFAULT NULL, last_name VARCHAR(255) DEFAULT NULL, phone VARCHAR(255) UNIQUE)"
        create_phonebook_table = ("CREATE TABLE IF NOT EXISTS phonebook (id "
                                  "INT AUTO_INCREMENT PRIMARY KEY, "
                                  "first_name VARCHAR(255) CHARACTER SET "
                                  "utf8mb4 COLLATE utf8mb4_unicode_ci "
                                  "DEFAULT NULL, last_name VARCHAR(255) "
                                  "CHARACTER SET utf8mb4 COLLATE "
                                  "utf8mb4_unicode_ci DEFAULT NULL, "
                                  "phone VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci UNIQUE)")
        self.cursor.execute(create_phonebook_table)
        self.cursor.execute("ALTER TABLE phonebook CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        # self.cursor.execute("ALTER TABLE phonebook CHANGE first_name last_name phone_number VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
        self.conn.commit()


    def add_phone_numbers(self, phone_numbers):
        """
        Add phone numbers to the phonebook database.

        :param phone_numbers: list of dictionaries containing 'first_name', 'last_name', and 'phone' keys.
        :return: None
        """
        for phone_number in phone_numbers:
            query = "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (
                phone_number.get('first_name'), phone_number.get('last_name'),
                phone_number.get('phone')))
        self.conn.commit()

    def get_phone_numbers(self):
        """
        Retrieve all phone numbers from the phonebook.
        No parameters.
        Returns a list of tuples, where each tuple represents a row from the 'phonebook' table.
        """
        query = "SELECT * FROM phonebook"
        self.cursor.execute(query, )
        return self.cursor.fetchall()

    def search_phone_number(self, phone):
        """
        Searches for a phone number in the phonebook table.

        Parameters:
            phone (str): The phone number to search for.

        Returns:
            list: A list of tuples containing the results of the search.
        """
        query = "SELECT * FROM phonebook WHERE phone LIKE %s"
        self.cursor.execute(query, ('%' + phone[1:] + '%',))
        return self.cursor.fetchall()
