#improve performance of imbalanced german credit dataset
from numpy import mean
from numpy import std
from pandas import read_csv
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose	 import ColumnTransformer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import fbeta_score
from sklearn.metrics import make_scorer
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from imblearn.pipeline import Pipeline
from imblearn.combine import SMOTEENN
from imblearn.under_sampling import EditedNearestNeighbours

# load the dataset
def load_dataset(full_path):
	# load the dataset as a numpy array
	dataframe=read_csv(full_path, header=None)
	#split into inputs and outputs
	last_ix = len(dataframe.columns)-1
	X, y = dataframe.drop(last_ix, axis=1), dataframe[last_ix]
	#select categorical and numerical features
	cat_ix = X.select_dtypes(include=['object', 'bool']).columns
	num_ix = X.select_dtypes(include=['int64', 'float64']).columns
	#label encode the target variable to have the classes 0 and 1
	y = LabelEncoder().fit_transform(y)
	return X.values, y, cat_ix, num_ix

# calculate f2-measure
def f2_measure(y_true, y_pred):
	return fbeta_score(y_true, y_pred, beta=2)
	
#evaluate a model
def evaluate_model(X, y, model):
	#define evaluation procedure
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	#define the model evaluation metric
	metric = make_scorer(f2_measure)
	#evaluate model
	scores = cross_val_score(model, X, y, scoring=metric, cv=cv, n_jobs=-1)
	return scores

#define the location of the dataset
full_path = 'german.csv'
#load the dataset
X, y, cat_ix, num_ix = load_dataset(full_path)
#define model to evaluate
model = LinearDiscriminantAnalysis()
#define the data sampling
sampling = SMOTEENN(enn=EditedNearestNeighbours(sampling_strategy='majority'))
# one hot encode categorical, normalize numerical
ct = ColumnTransformer([('c', OneHotEncoder(), cat_ix), ('n', MinMaxScaler(), num_ix)])
# scale, then sample, then fit model
pipeline = Pipeline(steps=[('t', ct), ('s', sampling), ('m', model)])
#evaluate the model and store results
scores = evaluate_model(X, y, pipeline)
print('%.3f (%.3f)' %(mean(scores), std(scores)))
