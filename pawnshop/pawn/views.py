from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import Pledge 
# Create your views here.
def index(request):
    latest_pledges = Pledge.objects.all().order_by('-pledge_no')[:5]
    return render_to_response('pawn/index.html', {'latest_pledges': latest_pledges})