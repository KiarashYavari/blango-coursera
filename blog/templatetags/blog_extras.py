from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()

@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, user_model):
    return ""

  if author.first_name and author.last_name:
    name = f"{author.first_name} {author.last_name}"
  else:
    name = f"{author.username}"

  if author.email:
    email = author.email
    prefix = format_html(f'<a href="mailto:{email}">')
    suffix = format_html("</a>")
  else:
    prefix = ""
    sufix = ""
  if current_user == author:
    return format_html("<strong>me</strong>")

  else:
    return format_html('{}{}{}', prefix, name, suffix)
  

@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)


@register.simple_tag
def endrow():
  return format_html('</div>')  
