def run_program(data_in, i, memory):
    '''
    Runs the program on the Intcode computer
    '''
    out = None
    base = 0
    while i < len(data_in):
        
        # Translate instruction
        instr = data_in[i]
        oper  = instr % 100
        instr = instr - oper
        mode1 = instr % 1000
        mode2 = int(((instr - mode1) % 10000) / 1000)
        mode1 = int(mode1 / 100)
        
        # Check operation
        assert oper in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99], \
        "operation {} not recognized".format(oper)
        if oper == 99: return data_in, 0, 'end'
        
        # Obtain data and do operation
        if oper in [1, 2, 5, 6, 7, 8]:
            # Apply modes
            num1 = data_in[i + 1]
            num2 = data_in[i + 2]
            if mode1 == 2:
                num1 = data_in[base + num1]
            elif mode1 == 0:
                num1 = data_in[num1]
            if mode2 == 2:
                num2 = data_in[base + num2]
            elif mode2 == 0:
                num2 = data_in[num2]
            
            # Apply operations
            if oper in [1, 2, 7, 8]:
                if oper == 1:
                    to_store = num1 + num2
                elif oper == 2:
                    to_store = num1 * num2
                elif (oper == 7)*(num1 < num2) or (oper == 8)*(num1 == num2):
                    to_store = 1
                else:
                    to_store = 0
                data_in[data_in[i + 3]] = to_store
                i += 4
            else:
                if (oper == 5)*(num1 != 0) or (oper == 6)*(num1 == 0):
                    i = num2
                else:
                    i += 3
                    
        # Operation of save to memory / base change
        elif oper in [3, 9]:
            if oper == 3:
                if memory is None:
                    return data_in, i, 'in'
                else:
                    data_in[data_in[i + 1]] = memory
                    memory = None
            else:
                base += data_in[i + 1]
            i += 2
        
        # Output operation
        elif oper == 4:
            out = data_in[i + 1]
            if mode1 == 2:
                out = data_in[base + out]
            elif mode1 == 0:
                out = data_in[out]
            return data_in, i + 2, out
