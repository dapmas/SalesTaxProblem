tax_excluded_items = ['book','chocolate','pill']

def getTaxStatus(itemName):
    taxApplied = True

    for ele in tax_excluded_items:
        if(itemName.find(ele)!=-1):
            taxApplied = False
            break

    if(itemName.find('imported')!=-1):
        imported = True
    else:
        imported = False

    if(taxApplied):
        if(imported):
            return True, True  # sales tax not applied but item is imported.
        else:
            return True, False # Item gets normal tax but not imported.

    else:
        if(imported):
            return False, True
        else:
            return False, False
