from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                    ListView, DetailView,
                                    CreateView, UpdateView,
                                    DeleteView)
from . import models
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context

class SchoolListView(ListView):
    #if we want to change name of list:
    context_object_name = 'schools'
    model = models.School
    #it returns school_list :)

class StudentListView(ListView):
    model = models.Student
    #student_list

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class StudentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.Student
    template_name = 'basic_app/student_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal','location')
    model = models.School

class StudentCreateView(CreateView):
    fields = ('name', 'age','school')
    model = models.Student

class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class StudentUpdateView(UpdateView):
    fields = ('name', 'age', 'school')
    model = models.Student

class SchoolDeleteView(DeleteView):
    model =models.School
    success_url = reverse_lazy("basic_app:list")

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:slist")
