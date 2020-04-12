arv = {
    "<inteiro>":["<digito>","<digito><inteiro>"],
    "<digito>":["0","1","2","3","4","5","6","7","8","9"]
}
import re
inicio = ["<inteiro>"]
padrao = r'<[a-z]+>'
goal = ["4","5","2","0"]
def generatorTree(inicio):
    for _ in range(len(inicio)):
        last = inicio[0]
        try:
            f = (re.findall(padrao,last))[0]
            p = arv[f]
            inicio.pop(0)
            for v in p:
                s = last
                inicio.append(s.replace(f,v,1))
        except Exception:
            print(inicio[0])  
            pass      
    generatorTree(inicio)
print(generatorTree(inicio))