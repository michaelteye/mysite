from django import template
from django.db import models
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Item
from django.template import context, loader
from .form import ItemForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView


def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request,'food/index.html', context)

class IndexClassView(ListView):
    model = Item;
    template_name = 'food/index.html'
    context_object_name = 'item_list'


def items(request):
    return HttpResponse('bring it')
def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context={
        'item': item,
    }
    return render(request, 'food/detail.html', context)


class FoodDetail(DetailView):
    model = Item;
    template_name = 'food/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html',{'form':form})

#This is a class based view for create item

class CreateItem(CreateView):
    model = Item;
    fields = ['Item_name', 'Item_desc', 'Item_price', 'Item_image']
    template_name='food/item-form.html'
    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)




def update_item(request, id):
    item= Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html',{'form':form, 'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html',{'item':item})
