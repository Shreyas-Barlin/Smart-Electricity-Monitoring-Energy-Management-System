{% extends 'base.html' %}
{% block title %}Reports - Smart Energy{% endblock %}
{% block content %}

<div class="d-flex justify-content-between align-items-center mb-3 flex-wrap gap-2">
  <h4><i class="fa-solid fa-file-invoice"></i> Energy Reports</h4>
  <form action="{{ url_for('bill.generate_report') }}" method="POST">
    <button type="submit" class="btn btn-primary btn-sm"><i class="fa-solid fa-camera"></i> Snapshot Today's Usage</button>
  </form>
</div>

<div class="card mb-3">
  <div class="card-body d-flex justify-content-between align-items-center flex-wrap gap-2">
    <div class="btn-group">
      <a href="{{ url_for('bill.reports', period='daily') }}" class="btn btn-outline-primary {{ 'active' if period == 'daily' }}">Daily</a>
      <a href="{{ url_for('bill.reports', period='weekly') }}" class="btn btn-outline-primary {{ 'active' if period == 'weekly' }}">Weekly</a>
      <a href="{{ url_for('bill.reports', period='monthly') }}" class="btn btn-outline-primary {{ 'active' if period == 'monthly' }}">Monthly</a>
    </div>
    <div>
      <a href="{{ url_for('bill.export_csv') }}" class="btn btn-outline-success btn-sm"><i class="fa-solid fa-file-csv"></i> Export CSV</a>
      <a href="{{ url_for('bill.export_pdf') }}" class="btn btn-outline-danger btn-sm"><i class="fa-solid fa-file-pdf"></i> Export PDF</a>
    </div>
  </div>
</div>

<div class="row g-3 mb-3">
  <div class="col-md-6">
    <div class="card stat-card text-white bg-primary">
      <div class="card-body">
        <div class="small">Total Energy ({{ period }})</div>
        <div class="fs-4 fw-bold">{{ total_energy }} kWh</div>
      </div>
    </div>
  </div>
  <div class="col-md-6">
    <div class="card stat-card text-white bg-success">
      <div class="card-body">
        <div class="small">Total Bill ({{ period }})</div>
        <div class="fs-4 fw-bold">₹{{ total_bill }}</div>
      </div>
    </div>
  </div>
</div>

<div class="card">
  <div class="card-body">
    {% if reports %}
    <div class="table-responsive">
      <table class="table table-hover">
        <thead>
          <tr><th>Date</th><th>Energy Used (kWh)</th><th>Bill (₹)</th></tr>
        </thead>
        <tbody>
          {% for r in reports %}
          <tr>
            <td>{{ r.date.strftime('%d %b %Y') }}</td>
            <td>{{ r.energy_used }}</td>
            <td>₹{{ r.bill }}</td>
          </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    {% else %}
    <p class="text-muted mb-0">No reports yet for this period. Click "Snapshot Today's Usage" to record one.</p>
    {% endif %}
  </div>
</div>

{% endblock %}
