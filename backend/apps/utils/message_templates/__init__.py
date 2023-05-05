from django.conf import settings

class EmailTemplate:
    @staticmethod
    def password_reset_email(token):
        message = f"""
            <p style="color: #fff">Kindly click the link below to continue in resetting your account password.</p>
            <p style="color: #fff"><a href="{settings.PASSWORD_RESET_PAGE}/{token}">{settings.PASSWORD_RESET_PAGE}/{token}</a></p>
            <p style="color: #fff"><b>The above link will expire in {DateTime.convert_seconds_to_hr_min(settings.PASSWORD_RESET_TOKEN_EXPIRATION_SECS)}.</b></p>
            """
        return message