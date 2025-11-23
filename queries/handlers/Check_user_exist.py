from models.user import User

def handle(user_name: str,user_password: str):
    users = User.query.all()
    for u in users:
        if User.check_password(u,password=user_password):
            if u.name == user_name:
                return {
                'success': True,
                'user': u.to_dict()
            }
    
    return {
        'success': False,
        'message': 'Nieprawidłowa nazwa użytkownika lub hasło'
    }


