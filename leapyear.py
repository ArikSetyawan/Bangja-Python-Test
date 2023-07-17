import datetime
 
def getDays(number_of_days:int, kabisat:bool=False):
    # get first date of this year
    fist_date = datetime.datetime.strptime('01/01/2023', '%d/%m/%Y')
    # add number_of days to first date
    second_date = fist_date + datetime.timedelta(days=number_of_days)

    # format second_date to full month name and day
    formatted_return = f"{second_date.strftime('%B')}, {second_date.strftime('%d')}# Adalah hari ke {number_of_days} dari {'bukan' if not kabisat else ''} tahun kabisat"
    return formatted_return


print(getDays(366,True))