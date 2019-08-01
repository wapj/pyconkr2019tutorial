import logging
logger = logging.getLogger(__name__)

# 빌링같은 데이터는 민감한 데이터라 오브젝트의 값을 읽을때마다 로그를 남겨야합니다. 
# 민감한 클래스의 변수에 접근할 때마다 로그를 남기도록 해봅시다. 

class BillingComponent(object):
    def __init__(self, user):
        self.user = user
    
    def __getattribute__(self, key):
        # 메서드 몸체에 self 로 변수에 접근을 하면 안됩니다.
        # 왜냐하면 변수에 접근할 때 __getattribute__ 를 다시 호출하게되어, 무한 루프에 빠지게 됩니다. 
        user = super().__getattribute__('user')
        try:
            if key != 'user':
                print(f"[DEBUG] user <{user}> try to GET key '{key}'")
            return super().__getattribute__(key)
        except AttributeError:
            logger.error(f"<{user}> try to get prohibited key : {key}")
            return None
    
    def __setattr__(self, key, val):
        if key != 'user':
            user = super().__getattribute__('user')
            print(f"[DEBUG] user <{user}> try to SET '{key}':'{val}'")
        super().__setattr__(key, val)
        
    def __getattr__(self, key):
        pass # __getattribute__ 와 어떻게 다를까요?
        
        
bill = BillingComponent('andy')
print(">>> ", bill.user)
print(">>> ", bill.password)
bill.reciept = '100원'
