from django.shortcuts import render
from blogapp.models import Category, Tovar  # может подкрашиваться

# Create your views here.
def main_view(request):
    return render(request, 'blogapp/index.html', context={}) # запускаем главную страницу

def category(request):
    categories = Category.objects.all() # выбираем все Категории и отправляем на страницу
    tovars = Tovar.objects.all() # выбираем все Тщвары и отправляем на страницу
    return render(request, 'blogapp/category.html', context={'categories' : categories, 'tovars' : tovars})

def contact(request):
    return render(request, 'blogapp/contact.html', context={}) # запускаем страницу LETTER

