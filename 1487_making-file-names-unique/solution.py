from typing import List

from collections import defaultdict


class Solution:
    """
    def get_base_and_suffix(name: str):
        if len(name) < 4:
            return name, 0            

        if name[-1] != ")":
            return name, 0

        left = len(name) - 2
        while left > 0:
            if name[left] == "(":
                if name[left + 1] in ["0", ")"]:
                    return name, 0
                
                else:
                    return name[:left], int(name[left + 1:-1])

            char_as_int = ord(name[left]) - ord('0')
            if char_as_int < 0 or char_as_int > 9:
                return name, 0

            left -= 1
        
        return name, 0
        

    def getFolderNames(self, names: List[str]) -> List[str]:
        name_suffixes = defaultdict(lambda: set())

        folder_names = []
        for name in names:
            name, suffix = Solution.get_base_and_suffix(name)

            if suffix in name_suffixes[name]:
                for last_suffix in range(len(name_suffixes[name]) + 1):
                    if last_suffix not in name_suffixes[name]:
                        break

                suffix = last_suffix

            name_suffixes[name].add(suffix)
            if suffix == 0:
                folder_names.append(f"{name}")
            else:
                folder_names.append(f"{name}({suffix})")

        return folder_names
    """


    def getFolderNames(self, names: List[str]) -> List[str]:
        folder_names = []
        folder_names_set = set()

        for name in names:
            if name not in folder_names_set:
                folder_names.append(name)
                folder_names_set.add(name)

            else:
                suffix_index = 1
                new_name = f"{name}({suffix_index})"
                while new_name in folder_names_set:
                    suffix_index += 1
                    new_name = f"{name}({suffix_index})"

                folder_names.append(new_name)
                folder_names_set.add(new_name)

        return folder_names

            
if __name__ == "__main__":
    assert Solution().getFolderNames(["pes","fifa","gta","pes(2019)"]) == ["pes","fifa","gta","pes(2019)"]
    assert Solution().getFolderNames(["gta","gta(1)","gta","avalon"]) == ["gta","gta(1)","gta(2)","avalon"]
    assert Solution().getFolderNames(["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]) == ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]

    assert Solution().getFolderNames(["kaido","kaido(1)","kaido","kaido(1)"]) == ["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
