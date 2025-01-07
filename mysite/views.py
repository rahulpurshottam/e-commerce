from django.http import HttpResponseBadRequest
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render,redirect
from submitform.models import contactEnquiry, Order
from submitform.form import OrderForm
from products.models import Product
from products.models import Review
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from allauth.socialaccount.models import SocialAccount
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver

@receiver(social_account_added)
def send_welcome_email(sender, request, sociallogin, **kwargs):
    user = sociallogin.user 
    if user.email: 
        send_mail(
            'Welcome Mail',
            f'Welcome to Voltex Store, {user.email}. Thank you for signing in to Voltex Store. We hope you enjoy our products.',
            'storevoltex@gmail.com',
            [user.email],  
            fail_silently=False,
        )


def save_social_account_data(user, additional_data):
    try:
        social_account = SocialAccount.objects.get(user=user)
        social_account.extra_data['custom_field'] = additional_data  
        social_account.save()
    except SocialAccount.DoesNotExist:
        pass

def LOGIN(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)  
        except User.DoesNotExist:
            user = None
        
        if user is None:
            messages.info(request, 'Email not registered. Please continue with Google.')
            return render(request, "login.html", {'title': 'Voltex Store - Login'})

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            try:
                social_account = SocialAccount.objects.get(user=user)
                if social_account:
                    social_account.extra_data['profile_data'] = 'Some extra data'  
                    social_account.save()
            except SocialAccount.DoesNotExist:
                messages.info(request, 'No social account linked. Please continue with Google to link your account.')
            
        
            

    return render(request, "login.html", {'title': 'Voltex Store - Login'})

@login_required
def homePage(request):
    productsData=Product.objects.all() #[:3]
    reviewData=Review.objects.all() #[:3]

    data = {
        "productsData":productsData,
        "reviewData":reviewData,
        "title": "Voltex Store"
    }
    return render(request, "index.html",data)

def contactUs(request):
    data = {"title": "Voltex Store - Contact Us"}
    msg = ""

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        en = contactEnquiry(name=name, email=email, phone=phone, message=message)
        en.save()
        request.session['msg'] = "Thank you for contacting us! We will get back to you soon."

    msg = request.session.pop('msg', '')  

    
    show_alert = not request.session.get("alert_shown", False)
    request.session["alert_shown"] = True

    return render(request, "contact.html", {"title": "Voltex Store - Contact Us", "msg": msg, "show_alert": show_alert})


def checkout(request):
    product_id = request.GET.get('product_id')  
    if not product_id:
        return HttpResponseBadRequest("Product ID is required.")

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponseBadRequest("Product not found.")

    shipping_charges = 499.0
    discount = 0
    discount_message = ""

    if request.method == 'POST' and request.headers.get('Content-Type') == 'application/json':
        import json
        data = json.loads(request.body)
        promo_code = data.get('promo_code', '').strip()

        if promo_code == 'RAHUL10':
            discount = 0.1 * product.product_price
            discount_message = f"Promo code applied! You saved Rs. {discount:.2f}"
        else:
            discount_message = "Invalid promo code. No discount applied."

        final_price = product.product_price - discount + shipping_charges

        return JsonResponse({
            'discount_message': discount_message,
            'final_price': final_price,
            'discount':discount,
        })

    final_price = product.product_price - discount + shipping_charges
    return render(request, 'checkout.html', {
        'product': product,
        'discount': discount,
        'discount_message': discount_message,
        'final_price': final_price,
        'shipping_charges': shipping_charges,
    })

def save_order(request):
    if request.method == "POST":
        order_data = {
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
            "email": request.POST.get("email"),
            "address": request.POST.get("address"),
            "address2": request.POST.get("address2"),
            "country": request.POST.get("country"),
            "state": request.POST.get("state"),
            "zip_code": request.POST.get("zip_code"),
            "payment_method": request.POST.get("payment_method"),
            "card_name": request.POST.get("card_name"),
            "card_number": request.POST.get("card_number"),
            "expiration": request.POST.get("expiration"),
            "cvv": request.POST.get("cvv"),
            "product_name": request.POST.get("product_name"),
            "product_price": request.POST.get("product_price"),
            "shipping_charges": request.POST.get("shipping_charges"),
        }
        order = Order(**order_data)
        order.save()
        return render(request, "order_success.html", {"message": "Order saved successfully!"})
    return render(request, "checkout.html")

def saveForm(request):
    msg = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        en = contactEnquiry(name=name, email=email, phone=phone, message=message)
        en.save()
        msg = "Thank you for contacting us! We will get back to you soon."

    return render(request, "contact.html", {"title": "Voltex Store - Contact Us", "msg": msg})


def save_order(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        address2 = request.POST.get('address2', '')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        payment_method = request.POST.get('payment_method')
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        expiration = request.POST.get('expiration')
        cvv = request.POST.get('cvv')
        product_name = request.POST.get('product_name')
        product_price = request.POST.get('product_price')
        shipping_charges = request.POST.get('shipping_charges')

        
        order = Order(
            first_name=first_name,
            last_name=last_name,
            email=email,
            address=address,
            address2=address2,
            country=country,
            state=state,
            zip_code=zip_code,
            payment_method=payment_method,
            card_name=card_name,
            card_number=card_number,
            expiration=expiration,
            cvv=cvv,
            product_name=product_name,
            product_price=product_price,
            shipping_charges=shipping_charges,
        )
        order.save()

        return JsonResponse({"message": "Order saved successfully!"}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=400)








