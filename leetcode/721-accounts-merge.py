# https://leetcode.com/problems/accounts-merge/
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(email):
            if parents[email] != email:
                parents[email] = find(parents[email])
            return parents[email]
        
        def union(email_1, email_2):
            root_1 = find(email_1)
            root_2 = find(email_2)
            parents[root_1] = root_2
        
        parents = {}
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                
                # Make set if doesn't exist.
                if email not in parents:
                    parents[email] = email
                
                union(first_email, email)
        
        root_to_emails = defaultdict(list)
        for email in parents:
            root = find(email)
            root_to_emails[root].append(email)
            
        for names in root_to_emails.values():
            names.sort()
        
        return [[email_to_name[root]] + emails for root, emails in root_to_emails.items()]
