class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        count = 0
        email_set = set()
        for email in emails:
            name_list = email.split('@')
            local_name = name_list[0]
            domain_name = name_list[1]
            local_name = local_name.split('+')[0]
            local_name = ''.join(local_name.split('.'))
            new_email = local_name + '@' + domain_name
            email_set.add(new_email)
        return len(email_set)
