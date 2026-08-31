class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()

        for s in emails:
            local , domain = s.split("@")
            local = local.replace("." , "")
            local = local.split("+")[0]
            unique.add((local , domain))
        return len(unique)



        
        



        