from allauth.account.views import SignupView
from ..forms import UserSignupForm

class UserSignupRegistrationView(SignupView):
    template_name = 'account/signup.html'
    form_class = UserSignupForm
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(UserSignupRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


UserView = UserSignupRegistrationView.as_view()