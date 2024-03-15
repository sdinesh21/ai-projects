# Problem: Given two arrays, write a function to compute their intersection. Each element in the result must be unique, and you may return the result in any order.
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]


def numUniqueEmails(emails):
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        local = local.split('+')[0]  # Ignore everything after '+'
        local = local.replace('.', '')  # Remove periods
        unique_emails.add(local + '@' + domain)

    return len(unique_emails)

# Test the function
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))  # Output: 2