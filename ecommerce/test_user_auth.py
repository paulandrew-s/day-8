from user_auth import UserAuth

auth = UserAuth()

def test_register_login():
    assert auth.register('user1', 'password1')
    assert auth.login('user1', 'password1')

def test_register_existing_user():
    assert not auth.register('admin', 'newpassword')
    
def test_login_wrong_password():
    assert auth.register('user2', 'password2')
    assert not auth.login('user2', 'wrongpassword')
    