from django.contrib.auth.forms import UserCreationForm


# django의 무시무시한 form class 상속!!! 미리 다 만들어져 있다!!
class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True


