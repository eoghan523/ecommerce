from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from .forms import OrderForm

# View for listing all orders
def order_list(request):
    orders = Order.objects.all()  #Calls the objects from the order Database 
    return render(request, 'orders/order_list.html', {'orders': orders})   # Render  order_list.html template

# View for creating a new order
def order_create(request):  # If the request is a POST request, process the form data
    if request.method == 'POST':    # Django checks if the request is HTTP POST
        form = OrderForm(request.POST)  
        if form.is_valid():  #if the form is valid
            form.save() #save
            return redirect('order_list')  #return to order_list view
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

# View for updating an existing order
def order_edit(request, pk):   # Retrieve the order by its primary key
    order = get_object_or_404(Order, pk=pk) 
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)   #Prepopulate the form with the existing data from order
        if form.is_valid():   # Check if the form is valid
            form.save()  #Save
            return redirect('order_list') #  Redirect to the order list view
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

# View for deleting an order
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')   # After deleting, redirect to the order list 
     # If the request is GET, render the confirmation page for deletion
    return render(request, 'orders/order_confirm_delete.html', {'order': order})