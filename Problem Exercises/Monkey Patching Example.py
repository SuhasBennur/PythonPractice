#Monkey Patching Example
class A:
    def method(self): return "original"
def new_method(self): return "patched"
A.method=new_method
print(A().method())
