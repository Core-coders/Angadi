from allauth.account.views import SignupView
from ..forms import FoodSignupForm

class FoodUserRegistrationView(SignupView):
    template_name = 'account/signup_organiser.html'
    form_class = FoodSignupForm
    
    success_url = None

    def get_context_data(self, **kwargs):
        ret = super(FoodUserRegistrationView, self).get_context_data(**kwargs)
        ret.update(self.kwargs)
        return ret


FoodView = FoodUserRegistrationView.as_view()