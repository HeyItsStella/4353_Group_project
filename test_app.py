import unittest

from app import app

#to run the code coverage test excute commend below:
#   coverage run test_app.py
#   coverage report -m
#   coverage html

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert "<title>QuotEZ</title>" in response.get_data(as_text=True)
        
    def test_signup(self):
        response = self.client.get("/registration")
        assert response.status_code == 200
        assert "<title>Registration</title>" in response.get_data(as_text=True)
        
    def test_signup2(self):
        username = "whatthis"
        password = "What1234"
        response = self.client.post("/registration", data={"usrname": username, "psw": password, "psw-con": password})
        assert response.status_code == 302
    
    def test_signup3(self):
        username = "ADMIN"
        password = "Nani1234"
        response = self.client.post("/registration", data={"usrname": username, "psw": password, "psw-con": password})
        assert response.status_code == 302
        
    def test_signup4(self):
        username = ""
        password = ""
        response = self.client.post("/registration", data={"usrname": username, "psw": password, "psw-con": password})
        assert response.status_code == 302
    
    def test_login(self):
        username = "123459"
        password = "212341235413451345"
        response = self.client.get("/login")
        assert response.status_code == 200
        assert " <title>Login</title>" in  response.get_data(as_text=True)
        
    def test_login2(self):
        username = "test"
        password = "Abc12345"
        response = self.client.post("/login", data={"username": username, 'psw': password})
        assert response.status_code == 302

    def test_login3(self):
        username = "ADMIN"
        password = "Nani1234"
        response = self.client.post("/login", data={"username": username, 'psw': password})
        assert response.status_code == 302
        
    def test_land(self):
        response = self.client.post("/land")
        assert response.status_code == 302
        
    def test_land2(self):
        response = self.client.get("/land")
        assert response.status_code == 200
        
    def test_logout(self):
        response = self.client.post("/logout")
        assert response.status_code == 302
        
    def test_logout2(self):
        response = self.client.get("/logout")
        assert response.status_code == 200
        
    def test_profile(self):
        response = self.client.get("/profile")
        assert response.status_code == 302
    
    def test_profile1(self):
        with self.client.session_transaction() as sess:
            sess['user'] = 'test'

        response = self.client.get("/profile")
        assert response.status_code == 200
        assert "<title>User Profile</title>" in  response.get_data(as_text=True)
        
    def test_profile2(self):
        with self.client.session_transaction() as sess:
            sess['user'] = 'test'

        profile = {'name': '', 'address1': '', 'address2': '', 'city': '', 'zipcode': '', 'state': ''}
        response = self.client.post("/profile", data=profile)
        assert response.status_code == 200
        assert  "Zipcode is too short" in  response.get_data(as_text=True)
        
    def test_profile3(self):
        with self.client.session_transaction() as sess:
            sess['user'] = 'test'

        profile = {'name': '1234', 'address1': '1', 'address2': '2', 'city': 'city', 'zipcode': '12341234', 'state': 'al'}
        response = self.client.post("/profile", data=profile)
        assert response.status_code == 302
        
        

    def test_quote(self):
        response = self.client.get("/quote")
        assert response.status_code == 302
        
    def test_quote1(self):
        with self.client.session_transaction() as sess:
            sess['user'] = 'test'

        response = self.client.get("/quote")
        assert response.status_code == 200
        
    def test_quote_history(self):
        with self.client.session_transaction() as sess:
            sess['user'] = 'test'

        response = self.client.get("/quote_history")
        assert response.status_code == 200
        
    def test_quote_history1(self):
        response = self.client.get("/quote_history")
        assert response.status_code == 302

if __name__ == "__main__":
    unittest.main()
