# candidates

1. Create Venv 
python3 -m venv testenv

2.Run command source testenv/bin/activate

3.Download python 3.0 or above

4. pip install django-rest-framework

5. go the project directory run ./manage.py makemigrations candidates

6. Run ./manage.py migrate

7.Run ./manage.py createsuperuser to be the admin user 

8. Run ./manage.py runserver 

****backend will be run in localhost:8000

***Run front end ***

9. open another terminal run the venv in step 1 

10. go to front end directory in project folder and run npm install

11.run sudo npm run start

12. Front end will be run localhost : 3000

****Admin****
1. admin/  users and candidate models register and can be updates 

*******API End Points ********
1.api/candidates/$ [name='candidate_list']
2.api/candidates/(?P<id>\d+)/details/$ [name='candidate_details']
3.api/candidates/(?P<id>\d+)/download_cv/$ [name='download_cv']
4.api/candidates/register/$
5.api/get-token [name='get-token']


