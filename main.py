from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
        pass

class Phone(Field):
    def __init__(self, value):
        if not self.number_validation(value):
            raise ValueError(f"Invalid phone number: {value}")
        super().__init__(value)

    def number_validation(self, value):
        return len(value) == 10 and value.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone_to_delete):
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone)
                return
        print(f"Phone {phone_to_delete} not found.")

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.add_phone(new_phone)
                return
            else:
                raise ValueError (f"Invalid phone number: {old_phone}")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
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

