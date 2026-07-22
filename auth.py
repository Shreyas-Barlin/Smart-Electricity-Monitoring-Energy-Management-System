from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Appliance

energy_bp = Blueprint('energy', __name__)

# Preset appliances the user can quickly pick from (name -> typical wattage)
PRESET_APPLIANCES = {
    'Fan': 75,
    'TV': 120,
    'AC': 1500,
    'Fridge': 200,
    'Washing Machine': 500,
    'Laptop': 65,
    'Computer': 250,
    'Motor': 750,
    'Cooler': 230,
    'Custom Appliance': 0,
}


@energy_bp.route('/appliances')
@login_required
def appliances():
    user_appliances = Appliance.query.filter_by(user_id=current_user.id)\
        .order_by(Appliance.created_at.desc()).all()
    return render_template('appliances.html', appliances=user_appliances)


@energy_bp.route('/appliances/add', methods=['GET', 'POST'])
@login_required
def add_appliance():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        custom_name = request.form.get('custom_name', '').strip()
        wattage = request.form.get('wattage', '')
        hours = request.form.get('hours', '')
        quantity = request.form.get('quantity', '1')

        if name == 'Custom Appliance' and custom_name:
            name = custom_name

        try:
            wattage = float(wattage)
            hours = float(hours)
            quantity = int(quantity)
        except (ValueError, TypeError):
            flash('Please enter valid numeric values.', 'danger')
            return redirect(url_for('energy.add_appliance'))

        if not name or wattage <= 0 or hours <= 0 or hours > 24 or quantity <= 0:
            flash('Please check your inputs (hours must be between 0-24).', 'danger')
            return redirect(url_for('energy.add_appliance'))

        appliance = Appliance(
            user_id=current_user.id,
            name=name,
            wattage=wattage,
            hours=hours,
            quantity=quantity
        )
        db.session.add(appliance)
        db.session.commit()
        flash(f'{name} added successfully!', 'success')
        return redirect(url_for('energy.appliances'))

    return render_template('add_appliance.html', presets=PRESET_APPLIANCES)


@energy_bp.route('/appliances/edit/<int:appliance_id>', methods=['GET', 'POST'])
@login_required
def edit_appliance(appliance_id):
    appliance = Appliance.query.filter_by(id=appliance_id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        try:
            appliance.name = request.form.get('name', '').strip() or appliance.name
            appliance.wattage = float(request.form.get('wattage'))
            appliance.hours = float(request.form.get('hours'))
            appliance.quantity = int(request.form.get('quantity'))
        except (ValueError, TypeError):
            flash('Please enter valid numeric values.', 'danger')
            return redirect(url_for('energy.edit_appliance', appliance_id=appliance_id))

        if appliance.hours <= 0 or appliance.hours > 24 or appliance.wattage <= 0 or appliance.quantity <= 0:
            flash('Please check your inputs (hours must be between 0-24).', 'danger')
            return redirect(url_for('energy.edit_appliance', appliance_id=appliance_id))

        db.session.commit()
        flash('Appliance updated successfully!', 'success')
        return redirect(url_for('energy.appliances'))

    return render_template('edit_appliance.html', appliance=appliance)


@energy_bp.route('/appliances/delete/<int:appliance_id>', methods=['POST'])
@login_required
def delete_appliance(appliance_id):
    appliance = Appliance.query.filter_by(id=appliance_id, user_id=current_user.id).first_or_404()
    db.session.delete(appliance)
    db.session.commit()
    flash('Appliance removed.', 'info')
    return redirect(url_for('energy.appliances'))
