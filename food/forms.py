from django import forms

from .models import Donar_Model,Agent_Model,Assign_Model


class Donar_ModelCreate(forms.ModelForm):

    orphanes = [
        ('vij', 'Vijayawada'),
        ('Gun', 'Gunturu'),
      ]

    def donarregister(request):

    upload=DonarRegister_ModelCreate()

    if request.method=='POST':
        
        upload=DonarRegister_ModelCreate(request.POST,request.FILES)

        if upload.is_valid():

            upload.save()

            return redirect('donatersuccess')
        
    else:
        
        return render(request,'donateregister.html',{'upload_form':upload})

    fullname=forms.CharField(label='Full Name',widget=forms.TextInput(attrs={'class':"form-control"}))
    
    email=forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
  
    fooditems=forms.CharField(label='Food Items', widget=forms.TextInput(attrs={'class': "form-control"}))
  
    address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
    
    phone=forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': "form-control"}))
    
    orphanage = forms.ChoiceField(label='Orphanages', widget=forms.Select(attrs={'class': "form-control"}), choices=orphanes)
   
    date=forms.CharField(label='Date Of Donation', widget=forms.widgets.DateInput(attrs={'class': "form-control",'type':"date"}))
  
    class Meta:

        model=Donar_Model

        fields='__all__'

class Agent_ModelCreate(forms.ModelForm):

  name=forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class':"form-control"}))
    
  password=forms.CharField(label='Password',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  email=forms.CharField(label='Email',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  phone=forms.CharField(label='Phone',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  address = forms.CharField(label='Address',widget=forms.Textarea(attrs={'class': "form-control"}))
   

  class Meta:

        model=Agent_Model

        fields='__all__'

class Assign_ModelCreate(forms.ModelForm):

  cid=forms.IntegerField(label='Customer Id',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  aid=forms.IntegerField(label='Agent Id',widget=forms.TextInput(attrs={'class':"form-control"}))
  
  class Meta:

    model=Assign_Model

    fields='__all__'


