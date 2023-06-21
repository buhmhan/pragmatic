from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 5

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    
    def get_success_url(self):
        return reverse_lazy('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

