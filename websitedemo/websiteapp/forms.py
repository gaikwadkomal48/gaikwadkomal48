
from django import forms



class contactUs(forms.Form):



    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),label='Your Name',max_length=50,min_length=4,required=True)  
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),label='Your Email',max_length=50,min_length=8,required=True)
    subject=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Subject'}),label='Subject',max_length=50,min_length=8,required=True)
    message=forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message'}),label='Message',max_length=200,min_length=10,required=True)
    
    # name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),label='Your Name',max_length=50,min_length=4,required=True) 
    # email=forms.EmailField(Widget=forms.EmailInput(attrs={'placefolder':'enter e-mail'}),label='enter e-mail',max_length=50,min_length=4,Required=True)
    # subject=forms.CharField(Widget=forms.TextInput(attrs={'placefolder':'enter subject'}),label='enter a subject',max_length=50,min_length=4,required=True)
    # message=forms.CharField(Widget=forms.Textarea(attrs={'placefolder':'enter message'}),label='enter a subject',max_length=50,min_length=4,required=True)
