
class Polynomial():
    """
    Compute the amount of water trapped, given the wall height sequence
    """
    def __init__(self, dic):
        """
        init the poly dict
        """
        # self.coef = list(dic.values()) 
        # self.ord = list(dic.keys())
        assert type(dic)==dict
        assert len(dic.keys())==len(dic.values())
        assert all(((type(k)==int) and (type(v)==int)) for k,v in dic.items())
        vals = list(dic.values())
        ks = list(dic.keys())
        for i in range(len(ks)):
            if vals[i]==0:
                del dic[ks[i]]
        self.polDict = dic
    def get_pol_list(self, l, reverse=True):
        """
        Get polynomial ordered list from dictionary
        -> [[order, coefficient],[order, coefficient]...] 
        """
        if (l != {}):
            divPolyList = [[a,b] for a,b in zip(list(l.keys()), list(l.values()))]
            divPolyList.sort(key=lambda l: l[0], reverse=reverse)
        else:
            divPolyList = []
        return divPolyList
    def __repr__(self):
        """print out reprs"""
        # print(self.polDict)
        pl = self.get_pol_list(self.polDict, reverse=False)
        ord = [j[0] for j in pl]
        coef = [j[1] for j in pl]
        res = ""
        for i in range(len(coef)):
            if (coef[i] != 0):
                if (ord[i]==0):
                    res += "{} + ".format(str(coef[i]))
                elif (ord[i]==1):
                    if (coef[i] == 1):
                        res += "{} + ".format("x")
                    # elif (coef[i] -= 1):
                    #     res += "{} {} + ".format(str(coef[i]), "x")
                    else:
                        res += "{} {} + ".format(str(coef[i]), "x")
                else:
                    if (coef[i] == 1):
                        res += "{}^{} + ".format("x", "({})".format(ord[i]))
                    else:
                        res += "{} {}^{} + ".format(str(coef[i]), "x", "({})".format(ord[i]))
        res = res[:-3]
        return res
    def __add__(self, other):
        """add two polys"""
        if (type(other)==Polynomial):
            allKeys = set(self.polDict.keys()).union(set(other.polDict.keys()))
            allKeys = list(allKeys)
            res = {}
            for j in allKeys:
                polDictVal = self.polDict.get(j, None)
                otherVal = other.polDict.get(j, None)
                if ((polDictVal!=None) and (otherVal!=None)):
                    if (polDictVal + otherVal != 0):
                        res[j] = polDictVal + otherVal
                elif ((polDictVal!=None) and (otherVal==None)):
                    res[j] = polDictVal
                elif ((polDictVal==None) and (otherVal!=None)):
                    res[j] = otherVal
        else:
            res = self.polDict
            res[0] = res[0] + other
        return Polynomial(res) 
    def __mul__(self, other):
        """left multiply"""
        res = {}
        if (type(other) != Polynomial):
            for k,v in self.polDict.items():
                res[k] = v * other
            return Polynomial(res)
        else:
            # TODO: Poly-by-Poly multiplications
            res = Polynomial({})
            for k,v in other.polDict.items():
                for kori, vori in self.polDict.items():
                    res = res + Polynomial({k+kori: v*vori})
            return res
    def __rmul__(self, other):
        """commutative right multiply"""
        return self.__mul__(other)
    def __sub__(self, other):
        """print out reprs"""
        # print("other")
        # print(other)
        # print("self")
        # print(self)
        return self.__add__(other * (-1))
    def __rsub__(self, other):
        """print out reprs"""
        return self.__sub__(other) * (-1)
    def subs(self, num):
        """substitution of value"""
        res = 0
        for k, v in self.polDict.items():
            res += v*((num)**k)
        return res
    def __eq__(self, other):
        """print out reprs"""
        if isinstance(other, self.__class__):
            return self.polDict == other.polDict
        else:
            if other != 0:
                return self.__eq__(Polynomial({0: other}))
            else:
                return self.polDict=={}
    def __ne__(self, other):
        """print out reprs"""
        return not self.__eq__(other)
    def is_empty(self):
        """check if empty"""
        return self.polDict == {}
    def __div__(self, divPoly):
        """print out reprs"""
        assert type(divPoly)==Polynomial
        res = Polynomial({})
        upPolDict = Polynomial(self.polDict)
        upPolList = self.get_pol_list(upPolDict.polDict)
        divPolyList = self.get_pol_list(divPoly.polDict)
        # TODO: poly-by-poly division (divisible case and not-implementable case)
        # polDictOrds = sorted(list(self.polDict.keys()), reverse=True)
        # print(upPolList, divPolyList)
        while (not upPolDict.is_empty()):
            if (upPolList[0][0] >= divPolyList[0][0]):
                currOrd = upPolList[0][0] - divPolyList[0][0]
                currCoeff = upPolList[0][1] // divPolyList[0][1]
                fac = divPoly * Polynomial({currOrd: currCoeff})
                # print("fac:")
                # print(fac)
                upPolDict = upPolDict - fac
                # print("upPolDict")
                # print(upPolDict)
                upPolList = self.get_pol_list(upPolDict.polDict)
                res = res + Polynomial({currOrd: currCoeff})
            else:
                raise NotImplementedError
        return res
    def __truediv__(self, divPoly):
        """print out reprs"""
        return self.__div__(divPoly)


# p=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
# q=Polynomial({0:8,1:2,2:8,4:4})
# repr(p)
# p*3 # integer multiply
# 3*p # multiplication is commutative!
# p+q # add two polynomials
# p*4 + 5 - 3*p - 1 # compose operations and add/subtract constants
# type(p-p) # zero requires special handling but is still a Polynomial
# p*q # polynomial by polynomial multiplication works as usual
# p.subs(10) # substitute in integers and evaluate
# (p-p) == 0
# p == q
# p=Polynomial({0:8,1:0,3:4}) # keys are powers, values are coefficients
# repr(p)
# p = Polynomial({2:1,0:-1})
# q = Polynomial({1:1,0:-1})
# p/q
# p  / Polynomial({1:1,0:-3}) # raises NotImplementedErrorp=Polynomial({0:8,1:2,3:4}) # keys are powers, values are coefficients
# q=Polynomial({0:8,1:2,2:8,4:4})
# repr(p)
# p*3 # integer multiply
# 3*p # multiplication is commutative!
# p+q # add two polynomials
# p*4 + 5 - 3*p - 1 # compose operations and add/subtract constants
# type(p-p) # zero requires special handling but is still a Polynomial
# p*q # polynomial by polynomial multiplication works as usual
# p.subs(10) # substitute in integers and evaluate
# (p-p) == 0
# p == q
# p=Polynomial({0:8,1:0,3:4}) # keys are powers, values are coefficients
# repr(p)
# p = Polynomial({2:1,0:-1})
# q = Polynomial({1:1,0:-1})
# p/q
# p  / Polynomial({1:1,0:-3}) # raises NotImplementedError





# # def main():
# #     t = (0, 5, 2, 1, 4, 7, 3, 6)
# #     print(next_permutation(t))
# #     return 0

# main()