class oper:
    oper = ''
    func = ''

    
    def __init__(self,oper):
        self.oper = oper.strip()

    def opers(self,num1,num2):
        switcher = {
            "+":"add",
            "-":"substract",
            "*":"multiply",
            "/":"divide"
        }
        func = switcher.get(self.oper)
        pass

    def add(self,num1,num2):
        return num1+num2

    def subtract(self,num1,num2):
        return num1-num2
    
    def multiply(self,num1,num2):
        return num1*num2

    def divide(self,num1,num2):
        return num1/num2
    

    

    