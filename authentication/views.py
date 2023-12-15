import os
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserRegistrationForm
from django.contrib.auth.decorators import login_required
# authentication/views.py

from .models import CustomUser
from django.urls import reverse_lazy

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('authentication:login')  # Redirect to the login page after logout


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        # return super().form_valid(form)  # Call the parent class method for successful login
        return redirect('authentication/dashboard')

# class CustomLogoutView(LogoutView):
#     next_page = 'authentication:login'  # Redirect to the login page after logout

def register(request):
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('authentication:login'))  # Redirect to the login page using the URL name
    else:
        form = CustomUserRegistrationForm()
    return render(request, "authentication/register.html", {"form": form})

@login_required
def dashboard(request):
    return render(request,'authentication/dashboard.html')

def home(request):
    return render(request, 'authentication/home.html')



def create_html_file(request):
    # HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sample HTML Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a sample HTML page created using Python.</p>
    </body>
    </html>

    """

     # Define the directory path to save HTML files
    html_files_directory = os.path.join("authentication", "templates", "authentication")

    # Ensure the directory exists
    os.makedirs(html_files_directory, exist_ok=True)

    # Set the filename based on the authenticated user
    if request.user.is_authenticated:
        username = request.user.username + ".html"
        filepath = os.path.join(html_files_directory, username)

        # Writing HTML content to the file
        with open(filepath, "w") as html_file:
            html_file.write(html_content)

    return render(request, "authentication/" + username)


