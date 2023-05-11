title = "Office Hour"
print(title)

message = "Office hour are from 9:00 am to 9:00 pm."
print(message)

timezones = {
    "Portland": {1: "closed", 2: "closed", 3: "closed", 4: "closed", 5: "closed", 
                 6: "closed", 7: "closed", 8: "open", 9: "closed", 10: "closed", 
                 11: "closed", 12: "closed"},
    "New York": {1: "closed", 2: "closed", 3: "open", 4: "closed", 5: "closed", 
                 6: "closed", 7: "closed", 8: "closed", 9: "closed", 10: "closed", 
                 11: "closed", 12: "closed"},
    "London":   {1: "closed", 2: "closed", 3: "closed", 4: "closed", 5: "open", 
                 6: "closed", 7: "closed", 8: "closed", 9: "closed", 10: "closed", 
                 11: "closed", 12: "closed"}
}

def checkBranch(city, timezone):
    status = timezones[city][timezone]
    print(f"The {city} branch is {status}")

checkBranch("Portland", 8)
checkBranch("New York", 3)
checkBranch("London", 5)
