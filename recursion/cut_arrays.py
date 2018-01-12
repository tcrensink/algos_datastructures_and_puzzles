# recursively bisect array into a nested list, log_2(N) layers deep.  A note on order of recursion:

# Example of recursion calls:
# arr = [1,16,9,20]
#   return = function nest: 				vars assigned:	arr 		left_arr	right_arr
#0  arr_div(arr) 										[1,16,9,20]	[1,16]		[9,20] 
#1  arr_div(l_a = list(arr_div([1,16]))) 							[1]			[16]	
#2  arr_div(l_a = list(arr_div(l_a = list(arr_div([1]))))
#3  arr_div(l_a = list(arr_div(l_a = [1]))) 							[1]
#   (first recursion loops ends)					
#4  arr_div(l_a = list(arr_div(r_a = list(arr_div([16]))))
#5  arr_div(l_a = list(arr_div(r_a = [16]))) 									[16]
#6  arr_div(l_a = list(list(([1],[16]))))							[[1],[16]]
#   (first time all code has been reached)	
#7  arr_div(l_a = [[1],[16]])
#8  arr_div(r_a = list(arr_div([9,20])))								[9]	 		[20]
#   (r_a takes value assigned at this scope, back on step 0)
#9  arr_div(r_a = list(arr_div(l_a = list(arr_div([9]))))
#10 arr_div(r_a = list(arr_div(l_a = [9])))

def arr_div(arr):
	if len(arr) <= 1:
		return arr

	left_arr 	= arr[0:round(len(arr)/2)]
	right_arr 	= arr[round(len(arr)/2):]

	left_arr 	= list(arr_div(left_arr))
	right_arr 	= list(arr_div(right_arr))

	return list((left_arr,right_arr))
