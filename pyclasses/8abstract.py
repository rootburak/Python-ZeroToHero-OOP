from abc import ABC,abstractmethod

class BaseOrm(ABC):
    @abstractmethod #dunder method
    def save(self, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class DjangoOrm(BaseOrm):
    def save(self, data):
        print(f"Saving data {data} to the Django database")
    
    def delete(self, id):
        print(f"Deleting data with id {id} from the Django database")

class SqlOrm(BaseOrm):
    def save(self, data):
        print(f"Saving data {data} to the SQL database")
    
    def delete(self, id):
        print(f"Deleting data with id {id} from the SQL database")

user1name = "burak"
user1id = 1

user2name = "doruk"
user2id = 2

main_orm = DjangoOrm()

main_orm.save(user1name)
main_orm.save(user2name)

# easy way to change the db or orm
main_orm = SqlOrm()
main_orm.save(user2name)
main_orm.save(user2id)

