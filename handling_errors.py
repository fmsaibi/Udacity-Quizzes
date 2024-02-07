def party_planner(num_of_cookies: int, num_of_people:int):
    """"
    Prefrom Calculatetion on how many person can revise the cookies and what is the left over:

    input:
        num_of_cookies: Number of Cookies will be provided in the party
        num_of_people: Total Number of people atteding the party

    output:
        num_each: It will return the number if each cooikes for each person
        left_overs: It will retrun the reminder of cookies after cousiming equally by each person
    """
    left_overs = None
    num_each = None

    try:
        num_each:int = num_of_cookies // num_of_people
        left_overs:int = num_of_cookies % num_of_people
    except ZeroDivisionError:
        print("Invalid Number")

    return(num_each, left_overs)

# The main code block is below; do not edit this
LETS_PARTY = 'y'
while LETS_PARTY == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        MESSAGE = "\nLet's party! We'll have {} people attending, they'll \
                    each get to eat {} cookies, and we'll have {} left over."
        print(MESSAGE.format(people, cookies_each, leftovers))

    LETS_PARTY = input("\nWould you like to party more? (y or n) ")
