import json, requests


class TKR5SimRequestAPI():
    def __init__(self,ulke,token,uygulama,operator):
        self.BuyHost = "https://5sim.net/v1/user/buy/activation/"
        self.CancelHost = "https://5sim.net/v1/user/cancel/"
        self.FINISHost = "https://5sim.net/v1/user/finish/"
        self.CHECKHost = "https://5sim.net/v1/user/check/"
        self.ProfileHost = "https://5sim.net/v1/user/profile"
        self.BANHost = "https://5sim.net/v1/user/ban/"
        self.country = ulke
        self.operator = operator
        self.product = uygulama
        self.headers = {
          'Authorization': f'Bearer {token}','Accept': 'application/json',
        }
        self.session = requests.Session()

    def GoodPrint(self, djson):
        print(json.dumps(djson, indent=4, sort_keys=True))
        
  
    def B(self):
        headers = self.headers
        r = self.session.get(self.BuyHost + self.country + '/' + self.operator + '/' + self.product,headers=headers).json()
        return r
      
    def C(self,ID):
        headers = self.headers
        r = self.session.get(self.CancelHost + str(ID),headers=headers).json()
        return r
      
    def F(self,ID):
        headers = self.headers
        r = self.session.get(self.FINISHost + str(ID),headers=headers).json()
        return r
      
    def R(self,ID):
        headers = self.headers
        r = self.session.get(self.CHECKHost + str(ID),headers=headers).json()
        return r
      
    def P(self):
        headers = self.headers
        r = self.session.get(self.ProfileHost,headers=headers).json()
        return r
      
    def D(self,ID):
        headers = self.headers
        r = self.session.get(self.BANHost + str(ID),headers=headers).json()
        return r
