from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import (
    FlashcardForm, 
    DynamicFlashcardForm
)
from set.forms import CreateSetForm
from .models import Flashcard
from .models import Set
from django.forms import formset_factory 



def flashcard_create_view(request):
    form = FlashcardForm(request.POST or None )
    if form.is_valid():
        set = form.cleaned_data['set']
        side_one = form.cleaned_data['side_one']
        side_two = form.cleaned_data['side_two']
        flashcard = Flashcard(set=set, side_one=side_one, side_two=side_two )
        flashcard.save()


    context ={
        'form' : form,
    }
    return render(request, "flashcard_create.html", context)


def flashcard_dynamic_create(request):
    set_form = CreateSetForm(request.POST or None)
    FlashcardFormSet = formset_factory(DynamicFlashcardForm)
    data = {
        'form-TOTAL_FORMS': '1',
        'form-INITIAL_FORMS': '0',
    }
    flashcard_formset = FlashcardFormSet(data,request.POST or None)     
    
    if flashcard_formset.is_valid() and set_form.is_valid():
        set_name = set_form.cleaned_data['name']
        set = Set(user=request.user, name=set_name)
        set.save()
        for flashcard_form in flashcard_formset:
            side_one = flashcard_form.cleaned_data['side_one']
            side_two = flashcard_form.cleaned_data['side_two']
            flashcard = Flashcard(set=set, side_one=side_one, side_two=side_two )
            flashcard.save()

    else:
        print("\nform not valid")
        print(str(flashcard_formset.errors))

    context ={
        'set_form' : set_form,
        'flashcard_form' :flashcard_formset
    }
    
    return render(request, "flashcard_dynamic_create.html", context)



def flashcard_edit_view(request, flashcard_id):
    my_flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    form = FlashcardForm(request.POST or None, 
                            set=my_flashcard.set, 
                            side_one=my_flashcard.side_one,
                            side_two=my_flashcard.side_two
                        )
    if form.is_valid():
        side_one = form.cleaned_data['side_one']
        side_two = form.cleaned_data['side_two']
        Flashcard.objects.filter(id=flashcard_id).update(
                side_one=side_one,
                side_two=side_two
            )
    else:
        print("invalid form")

    context ={
        'form' : form
    }
    return render(request, "flashcard_edit.html", context)



def flashcard_delete_view(request, flashcard_id):
    my_flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    if request.method == "POST":
        my_flashcard.delete()
        return redirect('sets:list_sets')
    context ={
        'flashcard' : my_flashcard
    }
    return render(request, "flashcard_delete.html", context)

def flashcard_detail_view(request, flashcard_id):
    my_flashcard = get_object_or_404(Flashcard, id =flashcard_id)
    context ={
        "flashcard" : my_flashcard
    }
    return render(request, "flashcard_detail.html", context)


def flashcard_list_view(request):
    queryset = Flashcard.objects.all()
    queryset = Flashcard.objects.filter()                                                                                                 
    context ={
        'flashcard_list' : queryset
    }
    return render(request, "flashcard_list.html", context)
