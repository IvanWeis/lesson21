from django.urls import path
from blogapp import views  # Mark Directory\Sources Root !!! чтобы НЕ подчеркивалось

app_name = 'blogapp'

#views.main_view()
urlpatterns = [
    path('', views.main_view)
]