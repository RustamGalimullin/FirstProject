def loger(primer, result):
    with open('file.txt', 'w') as data:
        rasparse = " ".join(primer)
        rasparse = rasparse + "="
        result = result + ';'
        data.write(str(rasparse))
        data.write(str(result))
        


        