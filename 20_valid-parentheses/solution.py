class Solution:
    def isValid(self, s: str) -> bool:
        open_parens = []

        for char in s:
            if char in ["(", "{", "["]:
                open_parens.append(char)

            else:
                if len(open_parens) <= 0:
                    return False

                open_paren = open_parens.pop()
                
                if (
                    (open_paren == "(" and char != ")") or
                    (open_paren == "{" and char != "}") or
                    (open_paren == "[" and char != "]")
                ):
                    return False

        if len(open_parens) > 0:
            return False

        return True
