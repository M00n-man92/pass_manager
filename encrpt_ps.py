import random
class Encript:
    def start():    
        h = []
        h.extend("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

        n = []
        n.extend("1234567890")

        k = []
        k.extend("!@#$%^&*()_+{[]'|?><.,/}")

        a = random.randrange(8,10)
        
        d = random.randrange(4,6)
        
        v = random.randrange(3,5)
        
        m = ["a", "d", "v"]
        o = []


        l = a+d+v
        
        for helo in range(0, l):
            if len(m) != 0:
                p = random.choice(m)
                if p == "a":
                    if a > 0:
                        o.append(random.choice(h))
                        a -= 1
                        if a == 0:
                            m.remove("a")
                elif p == "d":
                    if d > 0:
                        o.append(random.choice(n))
                        d -= 1
                        if d == 0:
                            m.remove("d")
                elif p == "v":
                    if v > 0:
                        o.append(random.choice(k))
                        v -= 1
                        if v == 0:
                            m.remove("v")
        password=""
        for lol in range(0,len(o)):
            password+=o[lol]
        
        return password 

