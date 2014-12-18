from PIL import Image
from glob import glob
from datetime import datetime
import numpy as np
import pandas as pd
from sklearn import ensemble, cross_validation, preprocessing, tree
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.cross_validation import cross_val_score as k_fold_CV

def dir_to_dataset2(glob_files, loc_train_labels=""):
    """Munging to yummy sklearn-ready data """
    print("Gonna process:\n\t %s"%glob_files)
    dataset = []
    for file_count, file_name in enumerate( sorted(glob(glob_files),key=len) ):
        image = Image.open(file_name)
        img = Image.open(file_name).convert('LA') #tograyscale
        pixels = [f[0] for f in list(img.getdata())]
        dataset.append(pixels)
        if file_count % 1000 == 0:
            print("\t %s files processed"%file_count)
    
    if len(loc_train_labels) > 0:
        df = pd.read_csv(loc_train_labels)
        return np.array(dataset), np.array(df["Class"])
    else:
        return np.array(dataset)

def dir_to_dataset(hog_features="", loc_train_labels=""):
    """Munging to yummy sklearn-ready data """
    if len(hog_features) > 0:
        data = pd.read_csv(hog_features, header=0)
    if len(loc_train_labels) > 0:
        df = pd.read_csv(loc_train_labels)
        return np.array(data), np.array(df["Class"])
    else:
        return np.array(data)
    
if __name__ == "__main__":
    ''''''
    start = datetime.now()
    #Loading the data
    X_train, y = dir_to_dataset("trainPaper.csv","trainLabels.csv")
    # X_train = np.append(X_train, dir_to_dataset("trainPaper.csv"), axis=0)
    # y = np.append(y, y)
    # X_train, y = dir_to_dataset2("trainPaperNoThresh\\*.BMP","trainLabels.csv")
    print( "Train Shape:\n\t%s"%str(X_train.shape) )
    print( "Labels Shape:\n\t%s\n"%str(y.shape) )
    X_test = dir_to_dataset("testPaper.csv")
    # X_test = dir_to_dataset2("testPaperNoThresh\\*.BMP")
    print( "Test Shape:\n\t%s\n\n"%str(X_test.shape) )
    le = preprocessing.LabelEncoder()
    le.fit(y)
    y = le.transform(y)

    #Classifier Setting
    clf = ensemble.ExtraTreesClassifier(n_estimators=1025,n_jobs=7,random_state=1, verbose = 1)
    print("Classifier:\n\t %s"%str(clf))
    
    #CV
    #scores = cross_validation.cross_val_score( clf, X_train, y, cv=10)
    #print("\n10-fold Validation Categorization Accuracy:\n\t %0.5f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
    
    #Fitting
    clf.fit(X_train,y)
    
    #Label decoding the predictions
    preds = list(le.inverse_transform(clf.predict(X_test)))
    
    #Creating submission
    with open("Try.csv","wb") as outfile:
        outfile.write("ID,Class\n")
        for e, pred in enumerate(preds):
            outfile.write("%s,%s\n"%(6284+e,pred))
    
    print("\n\n\t\tScript Running Time: %s"%str(datetime.now()-start))