{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.name }}
{% endblock %}

{% block html %}
This is an <strong>html</strong> message.
{{refresh}}
{% endblock %}