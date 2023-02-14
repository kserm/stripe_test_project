import stripe
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY

@api_view(['GET'])
def get_item(request, id):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item)
    data = {
        'data': serializer.data,
        'item': item,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    }
    return render(request, 'api/item.html', context=data)


@csrf_exempt
def get_buy(request, id):
    item = Item.objects.get(id=id)
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri(reverse('success')),
            cancel_url=request.build_absolute_uri(reverse('cancel')),
        )
    return JsonResponse({
        'id': checkout_session.id,
        'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY
    })


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


def index(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'api/index.html', context=context)


def success(request):
    return render(request, 'api/success.html')


def cancel(request):
    return render(request, 'api/cancel.html')
