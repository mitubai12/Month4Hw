from django import forms
from colorfield.fields import ColorField

from post.models import Cars, Images


class CarForm(forms.Form):
    car_model = forms.CharField()
    title = forms.CharField(max_length=100, min_length=5)
    description = forms.CharField(widget=forms.Textarea)
    # -----------------------------------------------------
    released = forms.DateField()
    mileage = forms.IntegerField()
    color = ColorField(verbose_name="color")
    engine = forms.FloatField()
    wheel = forms.CharField
    condition = forms.CharField(max_length=15)
    transmission = forms.CharField
    category = forms.CharField()


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = Images
        fields = ('image', )


class CarForm2(forms.ModelForm):
    class Meta:
        model = Cars
        fields = ["car_model", "title", "description",
                  "released", "mileage", "color",
                  "engine", "wheel", "condition",
                  "transmission", "category", "price"]
        widgets = {
            'car_model': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Введите название машины',
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Введите текст',
                    'class': 'form-control'
                }
            ),
            'released': forms.TextInput(
                attrs={
                    'placeholder': '',
                    'class': 'form-control'
                }
            ),
            'mileage': forms.NumberInput(
                attrs={
                    'placeholder': 'Введите пробег машины',
                    'class': 'form-control'
                }
            ),
            'color': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'engine': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'wheel': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'condition': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'transmission': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class SearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        max_length=100,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Поиск',
                'class': 'form-control'
            }
        )
    )

    orderings = (
        ('title', 'По заголовку'),
        ('-title', 'По заголовку (обратно)'),
        ('rate', 'По оценке'),
        ('-rate', 'По оценке (обратно)'),
        ('created_at', 'По дате создания'),
        ('-created_at', 'По дате создания (обратно)')
    )

    ordering = forms.ChoiceField(
        required=False,
        choices=orderings,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
