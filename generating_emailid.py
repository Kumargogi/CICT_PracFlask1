from flask import Flask, request, jsonify
app = Flask(__name__)
import numpy as np
import json




@app.route('/',methods = ['GET'])
def get_users():
    with open("data.json" , "r") as file:
        users_data = json.load(file)

        no_of_users = len(users_data)

        html = """
        <html>

            <body>

                <table border="1">
                    <tr>
                        <th>UID</th>
                        <th>NAME</th>
                        <th>MAIL_ID</th>

                    </tr>
        """
        for user in users_data:
                html += """
                    <tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                    </tr>
            """.format(user["u_id"],user["name"],user["email_id"])
        html += """
                
            </body>


        </html> """.format(users_data[0])
        return html
        # return jsonify({
        #     "users" : users_data,
        #     "no_of_users" : no_of_users
        # })
    
@app.route('/',methods=['POST'])
def add_uers():
    with open("data.json", "r") as file:
        users_data = json.load(file)
        
        u_id = request.json["u_id"]
        name = request.json["name"]

        new_user = {
            "u_id" : u_id,
            "name" : name,
            "email_id" : name+"@kpit.com"
        }
        users_data.append(new_user)

    with open("data.json", "w") as file:
        json.dump(users_data, file, indent = 4 ) 

    return jsonify({
        'msg' : 'added successfully'
    })

@app.route('/',methods=["PUT"])
def update_users():
    with open("data.json","r") as file:
        users_data = json.load(file)

        u_id = request.json["u_id"]
        updated_name = request.json["name"]

        for user in users_data:
            if user["u_id"] == u_id:
                user["u_id"]==u_id
                user["name"]==updated_name
                user["email_id"] == updated_name+"@kpit.com"
    with open("data.json","w") as file:
        json.dump(users_data,file, indent = 4)

    return jsonify({
        'msg' : 'Updated successfully'
    })

@app.route('/',methods=["DELETE"])
def delete_user():
    with open("data.json","r") as file:
        users_data = json.load(file)

        u_id = request.json["u_id"]

        for user in users_data:
            if user["u_id"] == u_id:
                users_data.remove(user)
                break
    with open("data.json","w") as file:
        json.dump(users_data,file,indent = 4)

    return jsonify({
        'msg' : 'Deleted successfully'
    })



app.run(port=5000)
