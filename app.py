from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)

@app.route('/')
def Index():
    # getdata
    
    cur = mysql.connection.cursor()
    cur.execute("""SELECT t.task, t.status
                FROM todos t
                INNER JOIN status s
                ON t.status = s.name
                ORDER BY s.rank""") 
    # update based on rank
    data = cur.fetchall()
    cur.close()
    return list(data), 200
    # return render_template('index.html', todos=data)

@app.route('/create', methods=['POST'])
def create():
    if request.method == "POST":
        # 
        
        
        flash("Todo Inserted Successfully")
        task = request.form['task']
        status = "Pending"
        # 
        
        cur = mysql.connection.cursor()
        cur.execute("""SELECT task, status FROM todos WHERE task = %s""",(task,))
        existing_data = (cur.fetchall())
        print(existing_data)
        if existing_data == ():
            cur.execute("INSERT INTO todos (task, status) VALUES (%s, %s)", (task, status))
        mysql.connection.commit()
        if existing_data != ():
            return "Task with same name exists", 403
            # status code 
            
        return "Created Succesfully", 200
        

@app.route('/delete', methods=['DELETE'])
def delete():
    if request.method == 'DELETE':
        task = request.form['task']
        # flash("Todo Has Been Deleted Successfully")
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM todos WHERE task=%s", (task,))
        data = (cur.fetchall())
        # check if tasks are valid or not
        if data == ():
            cur.close()
            return "Task does not exists", 404
        # status code
        cur.execute("DELETE FROM todos WHERE task=%s", (task,))
        mysql.connection.commit()
        return "Deleted succesfully", 200

@app.route('/update', methods=['PUT'])
def update():
    if request.method == 'PUT':
        task = request.form['task']
        new_task_name = request.form['new_name']
        status = request.form['status']
        
        print(task)
        print(new_task_name)
        print(status)
        
        if task == "":
            return "No task provided", 403
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM todos WHERE task=%s", (task,))
        data = (cur.fetchall())
        print(data)
        # flash("Todo Updated Successfully")
        # mysql.connection.commit()
        print(type(data))
        if data == ():
            return "Task not found", 404
        
        data = list(data)
        print(data)
        
        if new_task_name == "":
            new_task_name = data[0][1]
        else:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM todos WHERE task=%s", (new_task_name,))
            data = (cur.fetchall())
            mysql.connection.commit()
            if data != ():
                return "New task name already exists.", 403
            # 
            
        if status == "":
            status = data[0][2]
        #checking if status is correct or not
        status = status.lower()
        if status == "complete": # 'complete' and 'completed' both accepted
            status = "completed"
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM status WHERE value=%s",(status,))
        existing_status = cur.fetchall()
        if existing_status == (): # incorrect status, not found in db
            return "Incorrect status", 403
        
        cur.execute("""
        UPDATE todos SET task=%s, status=%s
        WHERE task=%s
        """, (new_task_name, status, task))
        mysql.connection.commit()
        return "Updated successfully", 200
        return redirect(url_for('Index'))

if __name__ == "__main__":
    app.run(debug=True)
