import csv
import time
#Example-1 --------------------------------------------------
def hello():
    greet = input("Lütfen Adınızı ve Soyadınızı Giriniz : ")
    return f"Merhaba {greet}, bugün nasılsın ?"
#-------------------------------------------------------------

number_list = []
#Example-2---------------------------------------------------
def opposite():
 while True:

    get_list = int(input("Liste Oluşturmak İçin Sayıları Giriniz.Çıkmak İçin 0 Tuşlayınız..."))
    if get_list == 0:
        break
    number_list.append(get_list)
 number_list.reverse()
 return number_list
#----------------------------------------------------------------

#Example-3-------------------------------------------------------
def numb_control():
    control_numb = int(input("Bir Sayı Giriniz ve Sayının Negatif mi, Pozitif mi Olduğunu Öğreniniz :  "))
    if control_numb > 0:
        print(f"Girdiğiniz Sayı {control_numb} Pozitif Bir Sayıdır.")
    elif control_numb < 0:
        print(f"Girdiğiniz Sayı {control_numb} Negatif Bir Sayıdır.")
    else:
        print(f"Girdiğiniz Sayı {control_numb} Sıfıra Eşittir.")
#------------------------------------------------------------------

#Example-4---------------------------------------------------------
def compare_list():
    list1 = input("Liste1 İçin Veri Girişi Yapınız, Girilen Sayıların Arasına Boşluk Bırakınız. Devam Etmek İçin Enter'a Basınız : ")
    list2 = input("Liste1 İçin Veri Girişi Yapınız, Girilen Sayıların Arasına Boşluk Bırakınız. Devam Etmek İçin Enter'a Basınız : ")
    common = []
    for element in list1:
        if element in list2 and element not in common:
            common.append(element)
    return common

#---------------------------------------------------------------------

#Example-5------------------------------------------------------------
def read():
    with open("example_folder.csv") as look:
        looks = csv.reader(look)

        line_num = sum(1 for row in looks)
        return line_num
line_num = read()
#-------------------------------------------------------------------

#Example-6----------------------------------------------------------
def letter_numb():
    string_numb = input("Lütfen Bir Cümle Giriniz : ")
    letter_dic = {}
    for letter in string_numb:
        if letter in letter_dic:
            letter_dic[letter] +=1
        else:
            letter_dic[letter] = 1
    return letter_dic
#-------------------------------------------------------------------

print(hello())
print("")
print("Liste Terse Çevrildi :",opposite())
print("")
print(numb_control())
print("")
common = compare_list()
print(common)
print("")
print("CSV Dosyası Okunuyor...")
for i in range(5):
    time.sleep(1)
print("Dosyadaki Satır Sayısı : ",line_num)
print("")
print(letter_numb())
