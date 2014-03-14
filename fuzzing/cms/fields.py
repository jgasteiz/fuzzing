from crispy_forms.layout import Fieldset


class WellFieldset(Fieldset):
    template = 'cms/forms/well_fieldset.html'

    def __init__(self, *args, **kwargs):
        super(WellFieldset, self).__init__(*args, **kwargs)
        self.css_class = 'well'
