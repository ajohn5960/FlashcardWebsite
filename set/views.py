from django.shortcuts import render, get_object_or_404, redirect
from flashcard.models import Flashcard
from flashcard.views import flashcard_list_view
from flashcard.forms import  FlashcardForm2
from django.forms import modelformset_factory , inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.utils.timezone import activate
from datetime import datetime, timezone

# Create your views here.
from .models import Set
from .forms import (
    CreateSetForm,
    SortSetForm
)


def set_study_view(request, set_id):
    my_set = get_object_or_404(Set, id =set_id)
    flashcard_list = Flashcard.objects.filter(set=my_set)
    # time_zone = request.POST.get('timezone', '')
    # activate(timezone=time_zone) 


    StarFlashcardFormset = modelformset_factory(Flashcard, fields=('star',))  # min_num=flashcard_count
    star_formset = StarFlashcardFormset(request.POST or None, queryset=flashcard_list)


    my_set.last_studied = datetime.now(timezone.utc)
    my_set.save()
    if request.method == 'POST':
        if star_formset.is_valid():

            star_formset.save()
            print("\n\nstar formset valid")
        else:
            print("\n\nstar formset invalid")
            print(str(star_formset.errors))
    

    flashcard_list_view(request)
    context ={
        "my_set" : my_set,
        'flashcard_list' : flashcard_list,
        "star_formset" : star_formset
    }
    return render(request, "set_study.html", context)


@login_required
def set_create_view(request):
    set_form = CreateSetForm(request.POST or None )
    FlashcardFormSet = inlineformset_factory(Set, Flashcard,form = FlashcardForm2,
            fields=('side_one', 'side_two',), extra=3)
     
    formset = FlashcardFormSet()

    if request.method == 'POST':
        if set_form.is_valid():
            set_name = set_form.cleaned_data['name']
            set = Set(user=request.user, name=set_name) 
            time_zone = request.POST.get('timezone', '')
            activate(timezone=time_zone) 
            set.last_modified = datetime.now()
            set.save()
            
            formset = FlashcardFormSet(request.POST, instance=set)

            if formset.is_valid():
                formset.save()
                return redirect(set.get_absolute_url())

    else:
        print("\n\nform is not valid")

       

    context = {
        'formset': formset,
        'set_form': set_form
    }
    return render(request, "set_create.html", context)
    
    
@login_required
def set_edit_view(request, set_id):
    my_set = get_object_or_404(Set, id=set_id, user=request.user)
    set_form = CreateSetForm(request.POST or None, name=my_set.name)
    FlashcardFormSet = inlineformset_factory(Set, Flashcard,form = FlashcardForm2,
        fields=('side_one', 'side_two',), extra=1)
    formset = FlashcardFormSet(instance=my_set)

    if request.method == 'POST':
        if set_form.is_valid():
            set_name = set_form.cleaned_data['name']
            # time_zone = request.POST.get('timezone', '')
            # activate(timezone=time_zone) 
            my_set.name = set_name
            my_set.last_modified = datetime.now(timezone.utc)
            my_set.save()
            formset = FlashcardFormSet(request.POST, instance=my_set)

            if formset.is_valid():
                formset.save()
                return redirect(my_set.get_absolute_url())

    else:
        print("\n\nform is not valid")

       

    context = {
        'formset': formset,
        'set_form': set_form
    }
    return render(request, "set_edit.html", context)




@login_required
def set_delete_view(request, set_id):
    my_set = get_object_or_404(Set, id=set_id, user=request.user)
    if request.method == "POST":
        Set.objects.filter(id=set_id).delete()
        return redirect('sets:list_sets')
    context ={
        'set_name' : my_set.name
    }
    return render(request, "set_delete.html", context)


def set_detail_view(request, set_id):
    my_set = get_object_or_404(Set, id =set_id)
    flashcard_list = Flashcard.objects.filter(set=my_set)

    flashcard_list_view(request)
    context ={
        "my_set" : my_set,
        'flashcard_list' : flashcard_list
    }
    return render(request, "set_detail.html", context)


@login_required
def list_all_sets(request):
    CREATED_ON = "Created On"
    LAST_MODIFIED = "Last Modified"
    ALPHABETICAL = "Alphabetical"
    LAST_STUDIED = "Recently Studied"
    


    sort_form = SortSetForm()
    queryset = Set.objects.filter(user=request.user).order_by('-last_modified')
    

    if request.POST: 
        sort_by = request.POST.get('sort_by', LAST_MODIFIED)
        print(sort_by)   
        if sort_by == CREATED_ON:
            queryset = Set.objects.filter(user=request.user).order_by('-date_created') 
        if sort_by == LAST_MODIFIED:
            queryset = Set.objects.filter(user=request.user).order_by('-last_modified') 
        if sort_by == ALPHABETICAL:
            queryset = Set.objects.filter(user=request.user).order_by('name')
        if sort_by == LAST_STUDIED:
            queryset = Set.objects.filter(user=request.user).order_by('-last_studied')
            
        sort_form = SortSetForm(set_initial=sort_by)
        


    context ={    
        'set_list' : queryset,
        'sort_form' : sort_form
    }
   
    return render(request, "set_list.html", context)




