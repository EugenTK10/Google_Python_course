from django.urls import path

from joburi import views

app_name = 'joburi'

urlpatterns = [
    path('', views.JoburiView.as_view(), name='lista_joburi'),
    path('adaugare/', views.CreateJoburiView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateJoburiView.as_view(), name='modificare'),
    path('<int:pk>/delete/', views.delete_joburi, name='stergere'),
    path('<int:pk>/activate/', views.activate_joburi, name='activare'),
]
