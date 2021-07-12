price_total = float(input("ป้อนตัวเลขราคาเต็ม : "))
before_vat = price_total * 100 / 107
vat = price_total - before_vat
 
print(f"ราคาก่อนภาษีมูลค่าเพิ่ม = {before_vat:.2f}")
print(f"ภาษีมูลค่าเพิ่ม 7% = {vat:.2f}")