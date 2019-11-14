
import sys




def payload_xor(filepath):
    shellcode = ''
    f = open(filepath, 'rb')
    out = open("./payload_xor_c",'wb')
    shellcode_size = 0
    try:
        while True:
            code = f.read(1)
            if not code:
                break
            print(code)
            xorcode = ord(code) ^ 4
            xorcode_str = chr(xorcode)
            code_hex = hex(xorcode)
            code_hex = code_hex.replace('0x','')
            if(len(code_hex) == 1):
                code_hex = '0' + code_hex
            shellcode += '\\x' + code_hex
            shellcode_size += 1
        f.close()
        out.write(bytes(shellcode, encoding = "utf8"))
        out.close()
        return shellcode_size
    except Exception as e:
        sys.stderr.writelines(str(e))




if __name__ == '__main__':
    payload_xor(sys.argv[1])
	
