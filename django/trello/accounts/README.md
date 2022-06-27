# PROFILE MANAGEMENT

## In this app we have api related to profile management.

## PREREQUISITE
    add EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in settings.py file for email.

## API'S COLLECTION OF ACCOUNT APP --
## Registration API
    User first need to verify its email using "/accounts/send-verification-email" API endpoint by passing its email in data.
    Than User get an OTP on email, User need to verify its email using "/accounts/verify-email" API endpoint by passing its email and OTP in data.

    after that user need to register his account using "/accounts/signup" API endpoint by passing name, email, password in data.

## Login API 
    We have used JWT authentication in it.
    ## Getting Token
        "/api/token" API endpoint and pass email and password in data.
    ## Refresh Token
        "/api/refresh-token" API endpoint and pass refresh token in data.

## Profile Operations
    ## View Profile
        call "/accounts/profile" in GET mode to view profile.
    ## Update Profile 
        call "/accounts/profile" in PUT mode to update email and name.
    ## Delete Profile
        call "accounts/profile" in DELETE mode to delete user account

## Change password
    "/accounts/change-password" API endpoint and pass old password and new password in data and password.

## Forgot password
    "/accounts/forgot-password" API endpoint to forgot password and pass your email in it and you will get an email and an password change link. click on that link and change user's password.
