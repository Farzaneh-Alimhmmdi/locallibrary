from django.conf.urls import url
from django.urls import path
from . import views

app_name='catalog'

urlpatterns = [
   path('' , views.Index.as_view(), name='index'),
   path('books/' , views.BookListView.as_view(), name='book-list'),
   path('authors/' , views.AuthorListView.as_view(), name='author-list'),
   url(r'^books/book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
   path('mybooks/' , views.LoanedBooksByUserListView.as_view() , name = 'my-borrowed')
]

