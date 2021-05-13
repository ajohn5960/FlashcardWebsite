from django import forms
from .models import Set
from .models import Flashcard


class FlashcardForm(forms.Form):
    set = forms.ModelChoiceField(queryset=Set.objects.all())
    side_one = forms.CharField(max_length=100,
                                 widget=forms.Textarea(
                                    attrs={
                                        "rows": 12,
                                        "cols":75,
                                        "class=":"side_one"
                                    }))
    side_two = forms.CharField(max_length=100,
                                 widget=forms.Textarea(
                                    attrs={
                                        "rows": 12,
                                        "cols":75,
                                        "class=":"side_two"
                                        
                                    }))
    def __init__(self,*args,**kwargs):
        self.set = kwargs.pop('set', None)
        self.side_one = kwargs.pop('side_one', None)
        self.side_two = kwargs.pop('side_two', None)   
        super(FlashcardForm,self).__init__(*args,**kwargs)
        self.fields['set'].initial = self.set
        self.fields['side_one'].initial = self.side_one
        self.fields['side_two'].initial = self.side_two
        

    def clean(self):
        cleaned_data = super(FlashcardForm, self).clean()
        side_one = cleaned_data.get('side_one')
        side_two = cleaned_data.get('side_two')
        if not side_one or not side_two:
            raise forms.ValidationError('You have to write something!')



class DynamicFlashcardForm(forms.Form):
    side_one = forms.CharField(max_length=100,
                                 widget=forms.Textarea(
                                    attrs={
                                        "rows": 12,
                                        "cols":75,
                                    }))
    side_two = forms.CharField(max_length=100,
                                 widget=forms.Textarea(
                                    attrs={
                                        "rows": 12,
                                        "cols":75,
                                    }))
    def __init__(self,*args,**kwargs):
        self.set = kwargs.pop('set', None)
        self.side_one = kwargs.pop('side_one', None)
        self.side_two = kwargs.pop('side_two', None)  
        super(DynamicFlashcardForm,self).__init__(*args,**kwargs)
        self.empty_permitted = False
        self.fields['side_one'].initial = self.side_one
        self.fields['side_two'].initial = self.side_two
        

    def clean(self):
        cleaned_data = super(DynamicFlashcardForm, self).clean()
        side_one = cleaned_data.get('side_one')
        side_two = cleaned_data.get('side_two')
        if not side_one or not side_two:
            raise forms.ValidationError('You have to write something!')





class FlashcardForm2(forms.ModelForm):
    side_one = forms.CharField(max_length=1000,
                                label='',
                                 widget=forms.Textarea(
                                    attrs={
                                        "rows": 6,
                                        "cols": 55,
                                        "class" : "side_one",
                                        "placeholder" : "Enter Term"
                                    }))
    side_two = forms.CharField(max_length=1000,
                                label='',
                                 widget=forms.Textarea(
                                    attrs={
                                        "rows": 6,
                                        "cols": 55,
                                        "class" :"side_two",
                                        "placeholder" : "Enter Definition"
                                    }))
    
    class Meta:
        model = Flashcard 
        fields = [
            'side_one',
            'side_two'
        ]



class StarFlashcardForm(forms.Form):
    star = forms.BooleanField(required=False)