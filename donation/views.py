from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Donation
from .forms import DonationForm


# Create your views here.
def sign_up(request):
    return render(request, 'donation/sign_up.html')

def donation_list(request):
    donations = Donation.objects.order_by('-donationAmount')
    return render(request, 'donation/donation_list.html', {'donations': donations})

def donation_details(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    return render(request, 'donation/donation_details.html', {'donation': donation})

@login_required
def donation_new(request):
    if request.method == "POST":
        form = DonationForm(request.POST)
        if form.is_valid():
            donationpost = form.save(commit=False)
            donationpost.donator = request.user
            donationpost.donationDate = timezone.now()
            donationpost.save()
            return redirect('donation_details', pk=donationpost.pk)
    else:
        form = DonationForm()
    return render(request, 'donation/donation_edit.html', {'form': form})

# Double Check donation edit vvv
def donation_edit(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == "POST":
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.donationDate = timezone.now()
            donation.save()
            return redirect('donation_details', pk=donation.pk)
    else:
        form = DonationForm(instance=donation)
    return render(request, 'donation/donation_edit.html', {'form': form})

# leaderboard
#Donation.objects.order_by('-donationAmount')