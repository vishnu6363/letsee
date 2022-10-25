from flask import Flask,request,render_template,url_for
import numpy as np
import pickle
crop_recommendation_model_path = 'RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))
app=Flask(__name__)
@ app.route('/')
def openpage():
    return render_template('index.html')
@ app.route('/crop-predict', methods=['POST'])
def crop_predict():
    title = 'Harvestify - Crop Recommendation'
    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorus'])
        K = int(request.form['potasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temp=float(request.form['temp'])
        humidity=float(request.form['humidity'])
        if temp>43:
            return render_template('index.html',prediction="You cant able to grow any crops in {} temperature".format(temp))
        elif temp<8:
            return render_template('index.html',prediction="You cant able to grow any crops in {} temperature".format(temp))
        
        elif ph<3:
             return render_template('index.html',prediction="You cant able to grow any crops in {} PH Level".format(ph))
        elif ph>10:
             return render_template('index.html',prediction="You cant able to grow any crops in {} PH Level".format(ph))
        elif humidity<13:
             return render_template('index.html',prediction="You cant able to grow any crops in {} Humidity".format(humidity))
        elif humidity>100:
             return render_template('index.html',prediction="You cant able to grow any crops in {} Humidity".format(humidity))
        elif N>140:
             return render_template('index.html',prediction="You cant able to grow any crops in {} temperature".format(temp))
        elif P>150:
             return render_template('index.html',prediction="You cant able to grow any crops if your soil containing more phosphorus like {} ".format(P))
        elif K>210:
             return render_template('index.html',prediction="You can't able to grow any crops if the Pottasium is very high in your soil {} ".format(K))
        elif rainfall>300:
             return render_template('index.html',prediction="You can't able to grow any crops if the rainfall is {} ".format(rainfall))      
            
            
        

        data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]
        if final_prediction== "rice":
            text="You should Grow Rice in your From.Beacues Rice is a tropical crop and grown where the average temperature during the growing season is between 20°C and 27°C.Although the regions are having average annual rainfall between 175—300 cm are the most suitable. Phosphorus availability to rice is optimum when the pH is below 6.5 "
            return render_template('index.html',prediction=text)
        elif final_prediction=="maize":
            text="You should Grow Maize in your From.\n Maize can be grown successfully in variety of soils ranging from loamy sand to clay loam. However, soils with good organic matter content having high water holding capacity with neutral pH are considered good for higher productivity."
            return render_template('index.html',prediction=text) 
        elif final_prediction=="chickpea":
            text="You should Grow hickpea in your From.\nThis crop is grown on moderately heavy soils, black cotton soils, and sandy loam soils. However, Fertile sandy loam to clay loam soils with good internal drainage are best suitable for its cultivation . Soils should not be heavy alkaline in nature. Ideal PH range of 5.5 to 7.0 is suitable for chickpea farming."
            return render_template('index.html',prediction=text)
        elif final_prediction=="kidneybeans":
            text="You should Grow kidneybeans in your From.\nIt can be grown on wide range of soils from light sandy to heavy clay soils. Well drained loamy soil is good for kidney beans cultivation. It is very sensitive to saline soils. Gives best result when pH of soil is 5.5 to 6."
            return render_template('index.html',prediction=text)
        elif final_prediction=="pigeonpeas":
            text="You should Grow pigeonpeas  in your From.\nSoil Type & Field Preparation It is successfully grown in black cotton soils, well drained with a pH ranging from 7.0-8.5. Pigeonpea responds well to properly tilled and well drained seedbed."
            return render_template('index.html',prediction=text)
        elif final_prediction=="mothbeans":
            text="You should Grow mothbeans in your From.\nMoth bean, a short-day crop, is one of the most drought-resistant pulses in India. Grown at altitudes up to 1300 m above sea level, it has a wide pH range (3.5–10) and can tolerate slight salinity. While dry sandy soil is most suitable for production, moth bean can tolerate a variety of soil types."
            return render_template('index.html',prediction=text)
        elif final_prediction=="mungbean":
            text="You should Grow mungbean in your From.\nMungbean is grown on a wide range of soils including red laterite soils, black cotton soils and sandy soils. A well-drained loamy to sandy loam soil is best for its cultivation. The crop does not grow well on saline and alkaline soil or waterlogged soils."
            return render_template('index.html',prediction=text)
        elif final_prediction=="blackgram":
            text="You should Grow blackgram in your From.\nBlack gram can be grown on variety of soils ranging from sandy soils to heavy cotton soils. The most ideal soil is a well drained loam with pH of 6.5 to 7.8. Black gram cannot be grown on alkaline and saline soils. Land is prepared like any other kharif season pulse crop."
            return render_template('index.html',prediction=text)
        elif final_prediction=="lentil":
            text="You should Grow lentil in your From.\nThe optimum temperature for growth is 18-30°C. Soil Type and Field Preparation Well drained, loam soils with neutral reaction are best for lentil cultivation. Acidic soils are not fit for growing lentil. The soil should be friable and weed free so that seeding could be done at uniform depth"
            return render_template('index.html',prediction=text)
        elif final_prediction=="pomegranate":
            text="You should Grow pomegranate in your From.\nPomegranate grows well under semi-arid conditions and can be grown upto an altitude of 500 m. above m.s.l.. It thrives well under hot, dry summer and cold winter provided irrigation facilities are available. The tree requires hot and dry climate during fruit development and ripening."
            return render_template('index.html',prediction=text)
        elif final_prediction=="banana":
            text="You should Grow banana in your From.\nDeep, rich loamy soil with pH between 6.5 – 7.5 is most preferred for banana cultivation. Soil for banana should have good drainage, adequate fertility and moisture. Saline solid, calcareous soils are not suitable for banana cultivation."
            return render_template('index.html',prediction=text)
        elif final_prediction=="mango":
            text="You should Grow mango  in your From.\nMango grows well on wide variety of soils, such as lateritic, alluvial, sandy loam and sandy. The loamy, alluvial, well-drained, aerated and deep soils (2-2.5 m) rich in organic matter with a pH range of 5.5-7.5 are ideal for mango cultivation."
            return render_template('index.html',prediction=text)
        elif final_prediction=="grapes":
            text="You should Grow grapes in your From.\nSandy to clayey and loamy soil with good drainage and irrigation facilities is suitable for the cultivation of Grapes. Soils having pH value from 6.5 to 7.5 are most suitable. In its natural habitat, the crop bears fruit during the hot and dry period and undergoes dormancy during the period of severe cold."
            return render_template('index.html',prediction=text)
        elif final_prediction=="watermelon":
            text="You should Grow watermelon  in your From.\nWatermelon grows well in deep fertile and well-drained soil. It gives best result when grown on sandy or sandy loam soil. Soil having poor drainage capacity is not suited for watermelon cultivation."
            return render_template('index.html',prediction=text)
        elif final_prediction=="muskmelon":
            text="You should Grow muskmelon in your From.\nIt grows well in deep fertile and well-drained soil. It gives best result when grown on well drained loam soil. Soil having poor drainage capacity is not suited for Muskmelon cultivation. Follow crop rotation as continuous growing of same crop on same field leads loss of nutrients, poor yield and more disease attack"
            return render_template('index.html',prediction=text)
        elif final_prediction=="apple":
            text="You should Grow apple in your From.\nApples grow best on a well-drained, loam soils having a depth of 45 cm and a pH range of pH 5.5-6.5. The soil should be free from hard substrata and water-logged conditions. Soils with heavy clay or compact subsoil are to be avoided. growth period"
            return render_template('index.html',prediction=text)
        elif final_prediction=="orange":
            text="You should Grow orange in your From.\nDeep well drained loamy soils are the best for the cultivation of sweet orange. Heavy soils, if well drained, yield good crops but cultivation becomes difficult. The pH of soil should be 6.5 to 7.5 and EC of water should be less than 1.0. Plant is highly sensitive to water-logged soils."
            return render_template('index.html',prediction=text)
        elif final_prediction=="papaya":
            text="You should Grow papaya in your From.\nA high fertile soil with good drainage is most desirable for successful papaya I cultivation. The plant grows well in I sandy loam soil having PH between 6.5 I to 7. Papaya grows well in sun, warm & humid climate. The plant can be grown to elevation of 1000 m above the sea level but can't withstand frost."
            return render_template('index.html',prediction=text)
        elif final_prediction=="coconut":
            text="You should Grow coconut in your From.\nThe major soil types that support coconut in India are laterite, alluvial, red sandy loam, coastal sandy and reclaimed soils with a pH ranging from 5.2 to 8.0. Soil with a minimum depth of 1.2m and fairly good water holding capacity is preferred for coconut cultivation."
            return render_template('index.html',prediction=text)
        elif final_prediction=="cotton":
            text="You should Grow cotton in your From.\nCotton is grown on a variety of soils ranging from well drained deep alluvial soils in the north to black clayey soils of varying depth in central region and in black and mixed black and red soils in south zone."
            return render_template('index.html',prediction=text)
        elif final_prediction=="jute":
            text="You should Grow jute in your From.\nJute can be raised on all kinds of soils from clay to sandy loam, but loamy alluvial are best suited. Laterite and gravel soils are not suitable for this crop. The new grey alluvial soils of good depth, receiving silt from the annual floods are the best for jute cultivation."
            return render_template('index.html',prediction=text)
        elif final_prediction=="coffee":
            text="You should Grow  in your From.\nWhile soil is frequently referred to as the fertile substrate, not all soils are suitable for growing crops. Ideal soils for agriculture are balanced in contributions from mineral components (sand: 0.05–2 mm, silt: 0.002–0.05 mm, clay: <0.002 mm), soil organic matter (SOM), air, and water."
            return render_template('index.html',prediction=text)
        else:      
           return render_template('index.html', prediction='You should grow {} in your form'.format(final_prediction))
if(__name__=="__main__"):
    app.run(debug=True)

