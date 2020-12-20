from allauth.account.views import SignupView
from ..forms import FoodSignupForm,RationSignupForm

class RationUserRegistrationView(SignupView):
    template_name = 'account/signup_ration.html'
    form_class = RationSignupForm
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(RationUserRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


RationView = RationUserRegistrationView.as_view()