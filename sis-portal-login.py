import mechanicalsoup

# Create a browser object
browser = mechanicalsoup.StatefulBrowser()

# URL of the website
url = 'https://bitm.edu.in/parent-interaction-cell/'

# Get input from the user
username = input('Enter your USN: ')
birthday = input("Enter your date of birth (DD/MM/YYYY): ")

# Open the URL in the browser
browser.open(url)
print("Current URL:", browser.get_url())

# Find the login form by inspecting the HTML of the website
# Update the form selector accordingly
form = browser.select_form('form[id="your-form-id"]')

# Fill in the username
form.set_input({"username": username})

# Parse the birthday input
day, month, year = birthday.split('/')
months = {
    '01': 'January', '02': 'February', '03': 'March', '04': 'April',
    '05': 'May', '06': 'June', '07': 'July', '08': 'August',
    '09': 'September', '10': 'October', '11': 'November', '12': 'December'
}
month = months[month]

# Set the day, month, and year in the form
form.set_select({"dd": day})
form.set_select({"mm": month})
form.set_select({"yyyy": year})

# Uncomment the next line if you want to visualize the browser interaction
# browser.launch_browser()

# Submit the form
response = browser.submit_selected()

# Print the response text
print(response.text)
