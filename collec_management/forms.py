from django.forms import ModelForm
from collec_management.models import Collec, Element


class FormPost(ModelForm):
    class Meta:
        model = Collec
        fields = ["title", "description"]

        labels = {
            "title" : "Titre",
            "descritpion" : "descritpion"
        }
class ElementPost(ModelForm):
    class Meta:
        model = Element
        fields = ["title", "description", "value", "quantity", "collection"]

        labels = {
            "title" : "Titre",
            "description" : "Description",
            "value" : "Vleur",
            "quantity" : "Quantité",
            "collection" : "Collection"
        }


