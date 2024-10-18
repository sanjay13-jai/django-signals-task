# Django Signals Assignment

This project demonstrates the implementation of Django signals and explores questions about their execution, such as whether they run within the same thread and transaction, and whether they are synchronous or asynchronous.

## Code Overview

- The **Django signal-related code** can be found in the `models.py` file inside the `signals_app` Django app.
- The **test cases** illustrating the behavior of these signals are located in the `tests.py` file within the same app.

## How to Run the Code

1. Make sure you have **Django installed** and that your virtual environment is activated (if you're using one).

2. Navigate to the root directory of the project.

3. To run the test cases and observe the behavior of Django signals, use the following command:

   ```bash
   python manage.py test signals_app
   ```
