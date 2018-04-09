from django.shortcuts import render, redirect
from django.urls import reverse
from example.forms import ContactForm

from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def main(request):
	form = ContactForm(request.POST)

	if request.method == 'POST':
		
		
		if form.is_valid():
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject,message, email, ['admin@admin.py'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect(reverse('example/main'))

	return render(request, "example/main.html", {'form' : form})