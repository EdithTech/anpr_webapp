from fuzzywuzzy import fuzz
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Edith@2023",
    database="anpr"
)

# creating a cursor
cur = db.cursor()

# taking all the vechicle numbers from the database
cur.execute("select vNO from VEHICLEDB")
database_numbers = cur.fetchall()

# database_numbers = ["ABC123", "XYZ789", ...]

# Assuming `extracted_number` is the number plate extracted from the image
# extracted_number = "ABC124"  # Replace with your extracted number

# Set a threshold for similarity

def reqNum(extracted_number):
    
    threshold = 80

    best_match = None
    best_similarity = 0

    for db_number in database_numbers:
        similarity = fuzz.token_set_ratio(extracted_number, db_number)
        
        if similarity > threshold and similarity > best_similarity:
            best_similarity = similarity
            best_match = db_number

        return best_match
    
    # Check if a match is found
    # if best_match is not None:
    #     # Perform database query with the best_match
    #     # ...
    #     print(f"Best match found: {best_match} with similarity {best_similarity}")
    # else:
    #     print("No match found.")
