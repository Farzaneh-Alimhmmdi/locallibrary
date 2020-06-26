from django.shortcuts import render
from django.views import generic
from . import models

app_name = 'catalog'

class Index(generic.TemplateView):

    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_books"]                = models.Book.objects.all().count()
        context["num_instances"]            = models.BookInstance.objects.all().count()
        context["num_instances_available"]  = models.BookInstance.objects.all().filter(status__exact = 'a').count()
        context["num_authors "]             = models.Author.objects.count()
        return context
    
class BookListView(generic.ListView):
    template_name = 'catalog/booklist.html'
    model = models.Book

class BookDetailView(generic.DetailView):
    template_name =  'catalog/bookdetail.html' 
    model = models.Book

class AuthorListView(generic.ListView):
    template_name = 'catalog/authorlist.html'
    model = models.Author

class AuthorDetailView(generic.DetailView):
    template_name =  'catalog/authordetail.html' 
    model = models.Author    