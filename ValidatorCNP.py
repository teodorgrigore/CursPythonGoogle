import numpy as np

district_dict = {
'01' : 'Alba',
'02' : 'Arad',
'03' : 'Argeș',
'04' : 'Bacău',
'05' : 'Bihor',
'06' : 'Bistrița-Năsăud',
'07' : 'Botoșani',
'08' :'Brașov',
'09' : 'Brăila',
'10' : 'Buzău',
'11' : 'Caraș-Severin',
'12' : 'Cluj',
'13' : 'Constanța',
'14' : 'Covasna',
'15' : 'Dâmbovița',
'16' : 'Dolj',
'17' : 'Galați',
'18' : 'Gorj',
'19' : 'Harghita',
'20' : 'Hunedoara',
'21' : 'Ialomița',
'22' : 'Iași',
'23' : 'Ilfov',
'24' : 'Maramureș',
'25' : 'Mehedinți',
'26' : 'Mureș',
'27' : 'Neamț',
'28' : 'Olt',
'29' : 'Prahova',
'30' : 'Satu Mare',
'31' : 'Sălaj',
'32' : 'Sibiu',
'33' : 'Suceava',
'34' : 'Teleorman',
'35' : 'Timiș',
'36' : 'Tulcea',
'37' : 'Vaslui',
'38' : 'Vâlcea',
'39' : 'Vrancea',
'40' : 'București',
'41' : 'București - Sector 1',
'42' : 'București - Sector 2',
'43' : 'București - Sector 3',
'44' : 'București - Sector 4',
'45' : 'București - Sector 5',
'46' : 'București - Sector 6',
'51' : 'Călărași',
'52' : 'Giurgiu'
}

demographic_dict ={
    1:'Barbat nascut intre 1 ianuarie 1900 si 31 decembrie 1999',
    2:'Femeie nascuta intre 1 ianuarie 1900 si 31 decembrie 1999',
    3:'Barbat nascut intre 1 ianuarie 1800 si 31 decembrie 1899',
    4:'Femeie nascuta intre 1 ianuarie 1800 si 31 decembrie 1899',
    5:'Barbat nascut intre 1 ianuarie 2000 si 31 decembrie 2099',
    6:'Femeie nascuta intre 1 ianuarie 2000 si 31 decembrie 2099',
    7:'Barbat rezident in Romania',
    8:'Femeie rezidenta in Romania',
    9:'Strain'
    }

months ={
    1: 'Ianuarie',
    2: 'Februarie',
    3: 'Martie',
    4: 'Aprilie',
    5: 'Mai',
    6: 'Iunie',
    7: 'Iulie',
    8: 'August',
    9: 'Septembrie',
    10: 'Octombrie',
    11: 'Noiembrie',
    12: 'Decembrie'
    }
def calculate_c(cnp: str) -> int:
    array = [int(x) for x in cnp]
    array.pop()
    a = np.dot(np.array(array), np.array([2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]).T)
    a = a % 11
    if a < 10:
        return a
    else:
        return 1

def check_c(cnp: str, c_bun: int) -> bool:
    last = int(cnp[-1])
    if last == c_bun:
        return True
    return False

def check_cnp(cnp) -> bool:
    if len(cnp) != 13 or not cnp.isnumeric():
        return False
    if cnp[0] == '0':
        return False

    year = int(cnp[1] + cnp[2])
    month = int(cnp[3] + cnp[4])
    day = int(cnp[5] + cnp[6])
    district = int(cnp[7] + cnp[8])
    nnn = int(cnp[9] + cnp[10] + cnp[11])
    control_digit = int(cnp[12])

    if month == 0 or month > 12:
        return False
    if day == 0:
        return False
    if month == 2 and day > 29 and year % 4 == 0:
        return False
    if month == 2 and day > 28 and year % 4 != 0:
        return False
    if month in (1, 3, 5, 7, 8, 10, 12) and day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    global district_dict
    district_dict = {int(k): v for k, v in district_dict.items()}

    if district not in district_dict.keys():
        return False
    if nnn == 0:
        return False
    return check_c(cnp, calculate_c(cnp))

def print_person_info(cnp:str) -> None:
    global district_dict
    global months
    global demographic_dict
    year = int(cnp[1] + cnp[2])
    month = int(cnp[3] + cnp[4])
    day = int(cnp[5] + cnp[6])
    district = int(cnp[7] + cnp[8])
    first_digit = int(cnp[0])
    print(demographic_dict.get(first_digit))
    print("Nascut in: " + str(day) + "-" + months.get(month) + "-" + str(year) +
          " , judetul " + district_dict.get(district))

if __name__ == '__main__':

    cnp = input("Introduceti CNP: ")
    if check_cnp(cnp) == True:
        print("CNP Valid!")
        print_person_info(cnp)
    else:
        print("CNP Invalid!")




