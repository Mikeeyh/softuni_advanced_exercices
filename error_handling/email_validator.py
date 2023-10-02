class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()

    if email == "End":
        break
    index = email.find('@')

    if len(email[:index]) < 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if not email.endswith(('.com', '.bg', '.org', '.net')):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

print("Email is valid")



