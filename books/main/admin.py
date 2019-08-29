from django.contrib import admin
from main.models import Book

class BookAdmin(admin.ModelAdmin):
    class Meta:
        models = Book
admin.site.register(Book, BookAdmin)

# Register your models here.
