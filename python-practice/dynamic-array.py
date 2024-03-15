attendees = []  # Dynamic array to hold the list of attendees

# Adding attendees as they RSVP
attendees.append('Alice')
attendees.append('Bob')
attendees.append('Charlie')

# Bob cancels his RSVP
attendees.remove('Bob')

# Print the final list of attendees
print(attendees)  # Output: ['Alice', 'Charlie']