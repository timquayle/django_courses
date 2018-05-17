from __future__ import unicode_literals

from django.shortcuts import render, redirect
import re
from models import *
#main route, it just queries all the users in the db and displays them on our main page
def index(request):
    
    return render(request, "course_app/index.html", { "courses": Course.objects.all() })

def addcourse(request):
 errors = []
 #call our validate function
 errors = validate(request.POST)
 #did we return errors?
 if len(errors):
  context = {
  "errorlist": errors,
  "courses": Course.objects.all()
  }
  return render(request,'course_app/index.html', context)
 #if we don't
 else:
  coursename = request.POST['coursename']
  coursedesc =   request.POST['description']
  Course.objects.create(name=coursename, desc=coursedesc)       
  #entry = Users.objects.get(first_name=firstname, last_name=lastname, email=emailaddress)
  #print "ENTRYID",entry.id
  return render(request, "course_app/index.html", { "courses": Course.objects.all() })
 
def showdelete(request):
   print "RP",request.POST
   cid = request.POST['cid']
   request.session['cid'] = cid
   context = {
   "course": Course.objects.get(id=cid)

    }
   return render(request, "course_app/delverify.html",  context )
def delcourse(request):
    number=request.session['cid']
    Course.objects.get(id=number).delete()
    return render(request, "course_app/index.html", { "courses": Course.objects.all() })
def validate(rp):
 cn = rp['coursename']
 cd = rp['description']
 
 errors = []
 if len(cn) < 5:
  errors.append("Course Name Should be more than 5 characters")
 if len(cd) < 15:
  errors.append("Course Description should be more than 15 characters")
 return errors