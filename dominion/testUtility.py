import Dominion

def GetBoxes(nV):
    box = {}
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

def GetSupplyOrder():
    supplyOrder = {
                    0:['Curse','Copper'],
                    2:['Estate','Cellar','Chapel','Moat'],
                    3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                    4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                    5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                    6:['Gold','Adventurer'],
                    8:['Province']
                }
                
    return supplyOrder
def fillSupply(supply, numCopper, numSilver, numGold, numEstate, numDuchy, numProvince, numCurse):
    supply["Copper"]=[Dominion.Copper()]*numCopper
    supply["Silver"]=[Dominion.Silver()]*numSilver
    supply["Gold"]=[Dominion.Gold()]*numGold
    supply["Estate"]=[Dominion.Estate()]*numEstate
    supply["Duchy"]=[Dominion.Duchy()]*numDuchy
    supply["Province"]=[Dominion.Province()]*numProvince
    supply["Curse"]=[Dominion.Curse()]*numCurse