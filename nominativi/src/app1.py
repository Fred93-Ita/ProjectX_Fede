from flask import Flask, render_template, request
app= Flask(__name__)


nomi_li = []
nomi_ord = []
contatore = 0

@app.route('/', methods=['GET', 'POST']) 
def main():
    global nomi_li, nomi_ord, contatore
    if request.method == 'POST':
        nome = request.form.get('nome')
        if request.form.get('action1') == 'salva':
            if (contatore != 10):
                nomi_li.append(nome)
                contatore+=1
        elif request.form.get('action3') =='cancella':
            nomi_li.clear()
            nomi_ord.clear()
            contatore = 0
        elif request.form.get('action2')== 'ordina':
            nomi_ord= sorted(nomi_li)
            
    
    return render_template("index.html", nomi_li=nomi_li, nomi_ord=nomi_ord)
 
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port= 5000)
  
