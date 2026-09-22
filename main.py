from pyscript import document, display

# skills test

def create_order(e):
    document.getElementById("ST_output").innerHTML = "" #reset to avoid the totals stacking in the receipt
    document.getElementById("VAT_output").innerHTML = "" #reset
    document.getElementById("TA_output").innerHTML = "" #reset

    tea1 = document.getElementById("input1") #get value from cook's tea
    tea2 = document.getElementById("input2") #get value from rock's tea
    tea3 = document.getElementById("input3") #get value from monster's tea

    subtotal1 = float(tea1.value) * tea1.checked #to check if the checkbox is checked (checked = *1 and unchecked = *0)
    subtotal2 = float(tea2.value) * tea2.checked 
    subtotal3 = float(tea3.value) * tea3.checked 
    
    subtotal = subtotal1 + subtotal2 + subtotal3 #computation for the subtotal
    vat = subtotal * 0.12 #computation for the tax
    total_amount = subtotal + vat #computation for the total amount

    display(f'Subtotal: ${subtotal}', target="ST_output") #diplays in the receipt 1
    display(f'Tax: ${vat}', target="VAT_output") #displays in the receipt 2
    display(f'Total: ${total_amount}', target="TA_output") #displays in the receipt 3

# project

def generation(e):
    document.getElementById("sku_output").innerHTML = "" # resets

    get_category= document.getElementById("category").value # gets value
    get_name= document.getElementById("name").value # gets value
    get_stock= document.getElementById("stock").value # gets value

    gen_sku = get_category[:3].upper() + "-" + get_name[:4].upper() + "-" + get_stock # concatenates for the SKU
    
    display("Generated SKU: ", gen_sku , target='sku_output') # displays the SKU