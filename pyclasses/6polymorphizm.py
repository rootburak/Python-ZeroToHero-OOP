class DbAction:
    def save(self, name):
        raise NotImplementedError("Method save is required")
    
    def delete(self, id):
        raise NotImplementedError("Method delete is required")
    
    def update(self, id, new_name):
        raise NotImplementedError("Method update is required")
    
    def get_all(self):
        raise NotImplementedError("Method get_all is required")

class DjangoOrm(DbAction):
    def save(self, name):
        print(f"Saving {name} to the database using Django ORM")
        # Implementation for saving data using Django ORM
    
    def delete(self, id):
        print(f"Deleting {id} from the database using Django ORM")
        # Implementation for deleting data using Django ORM
    
    def update(self, id, new_name):
        print(f"Updating {id} to {new_name} in the database using Django ORM")
        # Implementation for updating data using Django ORM
    
    def get_all(self):
        print("Retrieving all records from the database using Django ORM")
        # Implementation for retrieving all records using Django ORM

class Orm(DbAction):
    def save(self, name):
        print(f"Saving {name} to the database using Another ORM")
        # Implementation for saving data using Another ORM
    
    def delete(self, id):
        print(f"Deleting {id} from the database using Another ORM")
        # Implementation for deleting data using Another ORM
    
    def update(self, id, new_name):
        print(f"Updating {id} to {new_name} in the database using Another ORM")
        # Implementation for updating data using Another ORM
    
    def get_all(self):
        print("Retrieving all records from the database using Another ORM")
        # Implementation for retrieving all records using Another ORM

user1Name = "burak"
user1Id = 1

user2Name = "emre"
user2Id = 2

main_orm = DjangoOrm()  # Main ORM instance using Django ORM
seccond_orm = Orm()     # Secondary ORM instance using Another ORM

# We can easily switch to a new ORM with just one line of code
# main_orm = NewOrm() would allow us to change the ORM without modifying other parts of the code
main_orm.save(user1Name)  # Saving user1Name using the main ORM
seccond_orm.save(user1Name)  # Saving user1Name using the secondary ORM




