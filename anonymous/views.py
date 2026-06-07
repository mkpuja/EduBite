from django.shortcuts import render, redirect
from .models import Register, Food, Cart, Order
# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:

            Register.objects.create(
                name=name,
                email=email,
                phone=phone,
                password=password
            )

            return redirect('/login/')

    return render(request, 'register.html')


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            user = Register.objects.get(
                email=email,
                password=password
            )

            request.session["user_id"] = user.id
            request.session["user_name"] = user.name

            return redirect("/dashboard/")

        except Register.DoesNotExist:

            return render(
                request,
                "login.html",
                {"error":"Invalid Email or Password"}
            )

    return render(request, "login.html")


def dashboard(request):

    if "user_id" not in request.session:
        return redirect("/login/")

    return render(request, "dashboard.html")
def menu(request):

    search = request.GET.get('search')
    category = request.GET.get('category')

    foods = Food.objects.all()

    if search:
        foods = foods.filter(
            name__icontains=search
        )

    if category and category != "All":
        foods = foods.filter(
            category=category
        )

    return render(
        request,
        "menu.html",
        {
            "foods": foods
        }
    )
def cart(request):

    if "user_id" not in request.session:
        return redirect('/login/')

    user = Register.objects.get(
        id=request.session["user_id"]
    )

    cart_items = Cart.objects.filter(
        user=user
    )

    subtotal = 0

    total_items = 0

    for item in cart_items:

        subtotal += item.food.price * item.quantity

        total_items += item.quantity

    total = subtotal + 40

    return render(
        request,
        "cart.html",
        {
            "cart_items": cart_items,
            "subtotal": subtotal,
            "total_items": total_items,
            "total": total
        }
    )
def orders(request):

    if "user_id" not in request.session:
        return redirect('/login/')

    user = Register.objects.get(
        id=request.session["user_id"]
    )

    orders = Order.objects.filter(
        user=user
    )

    return render(
        request,
        "orders.html",
        {"orders": orders}
    )
def profile(request):

    if "user_id" not in request.session:
        return redirect('/login/')

    user = Register.objects.get(
        id=request.session["user_id"]
    )

    return render(
        request,
        "profile.html",
        {"user": user}
    )


def viewdata(request):

    users = Register.objects.all()

    return render(request,"viewdata.html",{"users": users})
def edit(request, id):

    user = Register.objects.get(id=id)

    if request.method == "POST":

        user.name = request.POST['name']
        user.email = request.POST['email']
        user.phone = request.POST['phone']

        user.save()
        return redirect('/viewdata/')
    return render(request,'edit.html',{'user': user})

def delete(request, id):
    user = Register.objects.get(id=id)
    user.delete()
    return redirect('/viewdata/')
def logout(request):

    request.session.flush()

    return redirect('/login/')
def add_to_cart(request, food_id):

    if "user_id" not in request.session:
        return redirect('/login/')

    user = Register.objects.get(
        id=request.session["user_id"]
    )

    food = Food.objects.get(id=food_id)

    existing_item = Cart.objects.filter(
        user=user,
        food=food
    ).first()

    if existing_item:

        existing_item.quantity += 1

        existing_item.save()

    else:

        Cart.objects.create(
            user=user,
            food=food,
            quantity=1
        )

    return redirect('/cart/')
def remove_cart(request, cart_id):

    cart_item = Cart.objects.get(id=cart_id)

    cart_item.delete()

    return redirect('/cart/')
def place_order(request):

    if "user_id" not in request.session:
        return redirect('/login/')

    user = Register.objects.get(
        id=request.session["user_id"]
    )

    cart_items = Cart.objects.filter(user=user)

    for item in cart_items:

        Order.objects.create(
            user=user,
            food=item.food,
            quantity=item.quantity,
            total_price=item.food.price * item.quantity,
            status="Pending"
        )

    cart_items.delete()

    return redirect('/orders/')

def decrease_cart(request, cart_id):

    item = Cart.objects.get(id=cart_id)

    if item.quantity > 1:

        item.quantity -= 1

        item.save()

    else:

        item.delete()

    return redirect('/cart/')

def cancel_order(request, order_id):

    order = Order.objects.get(id=order_id)

    if order.status == "Pending":

        order.status = "Cancelled"

        order.save()

    return redirect('/orders/')