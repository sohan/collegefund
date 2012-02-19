from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from fund.models import Student, Achievement
from django.utils import simplejson

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
