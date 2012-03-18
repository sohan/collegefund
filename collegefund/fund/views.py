from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from fund.models import Student, Achievement
from django.utils import simplejson
from django.contrib.auth.decorators import login_required

MAX_STUDENTS = 9

def get_top_students():
    '''
    get a list of student objects that we should 
    display on the front page
    '''
    students = Student.objects.all()[:MAX_STUDENTS]
    return students

def index(request):
    students = get_top_students()
    data = {'students': students}
    return render_to_response(
        'index.html',
        data,
        context_instance=RequestContext(request))

def about(request):
    data = {}
    return render_to_response(
        'about_us.html',
        data,
        context_instance=RequestContext(request))

def students(request):
    data = {}
    return render_to_response(
        'students.html',
        data,
        context_instance=RequestContext(request))

def donors(request):
    data = {}
    return render_to_response(
        'donors.html',
        data,
        context_instance=RequestContext(request))

def facts(request):
    data = {}
    return render_to_response(
        'facts.html',
        data,
        context_instance=RequestContext(request))

def faq(request):
    data = {}
    return render_to_response(
        'faq.html',
        data,
        context_instance=RequestContext(request))
