import re

text = "My number is 415-555-1234"

pattern = r"(\d{3})-(\d{3})-(\d{4})"
match = re.search(pattern, text)

if match:
    print("Full:", match.group(0))
    print("Area code:", match.group(1))
    print("Middle:", match.group(2))
    print("Last part:", match.group(3))

import re

text = "Today's date is 05/11/2025 and yesterday was 04/11/2025."

pattern = r"\d{2}/\d{2}/\d{4}"

matches = re.findall(pattern, text)
print(matches)





text = "Event on 05/11/2025"
pattern = r"(\d{2})/(\d{2})/(\d{4})"

match = re.search(pattern, text)
if match:
    day, month, year = match.groups()
    print("Day:", day)
    print("Month:", month)
    print("Year:", year)

    
