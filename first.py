from flask import Flask, render_template,request
import scrapping as scp
import analyser_model as anamo
import operation
model,vect = anamo.senti_analyser()
#creating the object name of the flask class
app = Flask(__name__) #file this file to run it




@app.route('/', methods=['POST'])
def index():
    site = request.form['get_value']
    list_review, positive_review, negative_review, title, price, description,image = scp.scrapy(site)
    prediction,total_positive,total_negative = operation.analyse(model,vect,list_review)
    return render_template("index.html",title=title,price=price,description=description, image=image,pi=positive_review,ni=negative_review,prediction=prediction,total_positive=total_positive,total_negative=total_negative)




@app.route('/')
def search():

    return render_template("miniproj.html")


if __name__ == '__main__':
    app.run()
