# Qingyuan Zheng

import datetime
import math 


#
start_date = datetime.datetime(2021, 9, 1)
end_date = datetime.datetime(2023, 12, 31)

# future contract FUT
# options on future OOF
table_B_FUT = []
table_B_OOF = []
table_81_FUT = []
table_81_OOF = []

def process_B(s: str):
    comodity = 'CL'
    product_type = s[15:18]
    if product_type == 'FUT':
        contract_month = s[18:22] + '-' + s[22:24]
        expiration = s[91:95] + '-' + s[95:97] +'-' + s[97:99]
        table_B_FUT.append([comodity, contract_month, 'Fut', expiration, None, None])

    elif product_type == 'OOF':
        options = 'LO'
        contract_month = s[18:22] + '-' + s[22:24]
        options_exp = s[91:95] + '-' + s[95:97] +'-' + s[97:99]
        table_B_OOF.append([comodity, contract_month, 'Opt', None, options, options_exp])

    return

def process_81(s: str):
    comodity = 'CL'
    product_type = s[25:28]
    if product_type == 'FUT':
        contract_month = s[29:33] + '-' + s[33:35]
        settlement_price = "{:.2f}".format(float(s[108:122])/100.0)
        table_81_FUT.append([comodity, contract_month, 'Fut', None, settlement_price])

    elif product_type == 'OOF':
        contract_type = 'Put' if s[28] == 'P' else 'Call'
        contract_month = s[29:33] + '-' + s[33:35]
        settlement_price = "{:.2f}".format(float(s[108:122])/100.0)
        strike_price = "{:.2f}".format(float(s[47:54])/100.0)
        table_81_OOF.append([comodity, contract_month, contract_type, strike_price, settlement_price])

    
    return


with open('cme.20210709.c.pa2', 'r') as fin:
    for line in fin:
        #datetime is used to compare the time
        # can change the numbers into datetime format
        if line[0] == 'B' and (line[5:15].strip() == 'CL' or line[5:15].strip() == 'LO') and \
            start_date <= datetime.datetime.strptime(line[18:24], '%Y%m') and \
            end_date >= datetime.datetime.strptime(line[18:24], '%Y%m'):
            process_B(line)
        elif line[:2] == '81' and (line[5:15].strip() == 'CL' or line[5:15].strip() == 'LO') and \
            start_date <= datetime.datetime.strptime(line[29:35], '%Y%m') and \
            end_date >= datetime.datetime.strptime(line[29:35], '%Y%m'):
            process_81(line)
    fin.close()

with open('CL_expirations_and_settlements.txt', 'w') as fout:
    fout.write(tabulate(table_B_FUT + table_B_OOF, headers = ['Futures\nCode', 'Contract\nMonth', 'Contract\nType', 'Futures\nExp Date', 'Options\nCode', 'Options\nExp Date'], tablefmt='simple'))
    fout.write('\n')
    fout.write('\n')
    fout.write(tabulate(table_81_FUT + table_81_OOF, headers = ['Futures\nCode', 'Contract\nMonth', 'Contract\nType', 'Strike\nPrice', 'Settlement\nPrice'], tablefmt='simple'))
    fout.close()
    