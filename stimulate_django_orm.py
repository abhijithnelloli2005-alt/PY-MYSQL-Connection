import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="root",database="DjangoORM")
cur=conn.cursor()
# cur.execute("CREATE DATABASE DjangoORM")
# print("database created")

# cur.execute('''create table employee(id int primary key auto_increment,
# name varchar(20),
# designation varchar(30),
# salary decimal(10,2)
# )''')
# print("table created")


"""
Django ORM- 
CRUD
employees list
----------------
select  from employee
ORM - Employee.objects.all()

employee detail
---------------
select  from employee where id=1
ORM - Employee.objects.get(id=1)

create employee
----------------
insert into employee values(val1,)
ORM - Employee.objects.create(id=1,name="abc")

filter employees
-----------------
select * from employee where designation="HR"
ORM - Employee.objects.filter(designation="HR")

Update employee
----------------
update employee set salary=100000 where id=1
ORM - employee.save()

delete employee
----------------
delete from employee where id=1
ORM - employee.delete()
"""
class Employee:
    def create(self,*args,**kwargs):
        cols=""
        placeholder=""
        for cols in kwargs.keys():
            if cols!="":
                cols+=","
                placeholder+=','
            cols+=cols
            placeholder+="%s"
        values=tuple(kwargs.values())
        query=f"insert into employee({cols}) values({placeholder})"
        cur.execute(query,values)
        conn.commit()


    def list(self,*args,**kwargs):
        cur.execute("SELECT * FROM employee")
        # for emp in cur:
        #     print(emp)
        print(cur.fetchall())

    def retrive(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee WHERE {key}={kwargs.get(key)}")
            print(cur.fetchall())
    def update(self,*args,**kwargs):
        print(args,kwargs)
        for key in kwargs:
            cur.execute(f"UPDATE employee SET {key}='{kwargs.get(key)}' WHERE id={args[0]}")
            conn.commit()
    def delete(self,*args,**kwargs):
        cur.execute(f"DELETE FROM employee WHERE id={args[0]}")
        conn.commit
    def filter(self,*args,**kwargs):
        for key in kwargs:
            cur.execute(f"SELECT * FROM employee WHERE {key}='{kwargs.get(key)}'")
            print(cur.fetchall())


employee=Employee()

while True:
    choice=int(input("1.create employee\n2.list employee\n3.retrive employee\n4.update employee\n5.delete employee\n6.exit"))
    if choice==1:
        name=input("enter emloyee name")
        desig=input("enter designation")
        salary=float(input("enter salary"))
        employee.create(name=name,designation=desig,salary=salary)
    elif choice==2:
        employee.list()
    elif choice==3:
        id=int(input("enter employee id"))
        employee.retrive(id=id)
    elif choice==4:
        id=int(input("enter id of employee"))
        print("update:")
        print("1.name")
        print("2.designation")
        print("3.salary")
        choice=int(input("enter the choice"))
        if choice==1:
            name=input("enter the name")
            employee.update(id,name=name)
        elif choice==2:
            desig=input("enter new designation")
            employee.update(id,designation=desig)
        elif choice==3:
            salary=float(input("enter new salary"))
            employee.update(id,salary=salary)
        else:
            print("invalid choice")
    elif choice==5:
        id=int(input("enter id"))
        employee.delete(id)
    elif choice==6:
        print("filter options")
        print("filter by name")
        print("filter by designation")
        print("filter by salary")
        choice=int(input("enter choice"))
        if choice==1:
            name=input("enter name")
            employee.filter(name=name)
        elif choice==2:
            desig=input("enter designation")
            employee.filter(designation=desig)
        elif choice==3:
            salary=float(input("enter salary"))
            employee.filter(salary=salary)
    elif choice==7:
        break
    else:
        print("invalid choice")
        

conn.close()


