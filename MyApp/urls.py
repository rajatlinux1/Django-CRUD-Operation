from django.urls import path
from MyApp import views
urlpatterns = [
    path('create_data/', views.student_data),
    path('getdata/',views.getdata,name="getdata"),
    path('', views.show_data, name='show_data'),
    path('update_data/<int:id>', views.update_data, name='update_data'),
    path('get_update_data', views.get_update_data, name='get_update_data'),
    path('thankyou/', views.ThankYou, name='ThankYou'),
    path('update/', views.updated, name='updated'),
    path('delete_data', views.Delete, name='delete_data'),
    # path('data_deleted/', views.Delete_redirect, name='Delete'),
]