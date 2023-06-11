from django.shortcuts import render

def get_index(request):
    return render(request,'menu_food/index.html',locals())

def about(request):
    return render(request,'menu_food/index.html',locals())

def elements(request):
    return render(request,'menu_food/elements.html',locals())

def contact(request):
    return render(request,'menu_food/contact.html',locals())

def blog(request):
    return render(request,'menu_food/blog.html',locals())

def single_blog(request):
    return render(request,'menu_food/single-blog.html',locals())
