from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    join_date = models.DateField()
    role = models.CharField(max_length=50, choices=[('Admin', 'Admin'), ('Member', 'Member')])

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    publication_year = models.IntegerField()
    isbn = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Meeting(models.Model):
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    agenda = models.TextField()
    notes = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name='meetings')

    def __str__(self):
        return f"Meeting on {self.date.strftime('%Y-%m-%d')} at {self.location}"


class ReadingProgress(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='progess')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='progress')
    progress_percentage = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member.name} - {self.book.title} ({self.progress_percentage}%)"