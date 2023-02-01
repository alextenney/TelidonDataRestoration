import subprocess
import os

def search_file(string, original_binary, new_binary):
    identifier = string
    replace_string = bytes(' ' * len(identifier), 'utf-8')
    
    with open(original_binary, 'rb') as f:
        lines = f.readlines()
        
    with open(new_binary, 'wb') as fout:
        for line in lines:
            if identifier in line:
                # print("Found in file")
                line = line.replace(identifier, b'')
            fout.write(line)

directories = ["G0001554_A", "G0001554_B", "G0001554_C", "G0001554_D", "G0001555_A", "G0001555_B", "G0001556_A", "G0001556_B", "G0001557", "G0001558"]

def main():
    src = "/home/alex/Documents/W2023/telidon/LAC/P11191"
    dst = "/home/alex/Documents/W2023/telidon/LAC/marked_binary"
    main_path = "/home/alex/Documents/W2023/telidon/LAC/output/"

    # runtime = n^2
    # maybe see if I can change this

    first_pass = True
    i = 0
    for foldername in directories:
        files = os.listdir(main_path + foldername)
        for filename in files:
            f = os.path.join(main_path + foldername, filename)
            if os.path.isfile(f):
                # print("Using file: " + f)
                with open(f, 'rb') as f_search:
                    search_string = f_search.read()
                
                if first_pass:
                    search_file(search_string, src, dst)
                else:
                    search_file(search_string, dst, dst)

                first_pass = False
                i += 1
            
            print(f"{i}/{len(files)}", end="\r")
        print()
        i = 0

if __name__ == '__main__':
    main()