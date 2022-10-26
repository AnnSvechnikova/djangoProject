from django.shortcuts import render
from django.http import HttpResponse
from datetime import date


# Create your views here
from lab1.models import Books


"""def GetData():
   return {
        'current_date': date.today(),
        'books': [
            {'id': 1, 'title': 'Марсианские хроники', 'in_stock': 4, 'descr': 'Рассказы о путешествиях на Марс', 'img': 'img/martian.jpg'},
            {'id': 2, 'title': 'Академия', 'in_stock': 5, 'descr': 'История галактической научной организации', 'img': 'img/academia.jpg'},
            {'id': 3, 'title': 'Макбет', 'in_stock': 0, 'descr': 'Трагедия о предательстве и жажде власти', 'img': 'img/macbeth.jpg'},
            {'id': 4, 'title': 'Шум и ярость', 'in_stock': 3, 'descr': 'Семейная трагедия в жанре потока сознания', 'img': 'img/sound_fury.jpg'},
            {'id': 5, 'title': 'Финансист', 'in_stock': 1, 'descr': 'История талантливого беспринципного бизнесмена', 'img': 'img/finance.jpg'},
        ]
   }"""
def GetData():
    return {
        'current_date': date.today(),
        'books': Books.objects.all()
    }


def GetBooks(request):
   return render(request, 'books.html', {'data': GetData()})


def GetBook(request, id):
   # book = list(filter(lambda x: x['id'] == id, GetData()['books']))
   return render(request, 'book.html', {'data': Books.objects.filter(book_id=id)[0]})




