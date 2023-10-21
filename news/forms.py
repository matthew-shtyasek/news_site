from django import forms


class SearchForm(forms.Form):
    search_field = forms.CharField(max_length=128)


class SortForm(forms.Form):
    SORTING_CHOICES = (('n2o', 'От новых к старым'),
                       ('o2n', 'От старых к новым'),
                       ('a-z', 'От А до Я'),
                       ('z-a', 'От Я до А'))

    sort_field = forms.ChoiceField(choices=SORTING_CHOICES)
    current_tag = forms.CharField(widget=forms.HiddenInput, required=False)
