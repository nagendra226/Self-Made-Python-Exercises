import googletrans

def translate_file(new_file,trans_lng):
    '''
    INPUT: FileName and Language is Provided.
    OUTPUT: New List and New File is returned with translated language.
    '''
    #Assign Values
    file = new_file
    lng = trans_lng
    
    if(type(lng) == str and type(file) == str and lng.isalpha()):
        
        #Intitialize Values
        translate_list = []
        line_value = None
        g = googletrans.Translator()
        val = None
        
        try:
            my_file = open(file)
            while True:
                line_value = my_file.readline()
                if(g.detect(line_value).lang != lng):
                    if(len(line_value) > 0):
                        val = g.translate(line_value,dest=lng).text
                        translate_list.append(val)
                        #file = open(dest_file,mode='w')
                        #file.writelines(val +'\n')
                    else:
                        my_file.close()# close source file
                        #file.close()#new file
                        break
                else:
                    return "Text Language and File Language are same  can't be converted."
        except err:
            print('Please enter the correct specified path')
            raise err
        return translate_list
    else:
        return "file value and language are not in string."
