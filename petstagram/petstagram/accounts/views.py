from django.contrib.auth import views as auth_views
from django.views import generic as views
from django.urls import reverse_lazy

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from petstagram.accounts.models import Profile
from petstagram.main.models import PetPhoto, Pet


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    # success_url = reverse_lazy('dashboard')


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user_id=self.object.user_id))

        pet_photos = PetPhoto.objects.filter(tagged_pets__in=pets).distinct()

        total_pet_photos_count = len(pet_photos)

        total_likes_count = sum(pp.likes for pp in pet_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_pet_photos_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })

        return context


class EditProfileView(views.UpdateView):
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm


class DeleteProfileView(views.DeleteView):
    template_name = 'accounts/profile_delete.html'
    form_class = DeleteProfileForm


