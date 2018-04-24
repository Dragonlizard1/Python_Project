project create--
must be in python environment

django-admin startproject projectname
go inside project name create apps directory
mkdir apps
go inside apps folder and add a init file
nul> __init__.py

in apps a subfolder of app name need to add a url and view file.

--------

start in django folder. then call it
call djangoEnv/Scripts/activate

to run the program
python manage.py runserver


foldername is to create folder
python ../manage.py startapp foldername

del request.session["key"]    individual key
request.session.clear()     will delete all key

inside of form need this in django security form protection
{% csrf_token %}



static stylesheet create in html
{% load static %}  - need this to load static file
<link rel="stylesheet" href="{% static 'Ttime_display/main.css' %}" media="screen" title="no title"  charset="utf-8">

table collapse border
border-collapse: collapse;

in view file  to render with a request for html

return render(request, "first_app/index.html")

from django.contrib.messages import get_messages
is the message in dictionary.

.iteritems()   to iterate a dictionary key in the for loop

'^' Matches the following characters at the beginning of a string. Example: '^a' matches 'anna' but not 'banana'.
'$' Matches the previous characters at the end of a string. Example: 'a$' matches 'anna' and 'banana' but not 'fan'.
'[]' Matches any value in a range. Example: '[0-9]' matches '9' and '9s'.
'{n}' Matches n number or more repetitions of the preceding pattern. Example: '[0-9]{2}' matches '91' and '9834' but not '9'
"\d Matches digits.  Example:" "\d" matches "8" and "877x"
"\d+ matches a string with one or more digits"
"\w Matches characters."
"\w+ matches a string with one or more character/word"


url(r'^(?P<number>\d+)$', views.show)
to search the number pass nnumber variable to function


<p id = "bluebig">{{request.session.list}}</p>
			<p id = "red">{{request.session.list}}</p>
			<p id = "redbig">{{request.session.list}}</p>
			<p id = "green">{{request.session.list}}</p>
			<p id = "greenbig">{{request.session.list}}</p>


---------------------

sql model in django

python manage.py shell 
to run the program

python manage.py makemigrations
python manage.py migrate

must do both everytime you modify the model or finish.

inshell must import everytime:
from apps.{{app_name}}.models import *


---------
use the .value() to get a certian column in table
.value_list("column") give a tuple list without a key.
.value_list("column", flat=True) give a array list.

instance = MyModel.objects.values('description')[0]
description = instance['description']
If you use values_list(), you'll end up with a list of tuples

instance = MyModel.objects.values_list('description')[0]
description = instance[0]
Or if you're just getting one value like in this case, you can use the flat=True kwarg with values_list to get a simple list of values

description = MyModel.objects.values_list('description', flat=True)[0]

examplel------ for rename keys in search.
address = UniversityAddress.objects.filter(university=university)
address = address.extra(select={'city__state__country__name': 'country', 'city__state__name': 'state', 'city__name': 'city'})
address = address.values('country', 'state', "city", 'street', "postal_code").get()


.distinct("column",)

datetimes(field_name, kind, order='ASC', tzinfo=None)
kind be replace with:
"year", "month", "day", "hour", "minute" or "second"

	print datetime.now() , "  now"
	print datetime.today() , "today"
----------

similiar to init:
def __str__(self):
	return self.name

time
created_at = models.DateTimeField(auto_now_add = True)
updated_at = models.DateTimeField(auto_now = True)

auto_now_add gives current DateTime
auto_now  update datetime everytime modify


CharField
Any text that a user may enter. This has one additional required parameter, max_length, that (unsurprisingly) is the maximum length of text that can be saved.
TextField
Like a CharField, but with no maximum length. Your user could copy the entire text of Atlas Shrugged into the field, and it would save in the database correctly.
IntegerField, BooleanField
Holds integers or booleans, respectively
DateTimeField
Used for date and times, such as timestamps or when a flight is scheduled to depart. This field can take two very useful optional parameters, auto_now_add=True, which adds the current date/time when object is created, and auto_now=True, which automatically updates any time the object is modified.
ForeignKey, ManyToManyField, OneToOneField
Used to indicate a relationship between models (anything that would require a JOIN statement in SQL). ForeignKey is for one-to-many relationships and goes in the model on the "many" side, just as the foreign key column goes in the SQL table on the "many" side.


 author = models.ForeignKey(Author, related_name="books")  related name is a hidden key inside of other"Author" table.
left side is many  = is one side


all validation form in model.py file.

 to create
 this_author = Author.objects.get(id=2)
my_book = Book.objects.create(title="Little Women", author=this_author)  
# or on one line...
my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

it will auto JOIN
will name it in this ex.  my_book.author.name

to search
this_author = Author.objects.get(id=2)
books = Book.objects.filter(author=this_author)
# one-line version:
books = Book.objects.filter(author=Author.objects.get(id=2))

use __   double underline between 2 column to search for both


------------------step1 upload to github
git init
git add --all
git commit -m "initial commit"
git remote add origin https://github.com/Dragonlizard1/django_courses.git
git push origin master

----------------- step 2 ativate gitbash in server
project run in aws
in gitbash

folder in aws

chmod 400 django_pem.pem
ssh -i "django_pem.pem" ubuntu@ec2-18-219-246-211.us-east-2.compute.amazonaws.com

ubuntu@ip-my-ip:~$: git clone https://github.com/Dragonlizard1/django_courses.git

in server go to folder of project ex django_courses:
source venv/bin/activate

python manage.py collectstatic

on server root:
sudo nginx -t

sudo service nginx restart

my ip address for aws
18.219.246.211

-----------------------------
Use time

Let's say you have the initial dates as strings like these:
date1 = "31/12/2015"
date2 = "01/01/2016"

You can do the following:
newdate1 = time.strptime(date1, "%d/%m/%Y") and newdate2 = time.strptime(date2, "%d/%m/%Y") to convert them to python's date format. Then, the comparison is obvious:

newdate1 > newdate2 will return False
newdate1 < newdate2 will return True

from datetime import datetime, date, time
strptime will seperate into timetuple
strftime to format into time format.

datetime.strftime(fmt, d.timetuple()
datetime.strptime(date_string, format)

datetime.now(tz=None)      tz = "CST"  --- central time
datetime.date
datetime.time
datetime.NOW()

Central  = USTimeZone(-6, "Central",  "CST", "CDT")

class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)

-------------------
<div style="position:relative;width:200px;height:25px;border:0;padding:0;margin:0;">
  <select style="position:absolute;top:0px;left:0px;width:200px; height:25px;line-height:20px;margin:0;padding:0;"
          onchange="document.getElementById('displayValue').value=this.options[this.selectedIndex].text; document.getElementById('idValue').value=this.options[this.selectedIndex].value;">
    <option></option>
    <option value="one">one</option>
    <option value="two">two</option>
    <option value="three">three</option>
  </select>
  <input type="text" name="displayValue" id="displayValue" 
         placeholder="add/select a value" onfocus="this.select()"
         style="position:absolute;top:0px;left:0px;width:183px;width:180px\9;#width:180px;height:23px; height:21px\9;#height:18px;border:1px solid #556;"  >
  <input name="idValue" id="idValue" type="hidden">
</div>