{% extends 'base.html' %}
{% block title %}{% if object %}Editar{% else %}Nova{% endif %} Categoria{% endblock %}
{% block content %}
<div class="row justify-content-center">
    <div class="col-md-8">
        <div class="card shadow">
            <div class="card-header bg-dark text-white">
                <h4 class="mb-0">{% if object %}Editar{% else %}Nova{% endif %} Categoria</h4>
            </div>
            <div class="card-body">
                <form method="post">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <div class="d-flex justify-content-end gap-2">
                        <a href="{% url 'categoria_list' %}" class="btn btn-secondary">Cancelar</a>
                        <button type="submit" class="btn btn-primary">Salvar Categoria</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</div>
{% endblock %}
