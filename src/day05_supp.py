def get_num(program, position, mode, base):
    '''
    Returns a number from certain position and by mode
    '''
    if position in program.keys(): num = program[position]
    else: num = 0
    
    # Apply modes
    if mode == 2:
        if base + num in program.keys(): return program[base + num]
        else: return 0
    elif mode == 0:
        if num in program.keys(): return program[num]
        else: return 0
        
    return num

def write_num(program, position, mode, base, number):
    '''
    Writes a number to a specific position and returns the altered program
    '''
    
    if mode == 0:
        program[program[position]] = number
    elif mode == 2:
        program[base + program[position]] = number
        
    return program

def run_program(data_in, i, memory, wo_base = True, base = 0):
    '''
    Runs the program on the Intcode computer
    '''
    out = None
    while True:
        
        # Translate instruction
        instr = data_in[i]
        oper  = instr % 100
        instr = int((instr - oper) / 100)
        mode = [0] * 3
        pos = 0        
        while instr > 0:
            mode[pos] = instr % 10
            instr = int((instr - mode[len(mode) - 1]) / 10)
            pos += 1
        
        # Check operation
        assert oper in [1, 2, 3, 4, 5, 6, 7, 8, 9, 99], \
        "operation {} not recognized".format(oper)
        if oper == 99: 
            if wo_base: return data_in, 0, 'end'
            else: return data_in, 0, 'end', base
        
        # Obtain data and do operation
        if oper in [1, 2, 5, 6, 7, 8]:
            # Apply modes
            num1 = get_num(data_in, i + 1, mode[0], base)
            num2 = get_num(data_in, i + 2, mode[1], base)

            # Apply operations
            if oper in [1, 2, 7, 8]:
                if oper == 1:
                    to_write = num1 + num2
                elif oper == 2:
                    to_write = num1 * num2
                elif (oper == 7)*(num1 < num2) or (oper == 8)*(num1 == num2):
                    to_write = 1
                else:
                    to_write = 0

                # Write the final value
                data_in = write_num(data_in, i + 3, mode[2], base, to_write)
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
                    if wo_base: return data_in, i, 'in'
                    else: return data_in, i, 'in', base
                else:
                    data_in = write_num(data_in, i + 1, mode[0], base, memory)
                    memory = None
            else:
                base += get_num(data_in, i + 1, mode[0], base)
            i += 2
        
        # Output operation
        elif oper == 4:
            out = get_num(data_in, i + 1, mode[0], base)
            if wo_base: return data_in, i + 2, out
            else: return data_in, i + 2, out, base
