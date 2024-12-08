from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Member, Book
from django.http import HttpResponse

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name = 'project/member_list.html'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'project/member_detail.html'

class BookListView(ListView):
    model = Book
    template_name = 'project/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'project/book_detail.html'

def homepage(request):
    return HttpResponse("<h1>Welcome to the Book Club Manager!</h1><a href='/project/members/'>View Members</a><br><a href='/project/books/'>View Books</a>")