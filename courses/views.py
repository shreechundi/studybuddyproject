from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from study_buddy_app import *
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from .models import *
import requests
import json
from .forms import ProfileChangeForm

#Saved Departments into Database and Loaded all courses into course list
# students_classes = []
# response = requests.get('http://luthers-list.herokuapp.com/api/deptlist?format=json').json()
# for item in response:
#     # dept = Department(name = item['subject'])
#     # dept.save()

courses = []
dept = ""

def Profileview(request, pk=None):
    #add the classes to the student model & save to db
    students_classes = []
    students_classes_string = []
    if pk:
        student = Student.objects.get(name=pk)
    else:
        student, created = Student.objects.get_or_create(name=request.user.username)
        student.save()
    if student.class_list != "":
        students_classes_string = json.loads(student.class_list)
    for course in students_classes_string:
        students_classes.append(Course.objects.get(name=course))
    graduation = student.grad_year
    major = student.major
    minor = student.minor
    interests = student.interests
    name = student.name
    context = {'name':name, 'studentclasses': students_classes, 'grad':graduation, 'major':major, 'minor':minor, 'hobbies':interests}
    return render(request,'courses/profile.html', context)

def Courseview(request, pk=None):
    if pk:
        classobj = Course.objects.get(pk=pk)
        student_list = json.loads(classobj.studentslist)
        classname = classobj.name
        context={'studentlist': student_list, 'classname': classname}
    else:
        student_list = []
        context = {'studentlist': student_list}
    return render(request,'courses/class.html', context)


def Departmentview(request):
    global dept
    # departments = Department.objects.all()
    departments = []
    response = requests.get('http://luthers-list.herokuapp.com/api/deptlist?format=json').json()
    for item in response:
        departments.append(item['subject'])
    if request.method == 'POST':
        dept = request.POST
        return HttpResponseRedirect(reverse('classlist'))
    return render(request,'courses/courses.html', {'departments':departments}) #, 'courses': courselist})

def classview(request):
    global dept
    if request.method == 'POST':
        classobj, created = Course.objects.get_or_create(name=request.POST['course'])
        classobj.save()
        clss_lst = [request.POST['course']]
        student = Student.objects.get(name=request.user.username)
        student_list = [student.name]
        if student.class_list != "" and request.POST['course'] not in student.class_list:
            clss_lst = json.loads(student.class_list) #converts string into list
            clss_lst.append(request.POST['course'])
            if classobj.studentslist != "":
                student_list = json.loads(classobj.studentslist)
                student_list.append(student.name)
        classobj.studentslist = json.dumps(student_list)
        classobj.save()
        student.class_list = json.dumps(clss_lst) #converts a list into a string
        student.save()
        return HttpResponseRedirect(reverse('profile'))
    courses = []
    deptt = ""
    if dept != "":
        deptt = dept['dept']
    if deptt != "":
        response2 = requests.get('http://luthers-list.herokuapp.com/api/dept/' + deptt + '?format=json').json()
        for item2 in response2:
            course = deptt + " " + item2['catalog_number'] + " " + item2['description']
            if course not in courses:
                courses.append(course)
        return render(request, 'courses/test.html', {'courses': courses})

def ProfileEdit(request):
    if request.method == 'POST':
        student = Student.objects.get(name=request.user.username)
        form = ProfileChangeForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = ProfileChangeForm()
    context = {'form': form,}
    return render(request, 'courses/profileedit.html', context)

#sources:
#https://www.youtube.com/watch?v=zcJegVlKqqs for pk stuff
#author: Max Goodridge


