phone_book = {
    "Alice": "555-1234",
    "Bob": "867-5309",
    "Charlie": "555-9012",
    "Dave": "555-3456",
    "Eve": "555-7890",
    "Frank": "555-2345",
    "Grace": "555-6789",
    "Harry": "555-0123",
    "Isabelle": "555-4567",
    "Jack": "555-8901"
}

def get_book (phone_book):
    name = (input("Enter a name into the phone book: "))
    if name in phone_book:
        phone_number= phone_book[name]
        print(f"The phone number for {name} is {phone_number}")
    else:
        print(f"This name does not exist in the phone book.")



get_book(phone_book)


