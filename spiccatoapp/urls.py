from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.courses, name='courses'),
    path('base/', views.base, name='base'),
    path('apply/', views.apply, name='apply'),
    path('Gallery/', views.Gallery, name='Gallery'),
    path('video_gallery/', views.video_gallery, name='video_gallery'),
    path('home_final/', views.home_final, name='home_final'),

    # Enrollment
    path('enroll/', views.enroll_view, name='enroll'),  # The form page
    path('enroll_success/', views.enroll_success, name='enroll_success')  # The thank-you page
]
