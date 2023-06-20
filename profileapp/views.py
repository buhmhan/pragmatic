from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.utils.decorators import method_decorator

# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'get')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'
    
    def get_success_url(self):
        return reverse_lazy('accountapp:detail', kwargs={'pk': self.object.user.pk})
