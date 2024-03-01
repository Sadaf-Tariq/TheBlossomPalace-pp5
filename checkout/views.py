from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OpTl3B5BjdUEFZ1Y6Whi1A2JjvxKP8fC1r2z5G9myc2FkqhDk1rWDp6BJ5S7tTtnrll1aN35OO8gGsU6lrXVLF100t3YkK8hS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)