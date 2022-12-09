from django import forms
from datetime import date


class MonthlyAttendance(forms.Form):
    month = forms.ChoiceField(required=True, choices=((1, 'January'),
                                                      (2, 'February'),
                                                      (3, 'March'),
                                                      (4, 'April'),
                                                      (5, 'May'),
                                                      (6, 'June'),
                                                      (7, 'July'),
                                                      (8, 'August'),
                                                      (9, 'September'),
                                                      (10, 'October'),
                                                      (11, 'November'),
                                                      (12, 'December'),))

    def __init__(self, request, *args, **kwargs):
        super(MonthlyAttendance, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == 'month':
                self.fields[field].initial = request.GET.get(
                    'month', date.today().month)
