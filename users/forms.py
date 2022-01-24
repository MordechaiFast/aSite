from django.contrib.auth.forms import UserCreationForm

class UserCreationFormEMail(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email', )