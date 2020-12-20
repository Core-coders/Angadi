from allauth.account.forms import SignupForm

class UserSignupForm(SignupForm):
    def save(self, request):
        user = super(UserSignupForm, self).save(request)
        user.ration_no = self.cleaned_data.get('ration_no')
        user.save()
        return user

class RationSignupForm(SignupForm):

    def save(self, request):
        user = super(RationSignupForm, self).save(request)
        user.user_type = 2
        user.ration_no = self.cleaned_data.get('ration_no')
        user.save()
        return user

class FoodSignupForm(SignupForm):

    def save(self, request):
        user = super(RationSignupForm, self).save(request)
        user.user_type = 3
        user.save()
        return user