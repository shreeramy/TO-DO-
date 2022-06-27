from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from . models import UserAccount, UserOTP
from cerberus import Validator
from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .utils.messages import Messages
from .utils.otp_generator import generateOTP
from datetime import datetime, timezone
from .utils.emailNotification import send_email_notification
from rest_framework_simplejwt.tokens import RefreshToken
from . serializers import UserSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


# Create your views here.


def forgot_password(request, uidb64=None, token=None):
    """
    This is an view it's called when user click email forgot password link
    """
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserAccount.objects.get(pk=uid)
    except ObjectDoesNotExist:
        user = None
    if request.method == 'POST':
        password1 = request.POST["password1"]
        password = request.POST['password']
        if password == password1:
            password = make_password(password)
            UserAccount.objects.filter(pk=uid).update(password=password)
            return render(request, 'email/password_done.html')
        else:
            messages.info(request, "password not match")
    elif user and default_token_generator.check_token(user, token):
        return render(request, 'email/password_change.html')
    else:
        return render(request, 'email/link_expired.html')


@permission_classes((AllowAny, ))
class ForgotPassword(APIView):
    def post(self, request):
        """
        Forgot password
        ---
        parameters
        ---
        {
            "email": "sp@gmail.com"
        }
        ---
        Response
        ---
        {
            'message': "Link has been sent to your email"
        }
        """
        try:
            # Validate the request
            schema = {
                "email": {'type': 'string', 'required': True, 'empty': False}
            }
            v = Validator()
            if not v.validate(request.data, schema):
                return Response(
                    {'error': v.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user = UserAccount.objects.filter(
                email=(request.data.get('email')).lower())
            if not user.exists():
                return Response({"message": Messages.EMAIL_NOT_VALID}, status=status.HTTP_400_BAD_REQUEST)
            current_site = get_current_site(request)
            kwargs = {
                "uidb64": urlsafe_base64_encode(force_bytes(user.first().pk)).encode().decode(),
                "token": default_token_generator.make_token(user.first())
            }
            activation_url = reverse("accounts:forgot_password", kwargs=kwargs)
            activate_url = "{0}://{1}{2}".format(request.scheme,
                                                 request.get_host(), activation_url)

            context = {
                'user': user.first().name,
                'activate_url': activate_url,
                'domain': request.scheme + "://" + request.get_host()
            }
            html_content = render_to_string(
                'email/forgot_password.html', context)

            email = EmailMultiAlternatives('Reset password', 'Reset your password',
                                           EMAIL_HOST_USER, [user.first().email, ])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            return Response({"message": Messages.LINK_SENT}, status=status.HTTP_200_OK)
        except Exception as exception:
            return Response({"error": str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@permission_classes((AllowAny, ))
class SignUp(APIView):
    def post(self, request):
        """
        User Registration
        ---
        parameters
        ---
        {
            "email": "sp@gmail.com",
            "name": "any name",
            "password": "sp@123",
        }
        ---
        Response
        ---
        {
            'message': "Account created successfully!"
        }
        """
        try:
            # import pdb;pdb.set_trace()
            schema = {
                "email": {'type': 'string', 'required': True, 'empty': False},
                "name": {'type': 'string', 'required': True, 'empty': False},
                "password": {'type': 'string', 'required': True, 'empty': True},
            }
            v = Validator()
            if not v.validate(request.data, schema):
                return Response(
                    {'error': v.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_object = UserAccount.objects.filter(
                email=(request.data.get('email')).lower())
            if user_object.exists():
                return Response({"error": Messages.EMAIL_ALREADY_EXISTS}, status=status.HTTP_400_BAD_REQUEST)

            user_object = UserAccount.objects.create(
                email=(request.data.get('email')).lower(),
                name=request.data.get('name'),
                password=make_password(request.data.get('password')),
                role=1,
            )
            email = request.data.get('email')
            name = request.data.get('name')
            message = Messages.REGISTRATION_GREETINGS
            template = "email/email_notification.html"
            title = "Registration greeting"
            subject = "Registration greeting"
            # send_email_notification(
            #     email, name, message, template, title, subject)
            tokens = RefreshToken.for_user(user_object)
            data = {
                "refresh": str(tokens),
                "access": str(tokens.access_token)
            }
            return Response({"message": Messages.ACCOUNT_CREATED, "data": data}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserProfile(APIView):
    def get(self, request):
        """
        User profile view api
        ---
        parameters
        ---
            No parameters
        ---
        Response
        ---
        {
          "pk": 3,
          "name": "Govind",
          "email": "gb@mailinator.com",
          "role": 1
        }
        """
        return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)

    def put(self, request):
        try:
            user_data = UserAccount.objects.filter(pk=request.user.pk)
            schema = {
                'name': {'type': 'string', 'required': True, 'empty': False},
            }
            v = Validator()
            if not v.validate(request.data, schema):
                return Response({"error": v.errors}, status=status.HTTP_400_BAD_REQUEST)
            user_data.update(
                name=request.data.get('name'),
            )
            return Response({"message": Messages.PROFILE_UPDATED_SUCCESSFULLY}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        """
        User profile delete
        ---
        parameters
        ---
            No parameters
        ---
        Response
        ---
        {
          "message": "Your account deleted successfully!"
        }
        """
        user_object = UserAccount.objects.filter(pk=request.user.pk)
        email = request.user.email
        name = request.user.name
        message = Messages.ACCOUNT_DELETED
        template = "email/email_notification.html"
        title = "Account deleted"
        subject = "Account deleted"
        send_email_notification(email, name, message, template, title, subject)
        user_object.delete()
        return Response({"message": Messages.ACCOUNT_DELETED_SUCCESSFULLY}, status=status.HTTP_204_NO_CONTENT)


class ChangePassword(APIView):
    def post(self, request):
        """
        Change password
        ---
        parameters
        ---
            {
                "new_password": '123',
                "old_password": '900'
            }
        ---
        Response
        ---
        {
          "message": "Password changed successfully!"
        }
        """
        try:
            schema = {
                'new_password': {'type': 'string', 'required': False, 'empty': False},
                'old_password': {'type': 'string', 'required': False, 'empty': False},
            }
            v = Validator()
            if not v.validate(request.data, schema):
                return Response({"error": v.errors}, status=status.HTTP_400_BAD_REQUEST)

            if not request.user.check_password(request.data.get('old_password')):
                return Response({"error": Messages.INVALID_PASSWORD}, status=status.HTTP_400_BAD_REQUEST)

            user_object = UserAccount.objects.filter(pk=request.user.pk)
            user_object.update(
                password=make_password(request.data.get('new_password'))
            )
            return Response({"message": Messages.PASSWORD_CHANGED}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
