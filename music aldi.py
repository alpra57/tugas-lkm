import sys
import time

def jalanin_lirik () :
    lirik = [
        ("Dia masih di sini dan menari-nari", 0.3),
        ("Perlahan meracuni kewarasan yang mati", 0.5),
        ("Dia masih di sini dan menari-nari", 0.3),
        ("Perlahan menghantui kenyataan yang sepi", 0.5),
        ("Bertukar peran menyakiti", 0.4),
        ("Seakan ku tak bisa mati (bisa mati)", 0.6),
        ("Berpura-pura pulih sendiri", 0.4),
        ("Nyatanya ku telah mati berkali-kali", 0.6),
    ]

    delay = [0.3, 0.5, 0.3, 0.5, 0.4, 0.6, 0.4, 0.6]
    print("\n==Penyangkalan - For Revenge==")
    time.sleep(2)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
           print(karakter, end='',)
           sys.stdout.flush()
           time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("// code by aldi pratama")    


jalanin_lirik()
