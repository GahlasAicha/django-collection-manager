from django.shortcuts import render, get_object_or_404, redirect
from .models import Collec, Element
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden
from collec_management.forms import *
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def about(request):
    return render(request, 'collec_management/about.html')

@login_required
def collection_detail(request, n):
    collection = get_object_or_404(Collec, id=n)
    if collection.createur != request.user:
        return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")
    elements = collection.elements.all()
    return render(request, 'collec_management/collection_detail.html', {'collection': collection, 'element' : elements})


def index(request):
    collect = Collec.objects.order_by("id")
    context = {"all_collec":collect}
    return render(request, "collec_management/collection_liste.html", context)

"""def new_collec(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.date_creation = timezone.now()
            c.save()

        return HttpResponseRedirect(f"/collection/{c.id}/")
    else:
        form = FormPost()

    return render(request, "collec_management/ajout.html", {"form": form})
"""

def check_save(form, request):
    if form.is_valid():
        coll = form.save(commit=False)
        coll.date_creation = timezone.now()
        coll.createur = request.user
        coll.save()
    return coll.id

@login_required
def new_collec(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        id = check_save(form, request)
        return redirect("collection_detail", n=id)
    else:
        form = FormPost()
    return render(
        request,
        "collec_management/ajout.html",
        {"form": form, "button_label": "Nouvelle Collection"},
    )

@login_required
def delete_collec(request, collec_id):
    col = get_object_or_404(Collec, pk=collec_id)
    if col.createur != request.user:
        return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")
    if request.method == "POST":
        col.delete()
        return redirect("index")
    return render(request, "collec_management/delete_collec.html",{"collection": col})

@login_required
def edit_collec(request, collec_id):
    c = get_object_or_404(Collec, pk=collec_id)

    if c.createur != request.user:
        return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")

    if request.method == "POST":
        form = FormPost(request.POST, instance=c)
        id = check_save(form, request)
        return redirect("collection_detail", n=id)
    else:
        form = FormPost(instance=c)
    return render(
        request,
        "collec_management/ajout.html",
        {"form": form, "button_label": "Modifier"},
    )

def menu(request):
    return render(request, "collec_management/menu.html")



#parti element

def check_save_id(form, request):
    if form.is_valid():
        el = form.save(commit=False)
        el.createur = request.user
        el.save()
        
        return el.id

@login_required
def ajout_element(request):
    if request.method == "POST":
        form = ElementPost(request.POST)
        id = check_save_id(form, request)
        return redirect("element_detail", id)
    else:
        form = ElementPost()
    return render(
        request,
        "collec_management/ajout_element.html",
        {"form": form, "button_label": "Ajouter un Element"},
    )


@login_required
def delete_element(request, element_id):
    el = get_object_or_404(Element, pk=element_id)

    if el.createur != request.user:
        return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")
    
    if request.method == "POST":
        el.delete()
        return redirect("menu")
    return render(request, "collec_management/delete_element.html",{"element": el})


@login_required
def element_detail(request, n):
    element = get_object_or_404(Element, id=n)

    if element.createur != request.user:
        return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")

    return render(request, 'collec_management/element_detail.html', {'element': element})


@login_required
def edit_element(request, element_id):
    e = get_object_or_404(Element, pk=element_id)

    if e.createur != request.user:
        return HttpResponseForbidden("Vous n'avez pas le droit d'accèder à cette page")

    if request.method == "POST":
        form = ElementPost(request.POST, instance=e)
        id = check_save_id(form, request)
        return redirect("element_detail", n=id)
    else:
        form = ElementPost(instance=e)
    return render(
        request,
        "collec_management/ajout_element.html",
        {"form": form, "button_label": "Modifier Element"},
    )

#pour le login




    


