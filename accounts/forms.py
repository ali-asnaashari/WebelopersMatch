from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Product


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'username'}))
    first_name = forms.CharField(required=False, help_text='Optional.',
                                 widget=forms.TextInput(attrs={'id': 'first_name'}))
    last_name = forms.CharField(required=False, help_text='Optional.',
                                widget=forms.TextInput(attrs={'id': 'last_name'}))
    email = forms.EmailField(help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'id': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'password2'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class CreateItemForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'name': 'name'}))
    quantity = forms.CharField(required=True, widget=forms.TextInput(attrs={'name': 'quantity'}))
    price = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'name': 'price'}))
    tag = forms.CharField(required=False, widget=forms.TextInput(attrs={'name': 'tag'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_image'].widget.attrs.update({'id': 'product_image'})


    def set_initial(self, name_text='', price_text=0, quantity_text=0):
        # self.name.initial = name_text
        # self.price.initial = price_text
        # self.quantity.initial = quantity_text
        pass

    class Meta:
        model = Product
        fields = ('name', 'quantity', 'price', 'tag', 'product_image', 'user', )
        widgets = {
            'user': forms.HiddenInput,
            # 'product_image':forms.FileField(widget=forms.ImageField(at))
            # 'comments': forms.HiddenInput(attrs={'required':False}),
            # 'tag': forms.HiddenInput(attrs={'required':False}),

        }
