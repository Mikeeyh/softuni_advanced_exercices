class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = ['.com', '.bg', '.org', '.net']
while True:
    email = input()

    if email == "End":
        break

    if len(email.split('@')[0]) < EMAIL_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    domain = '.' + email.split('.')[-1]
    if domain not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

# OR --------------------------------------------------------------------

while True:
    email = input()

    if email == "End":
        break
    index = email.find('@')

    if len(email[:index]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if not email.endswith(('.com', '.bg', '.org', '.net')):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")



