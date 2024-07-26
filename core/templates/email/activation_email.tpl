{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{tokens}}
{% endblock %}