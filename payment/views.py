from django.shortcuts import render, redirect
from django.conf import settings 
from django.urls import reverse
from django.contrib import messages
from django.views.generic.base import TemplateView
import stripe
stripe.api_key = settings.STRIPE_SECRET 

class DonatePageView(TemplateView):
    template_name = 'payment/donate.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE
        return context
    
    
def charge(request): 
    if request.method == 'POST':
        try:
            charge = stripe.Charge.create(
            amount=300,
            currency='gbp',
            description='Beer list donation',
            source=request.POST['stripeToken']
            )
        except stripe.error.CardError:
            messages.error(request, "Your card was declined")
        if charge.paid:
            messages.success(request, "Thanks! You have successfully donated")
            return redirect(reverse('donate'))
        else:
            messages.error(request, 'Unable to take payment')
            
        
    else:
        return redirect(reverse('donate'))  
    
