from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import transactiontypes
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'core/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required
def transactions(request):
    def transactions(request):
        transactions = transactiontypes.objects.all()
    # Add logic for transactions here
    return render(request, 'core/transactions.html',{'transactions': transactions})

def tran_details(request, tran_id):
    tran = get_object_or_404(transactiontypes, pk = tran_id)
    return render(request, 'templates/core/tran_details.html',{'tran': tran})

def debug_image(request, image_name):
       image_path = os.path.join(settings.MEDIA_ROOT, 'transactions', image_name)
       if os.path.exists(image_path):
           with open(image_path, 'rb') as image_file:
               return HttpResponse(image_file.read(), content_type="image/jpeg")
       else:
           return HttpResponse(f"Image not found at {image_path}", status=404)