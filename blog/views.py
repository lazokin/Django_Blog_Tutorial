from django.shortcuts import render

posts = [
    {
        'author': 'Jogn Doe',
        'title': 'Blog Post 1',
        'content': 'Cotent for Blog Post 1',
        'date_posted': 'January 1, 1970'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Cotent for Blog Post 2',
        'date_posted': 'January 1, 1970'
    }
]


def home(request):
    return render(request, 'blog/home.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
