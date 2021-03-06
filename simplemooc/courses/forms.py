from django import forms
#from django.core.mail import send_mail
from django.conf import settings

from simplemooc.core.mail import send_mail_template

class ContactCourse(forms.Form):

  name = forms.CharField(label='Name', max_length=100) # required=True/False
  email = forms.EmailField(label='E-mail')
  message = forms.CharField(label='Message', widget=forms.Textarea)

  def send_mail(self, course):
    subject = '[%s] Contact' % course # Not named string

    # message = 'Name: %(name)s; E-mail: %(email)s; %(message)s' # Named string

    context = {
      'name': self.cleaned_data['name']
      , 'email': self.cleaned_data['email']
      , 'message': self.cleaned_data['message']
    }

    # message = message % context

    template_name = 'courses/contact_email.html'

    send_mail_template(
      subject
      , template_name
      , context
      , [settings.CONTACT_EMAIL]
    )
