from .init_db import db


class Invite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    user = db.relationship('User', primaryjoin='Invite.user_id == User.id')
    team = db.relationship('Team', primaryjoin='Invite.team_id == Team.id')
