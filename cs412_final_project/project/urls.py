from django.urls import path
from .views import MemberListView, MemberDetailView, BookListView, BookDetailView

urlpatterns = [
    path('members/', MemberListView.as_view(), name='member-list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member-detail'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]
