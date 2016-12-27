from django.shortcuts import render, get_object_or_404
from . models import Course, Step


def list_course(request):
    courses = Course.objects.all()
    email = "questions@learning_site.com"
    return render(request, 'courses/list_course.html', {
        'courses': courses,
        'email': email,
    })


def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses/course_detail.html', {
        'course': course,
    })


def step_detail(request, course_id, step_id):
    course = get_object_or_404(Course, id=course_id)
    step = get_object_or_404(Step, id=step_id)
    return render(request, 'courses/step_detail.html', {
        'step': step,
    })