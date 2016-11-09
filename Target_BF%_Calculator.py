currentWeight = float(raw_input("Current weight: "))
currentBF = float(raw_input("Current Body Fat %: ")) / 100
currentFat = currentWeight*currentBF

bulkLength = float(raw_input("Bulk length (weeks): "))
gainsPerWeek = float(raw_input("Gain per week: "))
muscleGainRatio = float(raw_input("Muscle/Fat Gain Ratio: "))

targetWeight = bulkLength * gainsPerWeek + currentWeight
targetFatGain = (1 - muscleGainRatio)*gainsPerWeek*bulkLength

targetFat = currentFat + targetFatGain

targetBF = targetFat / targetWeight

print targetWeight
print str(targetBF*100) + "%"
