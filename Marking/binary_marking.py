import subprocess
import shutil

def search_file(string, original_binary, new_binary):
    identifier = bytes(string, 'utf-8')
    replace_string = bytes(' ' * len(identifier), 'utf-8')

    fout = open(new_binary, "wb")

    with open(original_binary, 'rb') as f:
        for line in f.readlines():
            if identifier in line:
                # To do:
                # figure out how to output the parts of the binary????
                print("Found in file")
                line = line.replace(identifier, b'')
                
            fout.write(line)
                
                # break
   
    fout.close()

# function to loop through all the files of Aycock's output, and grab
# that string

#def grab_string():


if __name__ == '__main__':
    # make a duplicate of the original binary file to ensure there is no changes to the original 
    # if the string is found, it will replace the characters with blank spaces
    # in the end I will only be left with parts of the binary I could not match

    # if file does not exist, make it
    # src = "/home/alex/Documents/W2023/telidon/LAC/P11191"
    src = "/home/alex/Documents/W2023/telidon/output/test"
    dst = "/home/alex/Documents/W2023/telidon/LAC/marked_binary"

    # else, throw an error and exit 
    # dont make a billion files I guess

    search_string = """  =@ {O!H@@I<v"@@V"@@@Ma$BLVT$B\FE$BdvL$BtVI$B|vD$JLnO$J\^N<I"@@@IDK$BKjNEWS UPDATE<v"@@@Ma$AOQT$A_AE$AgqL$AwQI$AqD$IOiO$I_YN<I"@@@IDK$AMmNEWS UPDATE<v"@@@Ma$AITT$AYDE$AatL$AqTI$AytD$IIlO$IY\N<I"@@@IDK$AHhNEWS UPDATE<v"@@@Ma$@KWT$@[GE$@cwL$@sWI$@{wD$HKoO$H[_N<I"@@@IDK$@JkNEWS UPDATE+Z|rhh@JcrPX@IfuPX@IeuPX@IapPX@I`pPX@HcsPX@HbsPX@3Jpvxx]<"@@@ArL$Jp~ TELIDON REPORTS$IsH2 TELIDON NEWSLETTERS"@@@KA"@@@ArL$HuI3 TELIDON FORMS"@@@IDK$IrM"""
    search_file(search_string, src, dst)
