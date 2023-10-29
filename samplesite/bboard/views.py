from typing import Any, Dict, Optional
from django.core.paginator import Paginator
from django.db import models
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Bd, Rubric, CustomUser, comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView, BaseCreateView, ModelFormMixin, FormMixin
from .forms import BdForm, RegisterUserForm, LoginForm, CommentPostForm, UpdateUserInfoForm
from django.urls import reverse_lazy, reverse
from django.views.generic.base import TemplateView,RedirectView, ContextMixin
from django.views.generic.detail import DetailView, BaseDetailView, SingleObjectMixin
from django.views.generic.list import ListView
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.core.paginator import Paginator, Page
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


class RegView(CreateView):
    # model = Profile
    form_class = RegisterUserForm
    template_name = 'bboard/reg.html'
    success_url = reverse_lazy('login')
    
    # def get(self ,request, *args, **kwrgs):
    #     request.session['d'] = '123'    
    #     print(request.session['d'])    \
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('index')
    form_class = LoginForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
    

class MyProfileView(TemplateView):
    template_name = 'accounts/prof.html'

    # def get_queryset(self):
    #     return Bd.objects.filter(user=self.kwargs['user_id'])
    def post(self, request):
        name = request.POST.get('FLfirst')
        phone =request.POST.get('phone_number')
        birth = request.POST.get('birth_date')
        user = self.request.user
        z = CustomUser.objects.get(user=user)

        z.phone_number = phone
        z.birth_date = birth
        z.first_name = name[0]
        z.last_name = name[1]
        
        z.save()
        return JsonResponse({'message': 'все ок'})
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        context['bbs'] = Bd.objects.filter(user=self.request.user)
        
        return context
    

class ProfileView(TemplateView):
    template_name = 'accounts/other_profile.html'
    # form_class = UpdateUserInfoForm
    model = CustomUser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        user = self.kwargs['user_id']
        context['bbs'] = Bd.objects.filter(user = user)
        context['user_info'] = CustomUser.objects.filter(pk=user)

        
        return context
    
 
class fetch(TemplateView):
    template_name = 'bboard/fetch.html'

    def post(self, request):
        
        con = self.request.POST.get()
        print(con)
    
        


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class BdIndex(TemplateView):
    template_name = 'bboard/index.html'
    # template_name = 'bboard/test.html'
    # context_object_name = 'bbs'
    # date_list_period = 'day'
    # date_field = 'published'
    # allow_empty = True
    # model = Bd

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        # if Bd.objects.all().count() == 0:
        bbs = Bd.objects.all()
        paginator = Paginator(bbs, 5)
        #     context['none'] = "Объявлений пока нет"
        # context['bbs'] = Bd.objects.all()
        context['rubrics'] = Rubric.objects.all() 

        return context
    
def BdIndex(request):
    rubric = Rubric.objects.all()
    bbs = Bd.objects.all()
    paginator = Paginator(bbs, 5)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'bbs':page.object_list, 'page':page, 'rubrics':rubric}
    return render(request=request, context=context, template_name='bboard/index.html')


class BdByRubricView(ListView):
    context_object_name = 'bbs'
    template_name = 'bboard/by_rubric.html'


    def get_queryset(self):

        return Bd.objects.filter(rubric=self.kwargs['rubric_id'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if by_rub.all().count() == 0:
            # context['none'] = "Объявлений пока нет"
        # if Bd.objects.filter(rubric=self.kwargs['rubric_id']).all().count() == 0:
        #     context['none'] = 'Объявлений пока нет'
        # context['t'] = by_rub
        context['rubrics'] = Rubric.objects.all()
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context
        
class BdMonthArchiveView(MonthArchiveView):
    model = Bd
    date_field = 'published'
    month_format = '%m'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BdDetailView(CreateView):
    model = Bd
    form_class = CommentPostForm
    template_name = 'bboard/bd_detail.html'
     

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['bd'] =  get_object_or_404(Bd, pk=self.kwargs['pk'])
        context['rubrics'] = Rubric.objects.all()
        context['form'] = CommentPostForm()
        comments = comment.objects.filter(post=Bd.objects.get(pk=self.kwargs['pk']))
        context['comments'] = comments
        context['count_comm'] = len(comments)
        return context
    
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        obj = Bd.objects.get(pk=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.post = obj
        return super().form_valid(form)
         
    def get_success_url(self) -> str:
        return reverse_lazy('detail', kwargs={
                'pk':self.kwargs['pk'],
                })   

def ajax_delete(request):
    if request.is_ajax():
        ...

class BdCreateView(CreateView):
    template_name = 'bboard/create.html'
    model = Bd
    form_class = BdForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BdUpdateView(UpdateView):
    form_class = BdForm
    model = Bd
    template_name = 'bboard/update.html'

    def get_context_data(self, *args, **kwrgs):
        context = super().get_context_data(*args, **kwrgs)
        context['rubrics'] = Rubric.objects.all()
        return context
    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={
            'pk': self.object.pk,
        })
    

class BdDeleteView(DeleteView):
    model = Bd
    context_object_name = 'ob'
    success_url = reverse_lazy('index')

    def get_queryset(self):   
        return Bd.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwrgs):
        context = super().get_context_data(**kwrgs)
        context['rubrics'] = Rubric.objects.all()
        return context
    

class DeleteComment(DeleteView):
    model = comment

    
    def get_success_url(self):
        return reverse_lazy('detail', kwargs = {
        'pk': self.kwargs['pk']
    })


class MainRedirectView(RedirectView):
    url = reverse_lazy('index')