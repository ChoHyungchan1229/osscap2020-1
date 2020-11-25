def weather_icon(char):
	if char == "맑음":
		#sunny
		icon = [
		[0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 3, 3, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 3, 3, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0]]

	elif char == "구름조금":
		#cloud1
		icon =[ 
		[0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 1, 1, 3, 3, 0, 0, 0, 0],
		[0, 0, 0, 6, 7, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 6, 7, 7, 6, 6, 6, 6, 6, 3, 0, 0, 0, 0, 0],
		[0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	elif char == "구름많음":
		#cloud2
		icon =[
		[0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 6, 6, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 1, 1, 4, 4, 0, 0, 0, 0],
		[0, 0, 0, 6, 6, 7, 6, 6, 6, 4, 6, 4, 4, 0, 0, 0],
		[0, 0, 6, 6, 7, 7, 6, 6, 6, 6, 4, 6, 4, 0, 0, 0],
		[0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	elif char == "흐림":	
		icon =[
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 4, 4, 4, 0, 0, 0],
        [0, 0, 0, 6, 6, 7, 6, 6, 6, 6, 4, 6, 4, 4, 0, 0],
        [0, 0, 0, 6, 6, 7, 6, 6, 6, 6, 4, 4, 6, 4, 0, 0],
        [0, 0, 6, 6, 7, 7, 6, 6, 6, 6, 6, 4, 6, 4, 0, 0],
        [0, 0, 6, 6, 7, 6, 6, 7, 7, 6, 6, 4, 4, 0, 0, 0],
        [0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	elif char == "비":
		#rainy
		icon = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0],
		[0, 0, 0, 4, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0],
		[0, 0, 0, 4, 4, 6, 4, 6, 4, 6, 6, 4, 6, 0, 0, 0],
		[0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0],
		[0, 0, 0, 4, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0],
		[0, 0, 4, 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 0, 0],
		[0, 0, 4, 0, 4, 0, 4, 0, 4, 0, 0, 4, 0, 0, 0, 0],
		[0, 0, 0, 4, 0, 4, 0, 0, 4, 0, 4, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	elif char == "눈":
		#snow
		icon = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0],
		[0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0],
		[0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0],
		[0, 0, 7, 0, 0, 0, 0, 7, 0, 0, 0, 0, 7, 0, 0, 0],
		[0, 0, 0, 7, 0, 7, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	elif char == "비 또는 눈" or char == "눈 또는 비":
		#rain&snow
		icon = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0],
		[0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0],
		[0, 0, 0, 4, 4, 6, 6, 4, 6, 6, 6, 6, 6, 0, 0, 0],
		[0, 0, 0, 0, 4, 4, 4, 4, 6, 6, 4, 6, 0, 0, 0, 0],
		[0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0],
		[0, 0, 0, 0, 4, 0, 7, 0, 4, 7, 4, 0, 7, 0, 0, 0],
		[0, 0, 7, 0, 4, 7, 0, 4, 0, 0, 4, 0, 0, 0, 0, 0],
		[0, 0, 0, 4, 0, 0, 0, 4, 0, 4, 0, 7, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	elif char == "천둥번개":
		#ligthning
		icon = [
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 3, 0, 3, 3, 0, 0, 3, 0, 3, 3, 3, 0, 0],
		[0, 0, 3, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 0, 0],
		[0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 3, 0, 0, 0],
		[0, 0, 0, 0, 3, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	else :
		icon =[
		[0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 1, 1, 1, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 6, 6, 6, 6, 1, 1, 3, 3, 0, 0, 0, 0],
		[0, 0, 0, 6, 7, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 6, 7, 7, 6, 6, 6, 6, 6, 3, 0, 0, 0, 0, 0],
		[0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 0, 3, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	return icon
