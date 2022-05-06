from matplotlib.pyplot import get

class Price:

    #by evan
    #inState, reqb4 are all boolean
    def __init__(self, reqAmount, inState, reqb4):
        self.reqAmount = reqAmount
        self.inState = inState
        self.reqb4 = reqb4

    def show(self):
        print("ReqAmount is: ", self.reqAmount)
        print("in out state is: ", self.inState)
        print("req b state is: ", self.reqb4) 

    def margin(self):
        finalNum = 0
        GReqfactor = 0

        if self.reqAmount > 1000:
            GReqfactor = 0.02
        else:
            GReqfactor = 0.03

        if self.inState == True and self.reqb4 == True:
            finalNum = (0.02-0.01+GReqfactor+0.1) * 1.5
        elif self.inState == False and self.reqb4 ==True:
            finalNum = (0.04-0.01+GReqfactor+0.1) * 1.5
        elif self.inState == True and self.reqb4 ==False:
            finalNum = (0.02+GReqfactor+0.1) * 1.5
        elif self.inState == False and self.reqb4 ==False:
            finalNum = (0.04+GReqfactor+0.1) * 1.5
        return finalNum

    def getSuggested(self):
        getsug = 0
        getsug = 1.5 + Price.margin(self)
        #print(getsug)
        return getsug

    def totalDue(self):
        payme = 0
        payme = round(self.reqAmount * Price.getSuggested(self), 2)
        format_payme = "{:.2f}".format(payme)
        return format_payme

'''
Additional Validations:
• Make suggested price and total amount fields in your Quote form read-only, i.e. user cannot enter these values.
• Create another button on Quote Form before Submit, call it "Get Quote".
• After user enters all other fields in the form other than Suggested Price and Total Amount, allow user to click on "Get Quote", i.e. Get Quote and Submit Quote buttons should be disabled if there are no values entered in the form. 
• When user clicks on "Get Quote" button make a call to Pricing Module and populate the suggested price and total. 
• Display Suggested Price and Total Amount once you get the values from pricing module. 
• Make sure you do not lose any form values when you make a call to Pricing module.
• You can use AJAX call to achieve this i.e.  partial form submission. 
• Then user clicks on Submit Quote and you save the quote.
'''

'''
Suggested Price = Current Price + Margin

Where,

Current price per gallon = $1.50 (this is the price what distributor gets from refinery and it varies based upon crude price. But we are keeping it constant for simplicity)
Margin =  Current Price * (Location Factor - Rate History Factor + Gallons Requested Factor + Company Profit Factor)

Consider these factors:
Location Factor = 2% for Texas, 4% for out of state.
Rate History Factor = 1% if client requested fuel before, 0% if no history (you can query fuel quote table to check if there are any rows for the client)
Gallons Requested Factor = 2% if more than 1000 Gallons, 3% if less
Company Profit Factor = 10% always

Example:
1500 gallons requested, in state, does have history (i.e. quote history data exist in DB for this client)

Margin => (.02 - .01 + .02 + .1) * 1.50 = .195
Suggested Price/gallon => 1.50 + .195 = $1.695
Total Amount Due => 1500 * 1.695 = $2542.50
'''

def printevan():
    print("Hi this is written by evan")