{% extends 'base.html' %}
{% block title %}Add Appliance - Smart Energy{% endblock %}
{% block content %}

<div class="row justify-content-center">
  <div class="col-md-7">
    <div class="card">
      <div class="card-header"><i class="fa-solid fa-plus"></i> Add Appliance</div>
      <div class="card-body">
        <form method="POST">
          <div class="mb-3">
            <label class="form-label">Appliance</label>
            <select name="name" id="applianceSelect" class="form-select" required onchange="handlePresetChange()">
              {% for preset_name, watt in presets.items() %}
              <option value="{{ preset_name }}" data-watt="{{ watt }}">{{ preset_name }}</option>
              {% endfor %}
            </select>
          </div>

          <div class="mb-3" id="customNameField" style="display:none;">
            <label class="form-label">Custom Appliance Name</label>
            <input type="text" name="custom_name" class="form-control" placeholder="e.g. Water Heater">
          </div>

          <div class="mb-3">
            <label class="form-label">Wattage (W)</label>
            <input type="number" step="0.1" name="wattage" id="wattageInput" class="form-control" required>
          </div>

          <div class="mb-3">
            <label class="form-label">Hours Used per Day</label>
            <input type="number" step="0.1" min="0.1" max="24" name="hours" class="form-control" required>
          </div>

          <div class="mb-3">
            <label class="form-label">Quantity</label>
            <input type="number" min="1" name="quantity" value="1" class="form-control" required>
          </div>

          <button type="submit" class="btn btn-primary"><i class="fa-solid fa-check"></i> Add Appliance</button>
          <a href="{{ url_for('energy.appliances') }}" class="btn btn-outline-secondary">Cancel</a>
        </form>
      </div>
    </div>
  </div>
</div>

{% endblock %}

{% block scripts %}
<script>
  function handlePresetChange() {
    const select = document.getElementById('applianceSelect');
    const selected = select.options[select.selectedIndex];
    const watt = selected.getAttribute('data-watt');
    const wattageInput = document.getElementById('wattageInput');
    const customField = document.getElementById('customNameField');

    if (selected.value === 'Custom Appliance') {
      customField.style.display = 'block';
      wattageInput.value = '';
    } else {
      customField.style.display = 'none';
      wattageInput.value = watt;
    }
  }
  document.addEventListener('DOMContentLoaded', handlePresetChange);
</script>
{% endblock %}
