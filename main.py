from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        pass

class Phone(Field):
    def number_validation(self):
        return len(self.value) == 10 and self.value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    def add_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj.number_validation():
            self.phones.append(phone_obj)

    def remove_phone(self, phone_to_delete):
        phone_obj = Phone(phone_to_delete)
        if phone_obj in self.phones:
            self.phones.remove(phone_obj)

    def edit_phone(self, old_phone, new_phone):
        old_phone_obj = Phone(old_phone)
        new_phone_obj = Phone(new_phone)
        if old_phone_obj in self.phones:
            index = self.phones.index(old_phone_obj)
            self.phones[index] = new_phone_obj
        else:
            raise ValueError (f"Invalid phone number: {old_phone}")

    def find_phone(self, phone):
        phone_obj = Phone(phone)
        if phone_obj in self.phones:
            return phone_obj
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        if not self.data:
            return "AddressBook is empty."
        return "\n".join(f"{record}" for record in self.data.values())



