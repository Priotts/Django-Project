
# Django project

Simple development of a certificate creation system with a blockchain-based verification.

## Project Description

The project consists of a simple web application that allows administrators to create and assign digital training certificates to students. Every time a certificate is assigned, a transaction is sent on Ethereum with all the certificate and student information. Students can then enter the certificate code to view the associated information and corresponding transaction. 

Additionally, the system stores the last IP address that accessed the platform for each administrator user and displays a warning if access is detected from a different IP address than the previous one.

## Project features
- A page accessible only to administrators, where it is possible to assign a digital certificate to a student.

![image](https://user-images.githubusercontent.com/94853311/235688704-55efa80e-190c-4ab9-8fa3-0f0373005840.png)

- A page that anyone can access and enter the identification code of a degree certificate to view all associated information and the transaction.

ATTENTION! Before searching for a certificate, you must assign it to a student.

![image](https://user-images.githubusercontent.com/94853311/235691018-ce5e9570-2bb8-4a2d-ba52-4ed5e37613b8.png)

- A logging system to store the last IP address of an administrator who accessed the platform, in order to display a warning message when it is different from the previous one.

![image](https://user-images.githubusercontent.com/94853311/235691919-d83439fe-bcad-49c5-b1ed-235231be4e99.png)



## Installation

- Clone the repo 

```bash
git clone https://github.com/Priotts/Django-Project.git
```
- Make database migrations
```bash
py .\manage.py makemigrations
py .\manage.py migrate
```
- Create administrator user
```bash
py .\manage.py createsuperuser
```
- Install the redis server (it will be used for ip control)
```bash
sudo service redis-server start
``` 

- start your server

```bash 
python manage.py runserver
``` 

- type your address into your browser


