#
# The original code for this example is credited to S. Subramanian,
# from this post on DZone: https://dzone.com/articles/restful-web-services-with-python-flask
#

from flask import Flask
from flask import jsonify
from flask import request
from flask import abort

app = Flask(__name__)

empDB=[
 {
 'id':'101',
 'name':'Arício Segundo',
 'title':'Technical Leader',
 'salary': '2000'
 },
 {
 'id':'201',
 'name':'Geraldo Rusmão',
 'title':'Sr Software Engineer',
 'salary': '3000'
 }
 ]


@app.route('/empdb/employee/average_salary', methods=['GET'])
def average_salary():
    salaries = [float(emp['salary']) for emp in empDB]
    
    if not salaries:
        return jsonify({'average_salary': 0})
    
    average = sum(salaries) / len(salaries)
    return jsonify({'average_salary': average})


@app.route('/empdb/employee', methods=['GET'])
def get_all_emp():
    return jsonify({'emps': empDB})

@app.route('/empdb/employee/<empId>', methods=['GET'])
def get_emp(empId):
    usr = [emp for emp in empDB if emp['id'] == empId]
    return jsonify({'emp': usr})

@app.route('/empdb/employee/<empId>', methods=['PUT'])
def update_emp(empId):
    em = [emp for emp in empDB if emp['id'] == empId]

    if len(em) == 0:
        abort(404, description=f"Employee with ID {empId} not found")

    if 'name' in request.json:
        em[0]['name'] = request.json['name']

    if 'title' in request.json:
        em[0]['title'] = request.json['title']

    return jsonify(em)

@app.route('/empdb/employee/<empId>/<empSal>', methods=['PUT'])
def update_emp_sal(empId, empSal):
    em = [emp for emp in empDB if emp['id'] == empId]

    if len(em) == 0:
        abort(404, description=f"Employee with ID {empId} not found")

    em[0]['salary'] = empSal
    return jsonify(em)

@app.route('/empdb/employee', methods=['POST'])
def create_emp():
    dat = {
        'id': request.json['id'],
        'name': request.json['name'],
        'title': request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/update_salary', methods=['POST'])
def update_salary():
    emp_id = request.json.get('id')
    new_salary = request.json.get('salary')

    if not emp_id or not new_salary:
        abort(400, description="Both 'id' and 'salary' must be provided in the request.")

    em = [emp for emp in empDB if emp['id'] == emp_id]

    if len(em) == 0:
        abort(404, description=f"Employee with ID {emp_id} not found")

    em[0]['salary'] = new_salary
    return jsonify(em)

@app.route('/empdb/employee/<empId>', methods=['DELETE'])
def delete_emp(empId):
    em = [emp for emp in empDB if emp['id'] == empId]

    if len(em) > 0:
        empDB.remove(em[0])
        return jsonify({'response': 'Success'})
    else:
        abort(404, description=f"Employee with ID {empId} not found")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)@app.route('/empdb/employee', methods=['GET'])
def get_all_emp():
    return jsonify({'emps': empDB})

@app.route('/empdb/employee/<empId>', methods=['GET'])
def get_emp(empId):
    usr = [emp for emp in empDB if emp['id'] == empId]
    return jsonify({'emp': usr})

@app.route('/empdb/employee/<empId>', methods=['PUT'])
def update_emp(empId):
    em = [emp for emp in empDB if emp['id'] == empId]

    if len(em) == 0:
        abort(404, description=f"Employee with ID {empId} not found")

    if 'name' in request.json:
        em[0]['name'] = request.json['name']

    if 'title' in request.json:
        em[0]['title'] = request.json['title']

    return jsonify(em)

@app.route('/empdb/employee/<empId>/<empSal>', methods=['PUT'])
def update_emp_sal(empId, empSal):
    em = [emp for emp in empDB if emp['id'] == empId]

    if len(em) == 0:
        abort(404, description=f"Employee with ID {empId} not found")

    em[0]['salary'] = empSal
    return jsonify(em)


@app.route('/empdb/employee', methods=['POST'])
def create_emp():
    dat = {
        'id': request.json['id'],
        'name': request.json['name'],
        'title': request.json['title']
    }
    empDB.append(dat)
    return jsonify(dat)

@app.route('/empdb/employee/<empId>', methods=['DELETE'])
def delete_emp(empId):
    em = [emp for emp in empDB if emp['id'] == empId]

    if len(em) > 0:
        empDB.remove(em[0])
        return jsonify({'response': 'Success'})
    else:
        abort(404, description=f"Employee with ID {empId} not found")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
