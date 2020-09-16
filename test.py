# import pickle
from sklearn.externals import joblib
#
# Create your model here (same as above)
#

# Save to file in the current working directory
pkl_filename = "sklearn_pipeline.pkl"
# with open(pkl_filename, 'wb') as file:
#     pickle.dump(model, file)

# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = joblib.load(file)

newdata = [":(((","Hàng kém chất lượng"]
# Calculate the accuracy score and predict target values
# score = pickle_model.score(Xtest, Ytest)
# print("Test score: {0:.2f} %".format(100 * score))
Ypredict = pickle_model.predict(newdata)
print(Ypredict)