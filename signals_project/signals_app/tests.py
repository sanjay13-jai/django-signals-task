from django.test import TestCase
from .models import Book, Author, Product
from django.db import transaction
# Create your tests here.

class SignalTests(TestCase):

    def test_book_signal(self):
        print("Creating book...")
        new_book = Book(title="Django for Beginners")
        new_book.save()
        print("Book created")


    def test_author_signal(self):
        print("Creating author...")
        new_author = Author(name="Sanjay Vijayakumar")
        new_author.save()
        print("Author created")

    def test_product_signal(self):
        """
        After the transaction block, it prints the total number of products created in the database.
        """
        try:
            with transaction.atomic():
                print("Creating product...")
                new_product = Product(name="Super Computer")
                new_product.save()
                print("Product created")
        except Exception as err:
            print(f"Error: {err}")   

        print(f"Total products: {Product.objects.count()}")                


class Rectangle:
    """
    creating a Rectangle class with the following requirements:
    1. Aninstance of the Rectangle class requires length:int and width:int to be
    initialized.
    2. Wecaniterate over an instance of the Rectangle class
    3. Whenaninstance of the Rectangle class is iterated over, we first get its length in the
    format: {'length': <VALUE_OF_LENGTH>} followed by the width {width:<VALUE_OF_WIDTH>}
    """
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}



rect = Rectangle(10,5)

for dimension in rect:
    print(dimension)
        