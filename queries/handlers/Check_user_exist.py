from models.user import User

def handle(user_name: str,user_password: str):
    user=User()
    u = User.query.filter_by(name=user_name).first()
    user.set_password(user_password)
    # return {
    #     'user':u.to_dict(),
    #     'passwordSended': user.password,
    #     'realpassword' : u.password
    # }
    # for u in users:
    #     if User.check_password(u,password=user_password):
    #         if u.name == user_name:
    #             return {
    #             'success': True,
    #             'user': u.to_dict()
    #         }
    user.set_password(user_password)
    if u.password == user.password:
        return {
            'success': True,
            'user': u.to_dict()
        }
    return {
        'success': False,
        'message': 'Nieprawidłowa nazwa użytkownika lub hasło'
        # 'passuser': u.password,
        # 'passsended': user.password
    }


