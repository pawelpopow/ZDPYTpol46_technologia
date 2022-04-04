from django.urls import path

from viewapp import views
from django.views.generic import TemplateView

app_name = 'viewapp'

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello2/', views.HelloView.as_view(), name='hello2'),

    path('template/hello/', views.hello_template, name='hello-template'),
    path('template/hello2/', views.HelloClassView.as_view(), name='hello-template2'),
    path('template/hello3/', views.HelloTemplateView.as_view(), name='hello-template3'),
    path(
        'template/hello4/',
        TemplateView.as_view(template_name="viewapp/hello.html"),
        name='hello-template4'
    ),

    path('template2/hello/', views.hello_template2, name='hello2-template'),
    path('template2/hello2/', views.HelloClassView2.as_view(), name='hello2-template2'),
    path('template2/hello3/', views.HelloTemplateView2.as_view(), name='hello2-template3'),

    path('person/<int:id>/', views.person_detail, name='person-detail'),
    path('person2/<int:id>/', views.PersonView.as_view(), name='person-detail2'),
    path('person3/<int:pk>/', views.PersonDetailView.as_view(), name='person-detail3'),

    path('create-person/', views.create_person, name='create_person'),
    path('create-person2/', views.PersonCreateView.as_view(), name='create_person2'),
    path('create-person3/', views.PersonCreateView2.as_view(), name='create_person3'),
]