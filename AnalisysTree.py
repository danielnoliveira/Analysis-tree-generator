arv = {
    "<inteiro>":["<digito>","<digito><inteiro>"],
    "<digito>": ["4","5","2","0"]
}
#["0","1","2","3","4","5","6","7","8","9"]
import re
inicio = "<inteiro>"
padrao = r'<[a-z]+>'
goal = ["4","5","2","0"]
deep_boundary = len(goal)*2
def generatorTree(inicio,deep):
    if inicio==''.join(goal):
        return True
    if deep >= deep_boundary:
        return False 
    try:
        f = (re.findall(padrao,inicio))[0]
        p = arv[f]
        for v in p:
            s = inicio.replace(f,v,1)
            b = generatorTree(s,deep+1)
            if b:
                print(s)
                return True
    except Exception:
        pass      
print(generatorTree(inicio,0))