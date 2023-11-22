[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/8OHy4RNn)
# RESTful-WS-Example
Simple RESTful Web Service used to illustrate the concept (based on the example by S. Subramanian on DZone.com).
Starter code for the assignment described below.

## What you have to do on this assignment:

After experimenting with this Web service (as described in the lab), extend the service (and its API) to:

a) store and update the salary of the employee;

Foi adicionado o caminho para atualizar os salários: **_@app.route('/empdb/employee/update_salary', methods=['POST'])_** 

Seguindo o modelo dos exemplos para chamar essa função usa o comando:  

**_curl -i -H "Content-type: application/json" -X POST -d "{\"id\":\"<empId>\",\"salary\":\"<empSal>\"}" http://localhost:5000/empdb/employee/update_salary_**  

b) check for errors, such as when trying to update information for a employee that does not exist;

Foi adicionado checagem para os erros 400 e 404 onde o primeira a variável necessária não é informada e o segundo o item que tá sendo procurado para atualizar não existe  

c) retrieve the average salary, considering all the employees;

Foi adicionado o caminho para buscar a media de salario: **_@app.route('/empdb/employee/average_salary', methods=['GET'])_**  
Seguindo o modelo dos exemplos para chamar essa função usa o comando:  

**_curl -i http://localhost:5000/empdb/employee/average_salary_**  

d) update the README with documentation of the service´s API (all its endpoints and how to use them).

## Note: Run the server and client on two separate machines in EC2
