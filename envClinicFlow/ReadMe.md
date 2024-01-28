to install the website, follow the following installation instrction:
or (https://xiaoguangwang.notion.site/xiaoguangwang/Equitable-Access-Installation-2b1df738377b46a89bec4ec5abd673d7)

1. Environment: Ubuntu 22.04 (default python 3.10.12)
2. Install python 3.7 (https://www.linuxcapable.com/how-to-install-python-3-7-on-ubuntu-linux/)
3. install virtual python3.7 environment (https://stackoverflow.com/questions/53070868/how-to-install-python3-7-and-create-a-virtualenv-with-pip-on-ubuntu-18-04)
4. install mongdb5.0 (https://computingforgeeks.com/how-to-install-mongodb-database-on-ubuntu/), and start the mangodb service.
5. create envClinicFlow virtual space using python3.7 environment with the name: envClinicFlow
6. install pip under envClinicFlow (source activate)
7. install pip install <packages>:

      appdirs==1.4.0
      Django==1.10.5
      django-debug-toolbar==1.6
      numpy==1.12.0
      packaging==16.8
      pymongo==3.4.0
      pyparsing==2.1.10
      simpy==3.0.10
      six==1.10.0
      sqlparse==0.2.2

8. copy the folder envClinicFlow to /home
9. edit line 16 in ClinicFlow/wsgi.py
    
    sys.path.append('home/yourusername/envClinicFlow/ClinicFlow')
    
10. run python [ClinicMongoDB.py](http://clinicmongodb.py/)
11. create am superuser:`python manage.py createsuperuser --username=joe --email=joe@example.com`
12. run python [manage.py](http://manage.py) 0:8000
13. use browser with URL: 127.0.0.1:8000
