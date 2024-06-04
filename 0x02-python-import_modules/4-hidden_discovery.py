#!/usr/bin/python3

import dis
import marshal

with open("hidden_4.pyc", "rb") as f:
    f.read(16)
    code_byte = f.read()
    code_obj = marshal.loads(code_byte)

    instructions = dis.get_instructions(code_obj)

    for instruct in instructions:
        if instruct.argrepr != "None":
            if instruct.argrepr and instruct.argrepr[0].isalpha():
                print(instruct.argrepr)
