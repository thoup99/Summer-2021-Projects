##Creates logic gates needed to operate with binary numbers
class Logic_gates():
    def __init__(self):
        pass

    def lg_or(self, A, B): #Returns 1 if either inputs are 1
        if (A or B == 1):
            return(1)
        else:
            return(0)

    def lg_and(self, A, B): #Returns 1 if both inputs are 1
        if (A and B == 1):
            return(1)
        else:
            return(0)

    def lg_not(self, A): #Returns 1 if the input is 0 and Returns 0 if the input is 1
        return(1 if A == 0 else 0)

    def lg_nor(self, A, B): #Returns 1 if both inputs are 0
        return(self.lg_not(self.lg_or(A, B)))

    def lg_xor(self, A, B): #Returns 1 if only one of the inputs is 1 else it Returns 0
        if (A or B == 1):
            if (not A == B):
                return(1)
            else:
                return(0)
        return(0)

    def half_adder(self, A, B):
        sum = self.lg_xor(A, B)
        carry = self.lg_and(A, B)
        return(sum, carry)

    def full_adder(self, A, B, C): #Full binary adder that takes the inputs and the carry and returns (sum, new carry)
        xor1 = self.lg_xor(A, B)
        sum = self.lg_xor(xor1, C)
        carry = self.lg_or(self.lg_and(xor1, C), self.lg_and(A, B))
        return(sum, carry)

    def half_subtractor(self, A, B):
        difference = self.lg_xor(A, B)
        borrow = self.lg_and(self.lg_not(A), B) 
        return(difference, borrow)

    def full_subtractor(self, A, B, C=0): #C stands for borrow
        hs1 = self.half_subtractor(A, B)
        hs2 = self.half_subtractor(hs1[0], C)
        diff = hs2[0]
        borrow = self.lg_or(hs1[1], hs2[1])
        return(diff, borrow)

##Uses the logic gates we made to do the desired operation
class Binary_Num(Logic_gates):
    def __init__(self, binary_num):
        self.num = str(binary_num)
        super().__init__()

    def To_binary(self): #converts a regular number to binary
        A = self.num
        is_neg = False
        if (str(A)[0] == "-"):
            A = A[1:]
            is_neg = True
        A = bin(int(A))[2:]
        if (is_neg == True):
            A = "-" + A
            return(A)
        return(A)

    def To_number(self): #converts a binary number to regular number |not my code|
        binary = int(self.num)
        decimal, i, n = 0, 0, 0
        while(binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary//10
            i += 1
        return(decimal)

    def twos_comp(self, binary_num): #Twos compliment for negative numbers
        twos_num = ""
        not_time = 0
        for x in range(len(binary_num)):
            if (not_time == 0):
                if (int(binary_num[-x -1]) == 1):
                    not_time = 1
                    twos_num = str(binary_num[-x -1]) + twos_num
                else:
                    twos_num = str(binary_num[-x -1]) + twos_num
            else:
                nt = self.lg_not(int(binary_num[-x -1]))
                twos_num = str(nt) + twos_num
        return(twos_num)


    def format(self, set1, set2):
        while len(str(set1)) > len(str(set2)):
            set2 = "0" + str(set2)
        while len(str(set1)) < len(str(set2)):
            set1 = "0" + str(set1)
        return(set1, set2)

    def __add__(self, num2):
        set1 = self.num
        set2 = num2.num
        fsets = self.format(set1, set2) #fsets[0] is num 1 and fsets[1] is num 2
        carry = 0
        fin_num = ""
        for index in range(len(fsets[0])): #loops for the length of the numbers
            val = self.full_adder(int(str(fsets[0])[-index - 1]), int(str(fsets[1])[-index - 1]), carry) #Does the full adder starts on right side of num
            carry = val[1]
            fin_num = str(val[0]) + fin_num
        if (carry == 1): ##Only do the carry if the number is not negative
            fin_num = str(carry) + fin_num
        if (fin_num[0] == 0): ##takes unnedded 0's off the front
            fin_num = fin_num[1:]
        return(fin_num)
            
    def __sub__(self, num2):
        set1 = self.num
        set2 = num2.num
        fsets = self.format(set1, set2) #fsets[0] is num 1 and fsets[1] is num 2
        borrow = 0
        fin_num = ""
        for index in range(len(fsets[0])): #loops for the length of the numbers
            val = self.full_subtractor(int(str(fsets[0])[-index - 1]), int(str(fsets[1])[-index - 1]), borrow) #Does the full adder starts on right side of num
            borrow = val[1]
            fin_num = str(val[0]) + fin_num
        if (borrow == 1):
            fin_num = str(borrow) + fin_num
        if (fin_num[0] == 0): ##takes unnedded 0's off the end
            fin_num = fin_num[1:]
        return(fin_num)


bn1 = Binary_Num("00010100")
bn2 = Binary_Num("110001")
print(bn2 - bn1)
