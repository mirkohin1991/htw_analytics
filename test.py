import datetime
import json
a = 1 + 2
print(a)
if a == 3:
    print(datetime.datetime.now())

# LOCAL CODING brand new new new1113333
# dev branch
# merge done

#########
# Here we have so class coding
#########
class newClass:
    def method(self):
        return 'Test'


a = newClass
print(a.method(a)



########
# Working with the JSON module.
########
object = """{ "Name" : "Mirko", "Hobbies": ["Sport", "Lesen"], "Alter": 10 }"""
encoded_obj = json.dumps(object)
print("Encoded Object", encoded_obj)
# Formatting of the JSON. Indent = Spaces
print("Formatted object", json.dumps(object, indent= 4))
decoded_obj = json.loads(encoded_obj)
print("Decoded Object", decoded_obj)
loaded_obj = json.loads(object)
print("Loaded Object", loaded_obj)










