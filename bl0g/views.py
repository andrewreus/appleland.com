from django.shortcuts import render, get_object_or_404
from .models import Mod, Categories
from django.views.generic import ListView


class AppleLand(ListView):
    model = Mod
    template_name = 'bl0g/appleland_list.html'


"""
def appleland(request):
    mods = Mod.objects.all()
    context = {
        'mods': mods,
        'name': 'AppleLand',
    }
    return render(request, template_name='bl0g/index.html', context=context)
"""
def get_category(request, category_id):
    mods = Mod.objects.filter(category_id=category_id)
    category = Categories.objects.get(pk=category_id)
    return render(request, 'bl0g/categories.html', {'mods': mods, 'category': category})

def view_mod(request, mod_id):
    mod_item = get_object_or_404(Mod, pk=mod_id)
    # mod_item = Mod.objects.get(pk=mod_id)
    return render(request, 'bl0g/view_mod.html', {'mod_item': mod_item})
