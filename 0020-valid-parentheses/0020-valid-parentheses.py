# # class Solution:
# #     def isValid(self, s: str) -> bool:
# #         while "()" in s or "[]" in s or "{}" in s:
# #             s.replace ("()","")
# #             s.replace ("{}","")
# #             s.replace ("[]","")
# #         return s== ""
# class Solution:
#     def isValid(self, s: str) -> bool:
#         while "()" in s or "[]" in s or "{}" in s:
#             s = s.replace("()", "")
#             s = s.replace("[]", "")
#             s = s.replace("{}", "")

#         return s == ""
class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        if n%2==1:
            return False
        st=[]
        for ch in list(s):
            if ch=='(' or ch=='{' or ch=='[':
                st.append(ch)
            else:
                if len(st)==0:
                    return False
                top=st.pop()
                if ch==')' and top!='(':
                    return False
                elif ch=='}' and top!='{':
                    return False
                elif ch==']' and top!='[':
                    return False
        return len(st)==0