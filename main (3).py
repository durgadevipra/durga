def linearSearchProduct(productList,targetProduct):  
  indicates = []

  for index,product in enumerate(productList):
    if product == targetProduct:
      indicates.append(index)

  return indicates



product = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
result = linearSearchProduct(product,target)
print(result)