from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Member, Book, Meeting, ReadingProgress
from django.http import HttpResponse
from django.urls import reverse_lazy

# Create your views here.
# Member Views
class MemberListView(ListView):
    model = Member
    template_name = 'project/member_list.html'
    context_object_name = 'members'

    def get_queryset(self):
        queryset = super().get_queryset()
        role = self.request.GET.get('role')
        if role:
            queryset = queryset.filter(role=role)
        return queryset
    
class MemberDetailView(DetailView):
    model = Member
    template_name = 'project/member_detail.html'

class MemberCreateView(CreateView):
    model = Member
    fields = ['name', 'email', 'join_date', 'role']
    template_name = 'project/member_form.html'
    success_url = reverse_lazy('member-list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['view'] = {'action':'Add'}
        return context

class MemberUpdateView(UpdateView):
    model = Member
    fields = ['name', 'email', 'join_date', 'role']
    template_name = 'project/member_form.html'
    success_url = reverse_lazy('member-list')

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
        context['view'] = {'action':'Add'}
        return context

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'project/member_confirm_delete.html'
    success_url = reverse_lazy('member-list')

#Book Views
class BookListView(ListView):
    model = Book
    template_name = 'project/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(author__icontains=query)
        return queryset

class BookDetailView(DetailView):
    model = Book
    template_name = 'project/book_detail.html'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'publication_year', 'isbn']
    template_name = 'project/book_form.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'publication_year', 'isbn']
    template_name = 'project/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'project/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

class MeetingListView(ListView):
    model = Meeting
    template_name = 'project/meeting_list.html'
    context_object_name = 'meetings'

class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'project/meeting_detail.html'

class MeetingCreateView(CreateView):
    model = Meeting
    fields = ['date', 'location', 'agenda', 'notes', 'books']
    template_name = 'project/meeting_form.html'
    success_url = reverse_lazy('meeting-list')

class MeetingUpdateView(UpdateView):
    model = Meeting
    fields = ['date', 'location', 'agenda', 'notes', 'books']
    template_name = 'project/meeting_form.html'
    success_url = reverse_lazy('meeting-list')

class MeetingDeleteView(DeleteView):
    model = Meeting
    template_name = 'project/meeting_confirm_delete.html'
    success_url = reverse_lazy('meeting-list')

class ReadingProgressListView(ListView):
    model = ReadingProgress
    template_name = 'project/reading_progress_list.html'
    context_object_name = 'progress'

class ReadingProgressCreateView(CreateView):
    model = ReadingProgress
    fields = ['member', 'book', 'progress_percentage', 'comments']
    template_name = 'project/reading_progress_form.html'
    success_url = reverse_lazy('reading-progress-list')

class ReadingProgressUpdateView(UpdateView):
    model = ReadingProgress
    fields = ['progress_percentage', 'comments']
    template_name = 'project/reading_progress_form.html'
    success_url = reverse_lazy('reading-progress-list')

def homepage(request):
    return render(request, 'project/homepage.html')