from django.urls import path
from .views import homepage, MemberListView, MemberDetailView, BookListView, BookDetailView, MemberCreateView, MemberDeleteView, MemberUpdateView, BookCreateView, BookDeleteView, BookUpdateView, MeetingCreateView, MeetingDeleteView, MeetingDetailView, MeetingListView, MeetingUpdateView, ReadingProgressListView, ReadingProgressCreateView, ReadingProgressUpdateView

urlpatterns = [
    path('', homepage, name='homepage'),
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('members/add/', MemberCreateView.as_view(), name='member-add'),
    path('members/<int:pk>/edit/', MemberUpdateView.as_view(), name='member-edit'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('meetings/', MeetingListView.as_view(), name='meeting-list'),
    path('meetings/<int:pk>/', MeetingDetailView.as_view(), name='meeting-detail'),
    path('meetings/add/', MeetingCreateView.as_view(), name='meeting-add'),
    path('meetings/<int:pk>/edit/', MeetingUpdateView.as_view(), name='meeting-edit'),
    path('meetings/<int:pk>/delete/', MeetingDeleteView.as_view(), name='meeting-delete'),
    path('progress/', ReadingProgressListView.as_view(), name='reading-progress-list'),
    path('progress/add/', ReadingProgressCreateView.as_view(), name='reading-progress-add'),
    path('progress/<int:pk>/edit/', ReadingProgressUpdateView.as_view(), name='reading-progress-edit'),
]
