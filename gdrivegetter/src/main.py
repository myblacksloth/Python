# (C) Antonio Maulucci 12/10/2023 - antomau.com

# downloader automatico
# dei contenuti di google drive
# indicati nella pagina [[[s_p_o_i_l_e_r]]]
# per scaricare le videolezioni di statistica


import gdown
import datetime



da_rimpiazzare1 = "/file/d/"
rimpiazzo1 = "/u/0/uc?id="
rimpiazzo2 = "&export=download"
da_rimpiazzare2 = "/view?usp=sharing"


with open("toDownload.txt", "r") as f:
    lines = f.readlines() # leggi tutte le righe di un file
    numOfFiles = len(lines)
    # ======================================================
    filename = ""
    fileurl = ""
    # ======================================================
    for i in range(0, len(lines)):
        if i %2 == 0: # e' il nome di un file
            filename = lines[i].rstrip('\n')
            basename = "downloaded/"
            extension = ".mp4"
            filename = basename+filename+extension
        else: # e' ulr
            print(f"downloading {int(i/2)} of {numOfFiles/2}")
            fileurl = lines[i].rstrip('\n')
            newUrl = fileurl.replace(da_rimpiazzare1, rimpiazzo1)
            newUrl = newUrl.replace(da_rimpiazzare2, rimpiazzo2)
            try:
                gdown.download(newUrl, filename)
                print(f"\033[42mmdownloaded {newUrl}:::::{filename}\033[0m")
            except:
                with open("errorlog.txt", "a") as ef:
                    nowtime = datetime.datetime.now()
                    ef.write(f"[{nowtime}] errore sul file {newUrl} ::::: {filename}")
                print(f'\033[41merrore sul file {filename} con url {newUrl}\033[0m')

