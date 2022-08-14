# feedforward-nn-python (WIP)
A feedforward neural network model using Python and NumPy, to predict UK housing prices 

### Overview

After completing the fast.ai course and reading the NNFS book by Harrison Kinsley & Daniel Kukieła, I want to
put knowledge into practice, but I don't want to use Tensorflow to create the model in 10 lines of code. The model will
be implemented using only Python with NumPy (I will also use Pandas for data pre-processing), which will encourage a
better understanding of how the model really works, without abstracting every function. 

The model will try to predict
the price of a house, given some input of features. I will use a neural network architecture for non-linear regression.


### Data
1. **Prices Paid** is a free dataset from the UK Government's, _HM & Land Registry_ website, which can be found [**here.**](https://www.gov.uk/guidance/about-the-price-paid-data#data-excluded-from-price-paid-data)
This dataset contains prices paid for registered properties for the 
year 2021. 

Below shows a sample from the dataset. Columns explanations can also be found in the link above.


<table class="sample">
	<thead>
	<tr>
		<th>UID</th>
		<th>Price</th>
		<th>Date</th>
		<th>Postcode</th>
		<th>PropertyType</th>
		<th>Old/New</th>
		<th>Duration</th>
		<th>PAON</th>
		<th>SAON</th>
		<th>Street</th>
		<th>Locality</th>
		<th>Town/City</th>
		<th>District</th>
		<th>County</th>
		<th>PPD</th>
		<th>Status</th>
	</tr>
	</thead>
	<tbody>
	<tr>
		<td>&nbsp;CFC9085C-AF6E-9A70-E053-6B04A8C09D6A</td>
		<td>&nbsp;£395000</td>
		<td>&nbsp;2021-06-22</td>
		<td>&nbsp;B96 6HN</td>
		<td>&nbsp;D</td>
		<td>&nbsp;N</td>
		<td>&nbsp;F</td>
		<td>&nbsp;1</td>
		<td>&nbsp;NULL</td>
		<td>&nbsp;HIGH STREET</td>
		<td>&nbsp;FECKENHAM</td>
		<td>&nbsp;REDDITCH</td>
		<td>&nbsp;REDDITCH</td>
		<td>&nbsp;WORCESTERSHIRE</td>
		<td>&nbsp;A</td>
		<td>&nbsp;A</td>
	</tr>
    </tbody>
</table>

Now we have the data, it's time for feature selection

 - **Which features are the most important for predicting house prices?**


House Size, Location, Number of Bedrooms, Number of Bathrooms, Location Crime Rate, Local Schools, Property Condition,
State of the Housing Market and Economy and many more variables, all contribute to the price of a house. The more data
we have about a house, the more accurate we can expect model predictions to be. 



As you might notice, the dataset I've chosen isn't the most expressive, but it's fine to use just to build up a first 
draft of our neural network.


Property types, location and whether the property is old or new, all directly contribute to the price of a house.
Having 6 columns to describe the location of a property probably won't help the model to learn more about how location
impacts price, especially if there are inconsistencies in the data. Using the pgeocode python library, I can get the
longitude and latitude from a postcode column. Not every (long,lat) pair will be 100% accurate, but we'll see how well 
the model does with it. We'll use longitude, latitude and the city name as features describing location. The other
features will be dropped except property type and old/new, and we'll keep duration too. 

 - **Is the data enough?**

The quantity of records certainly should be, however just from looking at the columns and a reasonable estimate, it's
unlikely the model will perform very well with so few features. Location will probably be the most impactful feature on
the prediction, but as mentioned already, many more variable contribute to the price of a house. The model likely won't
be very accurate, but it should be able to predict at the very worst, prices close to the average in the dataset. This
should be enough to develop a functional model, after that I'll train using a more expressive dataset.


### Normalization

Before defining the model, the features will need to be normalized. If we left the data as is, a feature like price
which can be up in the millions, will have a much bigger effect on the network compared to longitude and latitude, which
for the UK, will generally be an integer below 60. **We'll normalize every feature to be between 0 and 1.** Cities are 
currently described by a string, we need to convert the string into a numerical form, so that the model can interpret
it. To do that, we'll create a one hot encoding for each city. Since I don't have a fancy GPU, I'll end up with over
1000 features if I use every city, which will probably take a while to train. I'll drop cities with less than 600
appearances in the dataset into a single category, we'll call 'other'. This leaves us with a total of **378** **features**. 


### Model Architecture

    dense1 = Dense_Layer(X_train.shape[1], 128, weight_regularizer_l1=1e-4, bias_regularizer_l1=1e-4)
    activation1 = ReLU_Activation()
    dropout1 = Dropout_Layer(0.1)
    dense2 = Dense_Layer(128, 128)
    activation2 = ReLU_Activation()
    dropout2 = Dropout_Layer(0.1)
    dense3 = Dense_Layer(128, 1)
    activation3 = Linear_Activation()
    loss_function = MSE_Loss()
    optimizer = Optimizer_Adam(learning_rate=0.001, decay=1e-3)

