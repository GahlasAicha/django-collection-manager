Membres du groupe :
SEFFAR Nordine nordine.seffar@etu.univ-orleans.fr
GAHLAS Aicha aicha.gahlas@etu.univ-orleans.fr
MIMOUN Ali ali.mimoun@etu.univ-orleans.fr
AISSAT Fatima fatima.aissat@etu.univ-orleans.fr

Commandes :

ex 1 :

docker build . -f Dockerfile --build-arg USERNAME=$(basename $(id -un) @campus.univ-orleans.fr) --build-arg USERID=$(id -u) --tag cc

docker run -ti -p 8080:8000 -v $PWD:/home/user/workspace cc

django-admin startproject cc

cd cc

python3 manage.py startapp collec_management

python3 manage.py runserver 0.0.0.0:8000 &

ex 2 :

ex 3 :

python3 manage.py makemigrations

python3 manage.py sqlmigrate collec_management 0001

python3 manage.py migrate


python3 manage.py shell

exemple de création :
from collec_management.models import Collec
from django.utils import timezone
Collec.objects.all()
m = Collec(title="collectiontest", description="premiere collection pour verifier", date_creation=timezone.now())
m.id
m.save()
m.id

ex 4 :

python3 manage.py loaddata examples.json

ex 5 :

ex 6 :

ex 7 :

ex 8 :

ex 9 :

ex 10 :

ex 11 :

python manage.py createsuperuser

Admin

Admin@gmail.com

Admin

Admin

Admin


ex 12 :

python manage.py makemigrations

python manage.py sqlmigrate collec_management 0001

python manage.py migrate

ex 13 :

python manage.py dumpdata collec_management.Element --indent 2 >> collec_management/fixtures/examples.json

python manage.py loaddata examples

ex 14 :

ex 15 :

ex 16 :

ex 17 :

ex 18 :

python manage.py makemigrations

python manage.py sqlmigrate collec_management 0001

python manage.py migrate
