
# from akaraike import PasswordGenerator
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string, get_template



def send_email(receiver, subject, template_name, context, sender):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, to=receiver)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()


# def get_hash():
#     pg = PasswordGenerator()
#     pg.set_charset_length(24)
#     pg.set_charset_types(['numbers', 'lowers', 'uppers'])
#     return pg.generate_password()
