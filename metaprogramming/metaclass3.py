# type 함수로 타입검사.
# instance 를 넣으면 Class 를 알려준다.
# 아래는 신기하게도 다 type 이다.
# 즉 int, str, set, tuple 는 type의 인스턴스라는 얘기다.
# type 은 클래스를 만드는 클래스 : 즉 메타 클래스이다.
print(type(int))
print(type(str))
print(type(list))
print(type(set))
print(type(tuple))
print(type(type))  # type의 type도 type 이다...

# 얘도 type 이다.
print(type(Klass))

# 실행을 하면 Klass 가 나온다.
print(type(Klass()))

# 값
print(type(1))
print(type("1"))
