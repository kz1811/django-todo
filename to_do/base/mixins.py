from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseForbidden


class UserShouldBeOwnerMixin(UserPassesTestMixin, LoginRequiredMixin):

    def test_func(self):
        mmodel = self.get_object()
        return self.request.user == mmodel.user

    def handle_no_permission(self):
        return HttpResponseForbidden("You do not have permission to access this object.")

