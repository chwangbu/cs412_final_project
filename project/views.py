from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Member, Book, Meeting, ReadingProgress
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.timezone import now
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your views here.
# Member Views

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
    
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
    fields = ['name', 'email', 'join_date', 'role', 'password']

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['email'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        form.instance.user = user
        return super().form_valid(form)

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
        query = self.request.GET.get('q', '')
        author = self.request.GET.get('author', '')

        if query:
            queryset = queryset.filter(title__icontains=query)

        if author:
            queryset = queryset.filter(author__icontains=author)

        return queryset

class BookDetailView(DetailView):
    model = Book
    template_name = 'project/book_detail.html'

class BookCreateView(AdminRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'genre', 'publication_year', 'isbn']
    template_name = 'project/book_form.html'
    success_url = reverse_lazy('book-list')

    def test_func(self):
        return self.request.user.is_staff
    
    def handle_no_permission(self):
        from django.contrib import messages
        messages.error(self.request, "Only admins can add books.")
        return redirect('homepage')
    
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'genre', 'publication_year', 'isbn']
    template_name = 'project/book_form.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(AdminRequiredMixin, DeleteView):
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
    fields = ['date', 'location', 'agenda']
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

class ReadingProgressUpdateView(UpdateView):
    model = ReadingProgress
    fields = ['progress_percentage', 'comments']
    template_name = 'project/reading_progress_form.html'
    success_url = reverse_lazy('reading-progress-list')

    def get_queryset(self):
        return ReadingProgress.objects.filter(member=self.request.user.member)

class ReadingProgressCreateView(CreateView):
    model = ReadingProgress
    fields = ['member', 'book', 'progress_percentage']
    template_name = 'project/reading_progress_form.html'
    success_url = reverse_lazy('reading-progress-list')

class ReadingProgressUpdateView(UpdateView):
    model = ReadingProgress
    fields = ['progress_percentage', 'comments']
    template_name = 'project/reading_progress_form.html'
    success_url = reverse_lazy('reading-progress-list')

class ReadingProgressListView(ListView):
    model = ReadingProgress
    template_name = 'project/reading_progress_list.html'
    context_object_name = 'progress'

@method_decorator(login_required, name='dispatch')
class MyProfileView(TemplateView):
    template_name = 'project/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        member = self.request.user.member
        context['member'] = member
        context['books'] = Book.objects.filter(readingprogress__member=member).distinct()
        context['progress'] = ReadingProgress.objects.filter(member=member)
        return context

def homepage(request):
    total_books = Book.objects.count()
    total_members = Member.objects.count()
    upcoming_meetings = Meeting.objects.filter(date__gte=now()).order_by('date')[:5]

    context = {
        'total_books': total_books,
        'total_members': total_members,
        'upcoming_meetings': upcoming_meetings,
    }
    return render(request, 'project/homepage.html', context)

def custom_logout(request):
    logout(request)
    return redirect('homepage')