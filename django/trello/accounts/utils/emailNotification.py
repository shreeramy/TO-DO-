from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# from project.settings.dev import EMAIL_HOST_USER


def send_email_notification(email, name, message, template, title, subject):
    context = {
        'name': name,
        'message': message
    }
    html_content = render_to_string(template, context)

    email = EmailMultiAlternatives(title, subject,
                                   EMAIL_HOST_USER, [email, ])
    email.attach_alternative(html_content, 'text/html')
    email.send()