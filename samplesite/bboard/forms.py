from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Bd, CustomUser, comment

class BdForm(forms.ModelForm):  
    class Meta:  
        model = Bd
        fields = ('title', 'content', 'price', 'rubric')

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='login', widget=forms.TextInput)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)
    email = forms.EmailField(label='email', widget=forms.EmailInput)
    first_name = forms.CharField(label='first_name', widget=forms.TextInput)
    last_name = forms.CharField(label='last_name', widget=forms.TextInput)


    class Meta:
        model = CustomUser
        fields = ("username",'email', 'first_name', 'last_name')

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    # class Meta:
       
    #     fields = ('username', 'password')


class CommentPostForm(forms.ModelForm):
    text = forms.Textarea()

    class Meta:
        model = comment
        fields = ('text',)

class UpdateUserInfoForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields = ('first_name', 'last_name', 'birth_date', 'phone_number')


# def post(self, request, *args, **kwargs):
#         form = CommentPostForm(request.POST)
#         if form.is_valid():
#             form1 = form.save(commit=False)
#             form1.user = request.user
#             form1.post = self.get_object()
#             form1.save()
#             return reverse_lazy('detail', kwargs = {
#             'pk': self.object.pk
#         })



# class BdDetailView(BaseDetailView):
#     model = Bd

#     def get(self, request, *args, **kwargs):
#         bd = get_object_or_404(Bd, pk=self.kwargs['pk'])
#         context = dict()
#         context['bd'] = bd
#         context['rubrics'] = Rubric.objects.all()
#         context['form'] = CommentPostForm()
#         comments = comment.objects.filter(post=self.get_object())
#         context['comments'] = comments
#         context['count_comm'] = len(comments)
#         return render(request, context=context, template_name='bboard/bd_detail.html')


    


#     def post(self, request, *args, **kwargs):
#         form = CommentPostForm(request.POST)
#         if form.is_valid():
#             obj = self.get_object()
#             form1 = form.save(commit=False)
#             form1.user = request.user
#             form1.post = obj
#             form1.save()
#         return reverse_lazy('detail', kwargs={
#                 'pk': obj.pk,
#                 })  








# class BdDetailView(View):


#     def get(self, request, *args, **kwargs):
#         bd = get_object_or_404(Bd, pk=self.kwargs['pk'])
#         context = dict()
#         context['bd'] = bd
#         context['rubrics'] = Rubric.objects.all()
#         context['form'] = CommentPostForm()
#         comments = comment.objects.filter(post=Bd.objects.get(pk=self.kwargs['pk']))
#         context['comments'] = comments
#         context['count_comm'] = len(comments)
#         return render(request, context=context, template_name='bboard/bd_detail.html')


#     def post(self, request, *args, **kwargs):
#         form = CommentPostForm(request.POST)
#         if form.is_valid():
#             obj = Bd.objects.get(pk=self.kwargs['pk'])
#             form1 = form.save(commit=False)
#             form1.user = request.user
#             form1.post = obj
#             form1.save()
#         return reverse_lazy('detail', kwargs={
#                 'pk': obj.pk,
#                 })      