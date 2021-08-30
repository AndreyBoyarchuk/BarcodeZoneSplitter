import pandas as pd
from os.path import dirname, join
import re
connected = True
city="BOISE"


tags=[" ", ".", " W "," E "," N "," S "," W "," E. "," N. "," S. "," WEST "," EAST "," NORTH "," SOUTH ","W ","E ","N ","S ","WEST ","EAST ","NORTH ","SOUTH ",]
streetSuffixs=[" AVE"," CIR"," CT"," DR", " LN"," PL"," RD"," ST"," WAY", " COURT" " STREET", " LANE"," DRIVE", " ROAD", ]

dataFile = join(dirname(__file__), "libs/dataframe.csv")
dfstreets = pd.read_csv(dataFile)
df1=dfstreets.drop_duplicates(subset=["StName"])
df2=(df1["StName"])

scanValues=[]
def inpt_s(x):
    scanValues.append(x.upper())

def clean_up(barcodeScanner):

    item1=barcodeScanner.split(city,1)
    item2=item1[0]
    streetchoices=[]
    for street in df2:
        if street in item2:
            streetchoices.append(street)
            secondString=streetchoices[0]
            splitSring = item2.split(secondString, 1)
            firstString = (splitSring[0])
        else:
            leftStreets=[]
            leftStreets.append(street)

    integers = re.findall(r"\d+", firstString)
    hNumber = (integers[-1])
    return hNumber, secondString,


def run_query(houseNumber,cleanAddressline):
    dataFile = join(dirname(__file__), "libs/dataframe.csv")
    df = pd.read_csv(dataFile)
    query = df[(df["AddNum"] == houseNumber) & (df["StName"] == cleanAddressline)]
    locationAndAddress = query[['AddNum', 'StName', 'Name']]
    lAAddress=(locationAndAddress.to_string(header=None, index=False))
    return lAAddress


def inputFirst(scannedInpt):
    inpt_s(scannedInpt)
    count=0
    lastItem=scanValues[len(scanValues)-1]
    if city in lastItem:
        address_str=clean_up(lastItem)
        houseNumber=float(address_str[0])
        addressLine=address_str[1]
        output=(run_query(houseNumber,addressLine))
    else:
        output=("Address is not recognized Or Wrong Barcode")
    return output