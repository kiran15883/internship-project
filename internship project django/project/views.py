from django.shortcuts import render
import razorpay
from .models import Coffee
# Create your views here.
def home(request):
    if(request.method=="POST"):
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))*100
        client = razorpay.Client(auth=("rzp_test_kINEe99kmcov0U","DtdXkUnQ1GLbVZbDuJkJP9A0"))
        payment = client.order.create({'amount':amount, 'currency':'INR','payment_capture':'1'})
        coffee = Coffee(name=name, amount=amount,payment_id= payment['id'])
        coffee.save()
        return render(request,"index.html",{'payment':payment})
    return render(request,"index.html")

def success(request):
    #if(request.method=="POST"):
      #  a = request.POST
        
    return render(request,"success.html")    