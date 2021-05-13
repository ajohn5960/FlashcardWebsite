from django import forms





class CreateSetForm(forms.Form):
    name = forms.CharField(max_length=100, label='',
                                     widget=forms.TextInput(
                                         attrs={
                                             'placeholder': 'Enter Set Name'
                                             }))
    
    is_private = forms.BooleanField(initial=False, required=False)
    
    def __init__(self,*args,**kwargs):
        self.name = kwargs.pop('name', None)   
        super(CreateSetForm,self).__init__(*args,**kwargs)
        self.fields['name'].initial = self.name
        

    def clean(self):
        cleaned_data = super(CreateSetForm, self).clean()
        name = cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('You have to write something!')




class SetFlashcardForm(forms.Form):
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
        super(SetFlashcardForm,self).__init__(*args,**kwargs)
        self.empty_permitted = False
        self.fields['side_one'].initial = self.side_one
        self.fields['side_two'].initial = self.side_two
        

    def clean(self):
        cleaned_data = super(SetFlashcardForm, self).clean()





class SortSetForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.set_initial = kwargs.pop('set_initial', "Last Modified")
        super().__init__(*args, **kwargs)
        self.fields['sort_by'].widget.attrs.update({'class': 'submit'})
        self.fields['sort_by'].initial = self.set_initial

    CREATED_ON = "Created On"
    LAST_MODIFIED = "Last Modified"
    ALPHABETICAL = "Alphabetical"
    LAST_STUDIED = "Recently Studied"
    

    sort_by_choices =( 
        ( LAST_MODIFIED, "Last Modified"), 
        ( CREATED_ON, "Created On"), 
        ( ALPHABETICAL, "Alphabetical"), 
        ( LAST_STUDIED, "Recently Studied")
    ) 
    
    sort_by = forms.ChoiceField( choices=sort_by_choices)


   

   
