from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import threading
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=45)

@receiver(post_save, sender=Book)
def book_saved(instance, **kwargs):
        """Question 1:
        By default, Django signals are executed synchronously. 
        using time.sleep to simulate a delay in signal execution and 
        observe that the code execution halts while the signal is processed.
        """
        print(f"Saving book: {instance.title}")    
        time.sleep(2)
        print("Book saved")





class Author(models.Model):
      name = models.CharField(max_length=45)        

@receiver(post_save, sender=Author)
def author_saved(instance, **kwargs):
      """Question 2:
      By default, Django signals run in the same thread as the caller.
      By printing the thread identifiers in both the caller and the signal handler to compare them.
      """
      print(f"Author saved: {instance.name} in thread: {threading.current_thread().name}")
      print("Caller Thread ID:", threading.get_ident())





class Product(models.Model):
      name = models.CharField(max_length=45)

@receiver(post_save, sender=Product)
def porduct_saved(instance, **kwargs):
      """Question 3:
      by default, Django signals run in the same database transaction as the caller.
      """
      print(f"Product: {instance.name} has been saved")            