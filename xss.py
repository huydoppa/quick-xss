import os
import sys

def main():
    print("setup : sudo python3 setup.py")
    print("run: python3 xss.py host.txt payload.txt output.txt")
    host = sys.argv[1]
    payload = sys.argv[2]
    output = sys.argv[3]
    with open(payload,"r") as f:
        payloads = f.readlines()
        for payload in payloads:
            payload.replace('"','\\"')
            print(payload)
            os.system(" cat "+host+"| waybackurl | tee -a endpoint.txt ; cat endpoint.txt | qsreplace '"+payload+"' | tee -a "+output +";cat "+output+" | freq | tee -a possible_xss.txt")
if __name__== "__main__" :
    main()
