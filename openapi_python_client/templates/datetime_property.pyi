{% macro template(property, source) %}
{% if property.required %}
{{ property.python_name }} = datetime.fromisoformat({{ source }})
{% else %}
{{ property.python_name }} = None
if {{ source }} is not None:
    {{ property.python_name }} = datetime.fromisoformat(cast(str, {{ source }}))
{% endif %}
{% endmacro %}
