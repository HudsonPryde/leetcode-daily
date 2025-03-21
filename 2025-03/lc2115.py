from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        sup = set(supplies)
        imp = set()
        rec = {r:ingredients[i] for i,r in enumerate(recipes)}

        def check(r: str, dep: set):
            if r in sup:
                return True
            if r in imp:
                return False
            if r not in rec:
                imp.add(r)
                return False
            if r in dep: return False
            dep.add(r)
            for ingredient in rec[r]:
                if ingredient == r or not check(ingredient, dep):
                    imp.add(r)
                    return False
            sup.add(r)
            return True
        
        res = []
        for r in recipes:
            if check(r, set()):
                res.append(r)
        return res

S = Solution()
r = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
i = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
s = ["wi","otr","wbjr","fzr","xgp"]
# r=["sandwich","bread"]
# i=[["bread","flour"],["sandwich","flour"]]
# s=["yeast","flour","meat"]
print(S.findAllRecipes(r,i,s))
