#contruct binary constraint class
class binaryConstraint:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
    
    def partof(self, x):
        return x == self.x1 or x == self.x2
    
    def otherX(self, x):
        if x == self.x1:
            return self.x2
        return self.x1
    
    
class NotEqualConstraint(binaryConstraint):
    
    def isSatisfied(self, value1, value2):
        if value1 == value2:
            return False
        return True

    def __repr__(self):
        return 'NotEqualConstraint (%s, %s)' % (str(self.x1), str(self.x2))     

class csp:
    
    def __init__(self, x, domain, binaryconstraints=[]):
        self.xDom = {}
        for i in range(0, len(x)):
            self.xDom[x[i]] = domain[i]
        self.binaryconstraints = binaryconstraints
    
    
#contruct assignment class
class Assignment:
    def __init__(self, csp):
        #create a disctionary for storing variable domains
        self.xDom = {}
        self.assignedVals = {}
        for x in csp.xDom:
            self.xDom[x] = csp.xDom[x]
            self.assignedVals[x] = None
            
    def isAssigned(self, x):
        return (self.assignedVals[x] != None)
    
    def completeAssignment(self):
        for x in self.assignedVals:
            if self.assignedVals[x] == None:
                return False
        
        return True 
    
    def returnSolution(self):
        if not self.completeAssignment():
            return None
        return self.assignedVals

        
def isConsistent(csp, assignment, x, val):
    for constraint in csp.binaryconstraints:
        if constraint.partof(x) and val == assignment.assignedVals[constraint.otherX(x)]:
            return False
    return True        
            
            
def backtracking(csp, assignment, varOrdering, valOrdering):
    if assignment.completeAssignment():
        return assignment
    var = varOrdering(csp, assignment)
    # print(var)
    # if var == None:
    #     return None
    
    possVal = valOrdering(csp, assignment, var)
    for val in possVal:
        if isConsistent(csp, assignment, var, val):
            assignment.assignedVals[var] = val
            print(assignment.assignedVals)
            nextvar = backtracking(csp, assignment, varOrdering, valOrdering)
            return nextvar  
            assignment.assignedVals[var]=None
            
    return None

def varOrder(csp, assignment):
    for var in csp.xDom:
        if not assignment.isAssigned(var):
            return var
        

def valOrder(csp, assignment, x):
    return list(csp.xDom[x])


def solveCSP(csp, orderValuesMethod, selectVariableMethod):
    assignment = Assignment(csp)
    assignment = backtracking(csp, assignment, selectVariableMethod, orderValuesMethod)
    
    return assignment.returnSolution()
    
       
    
def forwardChecking():