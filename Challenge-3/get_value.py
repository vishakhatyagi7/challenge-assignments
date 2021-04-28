# defining inputs in-script
object_dict = {'a':{'b':{'c':'d'}}}
object_key = "a/b/c"

#fuction to get value of from a nested dictionary
def get_val(dic, key, i):
        key_list = [x for x in key.split('/')]
        if i != len(key_list)-1:
                get_val(dic.get(key_list[i]),key,i+1)
        elif i ==  len(key_list)-1:
                global FINAL_OUTPUT
                FINAL_OUTPUT = dic.get(key_list[i])
        return FINAL_OUTPUT


# calling the function and printing the output
print(get_val(object_dict, object_key, 0))
