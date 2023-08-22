# employee={"id":100,"name":"vijay","deparmnt":"HR","salary":3000}
# def get_name(st):
#     return st.get("name")
# print(get_name(employee))
# get_salary=lambda emp:emp.get("salary")
# print(get_salary(employee))
# get_name=lambda emp:emp.get("name")
# print(get_name(employee))

employee={"id":100,"name":"vijay","deparmnt":"HR","salary":3000}
(get_salary)=lambda emp: emp.get("salary")
print(get_salary(employee))
get_id=lambda emp:emp.get("id")
print(get_id(employee))