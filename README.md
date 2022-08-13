# feedforward-nn-python (WIP)
A feedforward neural network model using Python and NumPy, to predict UK housing prices 

### Overview

After completing the fast.ai course and reading the NNFS book by Harrison Kinsley & Daniel Kukieła, I want to
put knowledge into practice, but I don't want to use Tensorflow to create the model in 10 lines of code. The model will
be implemented using only Python with NumPy (I will also use Pandas for data pre-processing), which will encourage a
better understanding of how the model really works, without abstracting every function.

### Model

The model will try to predict the price of a house, given some input of features. I will use a neural network
architecture for regression, therefore Mean Squared Error (MSE) will be the best initial choice for the loss function. 

### Data
A free dataset from the UK Government's, HM & Land Registry website, which can be found [here.](https://www.gov.uk/guidance/about-the-price-paid-data#data-excluded-from-price-paid-data)
This dataset contains prices paid for registered properties for the 
year 2021. (talk more about the dataset, what data is missing etc.)

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

 - Should I use every feature from the dataset?

 - Which features are the most important for predicting house prices?