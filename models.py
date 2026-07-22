{% extends 'base.html' %}
{% block title %}Edit Appliance - Smart Energy{% endblock %}
{% block content %}

<div class="row justify-content-center">
  <div class="col-md-7">
    <div class="card">
      <div class="card-header"><i class="fa-solid fa-pen"></i> Edit Appliance</div>
      <div class="card-body">
        <form method="POST">
          <div class="mb-3">
            <label class="form-label">Appliance Name</label>
            <input type="text" name="name" class="form-control" value="{{ appliance.name }}" required>
          </div>
          <div class="mb-3">
            <label class="form-label">Wattage (W)</label>
            <input type="number" step="0.1" name="wattage" class="form-control" value="{{ appliance.wattage }}" required>
          </div>
          <div class="mb-3">
            <label class="form-label">Hours Used per Day</label>
            <input type="number" step="0.1" min="0.1" max="24" name="hours" class="form-control" value="{{ appliance.hours }}" required>
          </div>
          <div class="mb-3">
            <label class="form-label">Quantity</label>
            <input type="number" min="1" name="quantity" class="form-control" value="{{ appliance.quantity }}" required>
          </div>

          <button type="submit" class="btn btn-primary"><i class="fa-solid fa-check"></i> Save Changes</button>
          <a href="{{ url_for('energy.appliances') }}" class="btn btn-outline-secondary">Cancel</a>
        </form>
      </div>
    </div>
  </div>
</div>

{% endblock %}
