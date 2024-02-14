from flask import Flask, render_template, request
import os 
from deeplearning import object_detection
from flask_mysqldb import MySQL
import mysql.connector
from fuzzywuzzy import fuzz
import fuzzyLogic


# webserver gateway interface
app = Flask(__name__)

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH,'static/upload/')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Edith@2023",
    database="anpr"
)

mysql = MySQL(app)

cur = db.cursor()
cur.execute("select vNO from VEHICLEDB")
dbCol = cur.fetchall()

@app.route('/',methods=['POST','GET'])
def index():

    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH,filename)
        upload_file.save(path_save)
        text_list = object_detection(path_save,filename)

        print(text_list)

        cur.execute("select * from VEHICLEDB where vNO = (%s)", (text_list))
        feachdata = cur.fetchall() 

        print(feachdata)


        # #fuzzy logic testing

        # threshold = 50

        # best_match = None
        # best_similarity = 0

        # for db_number in dbCol:
        #     similarity = fuzz.token_set_ratio(text_list, db_number)
        #     print(f"Similarity {similarity}")
            
        #     if similarity > threshold and similarity > best_similarity:
        #         best_similarity = similarity
        #         best_match = db_number

        # # Check if a match is found
        # if best_match is not None:
        #     print(f"Best match found: {best_match} with similarity {best_similarity}")
        #     ind = dbCol.index(best_match)
        #     # print("Max Similarity : ", max(simVal))
        #     cur.execute("select * from VEHICLEDB where vNO = (%s)", (dbCol[ind]))
        #     feachdata = cur.fetchall() 

        #     return render_template('index.html',upload=True,upload_image=filename,text=text_list,no=len(text_list), rol=feachdata)
        # else:
        #     feachdata = "No match found"
        #     print("No match found.")

        return render_template('index.html',upload=True,upload_image=filename,text=text_list,no=len(text_list), rol=feachdata)

    return render_template('index.html',upload=False)


if __name__ =="__main__":
    app.run(debug=True)


#87

#  database
# num = ''.join(text_list)
# cur = db.cursor()
# cur.execute("INSERT INTO users(rol, vnum) values(%s, %s)", ("student", num))
# ---------------------------------------------------
# threshold = 55
# feachdata = ""
    

#94
    #---------------------------------------------------------------
        # simVal = []
        # mxThreshold = -1

        # for db_number in dbCol:
        #     similarity = fuzz.ratio(text_list, db_number)
        #     simVal.append(similarity)
        #     # if similarity > threshold:
        #     #     mxThreshold = max(mxThreshold, similarity)
        #     #     break    
        
        # ind = simVal.index(max(simVal))
        # print("Max Similarity : ", max(simVal))
        # cur.execute("select * from VEHICLEDB where vNO = (%s)", (dbCol[ind]))
        # feachdata = cur.fetchall() 

#110
# ----------------------------------------------------------------------------
    # num = ''.join(text_list)
    # best_match = fuzzyLogic.reqNum(text_list)

    # if best_match is not None:
    #     cur.execute("SELECT * FROM VEHICLEDB WHERE vNO = (%s)", (best_match))
        # feachdata = cur.fetchall() 
    #     print(f"Best match found: {best_match} with similarity {best_similarity}")
    # else:
    #     print("No match found.")
    

    

    # db.close() // if we uncomment this then we have to restart the server again and again
    # db.commit()

