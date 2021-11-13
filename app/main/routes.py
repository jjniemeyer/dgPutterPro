from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import current_user, login_required
from app import db
from app.main.forms import EditGoalForm, DrillForm
from app.models import User, Drill
from app.main import bp
from sqlalchemy import text




@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = DrillForm()
    if form.validate_on_submit():
        drill = Drill(putt_distance=form.putt_distance.data, number_attempts=form.number_attempts.data,
                      number_putts_made=form.number_putts_made.data, user=current_user)
        db.session.add(drill)
        db.session.commit()
        flash('You drill has been recorded!')
        return redirect(url_for('main.index'))
    drills = current_user.drills.all()
    return render_template('index.html', title='Home', form=form, drills=drills)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    drills = user.drills.order_by(Drill.timestamp.desc()).paginate(page, current_app.config['DRILLS_PER_PAGE'], False)
    next_url = url_for('main.user', username=user.username, page=drills.next_num) \
        if drills.has_next else None
    prev_url = url_for('main.user', username=user.username, page=drills.prev_num) \
        if drills.has_prev else None
    return render_template('user.html', user=user, drills=drills.items, next_url=next_url, prev_url=prev_url)

@bp.route('/user/<username>/stats')
@login_required
def stats(username):
    user = User.query.filter_by(username=username).first_or_404()
    # there must be a way to do this with the ORM but raw sql is working for now
    # summary is a tuple not a query object
    raw_sql = text("""
        SELECT Drill.putt_distance, SUM(Drill.number_putts_made) as putts_made, 
        SUM(Drill.number_attempts) as attempted FROM User Join Drill ON User.id=Drill.user_id 
        WHERE User.username=='{}' GROUP BY Drill.putt_distance ORDER BY Drill.putt_distance
        """.format(user.username))
    summary = db.engine.execute(raw_sql)
    return render_template('stats.html', user=user, summary=summary)

@bp.route('/edit_goal', methods=['GET', 'POST'])
@login_required
def edit_goal():
    form = EditGoalForm()
    if form.validate_on_submit():
        current_user.current_goal = form.current_goal.data
        db.session.commit()
        flash("Your changes have been saved.")
        return redirect(url_for('main.edit_goal'))
    elif request.method == 'GET':
        form.current_goal.data = current_user.current_goal
    return render_template('edit_goal.html', title='Edit Goal', form=form)


