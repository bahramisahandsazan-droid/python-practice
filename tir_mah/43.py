class Book :
    def __init__(self , title , author , rating) : 
        self.title = title
        self.author = author
        self.rating = rating
    def __str__(self) :
        return f'{self.title} by {self.author} - Rating : {self.rating}'
books =[
    Book('ikigay','hektor grasia',5),
    Book('iran' , 'ramin bahrami',5),
    Book('usa','trump',3),
    Book('farsi','ferdosi',4),
    Book('golestan','saadi',2)
]
for book in books :
    print(book)
top_books = [book for book in books if book.rating >4]
print('top rated books : ')
for book in top_books :
    print(book)
average_rating = sum(book.rating for book in books)/ len(books)
print(f'average rating : {average_rating}')
import json 
data = [{'title' : book.title , 'author' : book.author , 'rating' : book.rating} for book in books]
with open('h:/python/tir_mah/books.json' , 'w') as file :
    json.dump(data,file)
print('books saved')








