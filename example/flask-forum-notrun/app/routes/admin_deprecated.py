from flask import Blueprint, render_template
from flask_login import login_required
from ..auth.decorators import admin_required

admin_bp = Blueprint('admin', __name__)

@admin_bp.before_request
@login_required
@admin_required
def require_admin():
    pass

@admin_bp.route('/dashboard')
def dashboard():
    return render_template('admin/dashboard.html')