import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn import metrics
import random
import time
import ConfigSpace as CS
import ConfigSpace.hyperparameters as CSH
from hpbandster.core.worker import Worker
import logging
logging.basicConfig(level=logging.DEBUG)

class skWorker(Worker):
    def __init__(self, **kwargs):
            super().__init__(**kwargs)

            train = pd.read_csv("mnist_train.csv")
            #test = pd.read_csv("mnist_test.csv")

            #train = trainOrg.loc[0:1000,:]
            #test = testOrg.loc[0:1000,:]

            self.y = train['label']
            x = train.drop(columns ='label')


            #x = x/255.0
            #test = test /255.0
            self.scale_x = scale(x)
            #self.xtrain, self.xtest, self.ytrain, self.ytest = train_test_split(scale_x, y, random_state = 10)


    def compute(self, config, budget, working_directory, *args, **kwargs):
            

            #train = pd.read_csv("mnist_train.csv")
            #self.y = train['label']
            #x = train.drop(columns ='label')

            #self.scale_x = scale(x)

            #import IPython; IPython.embed()
            #x = x/255.0
            # ------------ my stuff
            fold = 3
            count = 0
            accuracy = []
            sec = 0
            #clist = []
            #glist = []
            #while i < len(gamma):
                #j = 0
                #while j < len(c):
            count = 0
            while count < fold:
                xtrain, xtest, ytrain, ytest = train_test_split(self.scale_x, self.y, random_state = int(random.uniform(0,1000)))
                trainTheX = int(len(ytrain) * budget)
                xtrain = xtrain[0:trainTheX, ]
                ytrain = ytrain[0:trainTheX, ]
                start = time.process_time()
                model = SVC(kernel="rbf", C = config['c'], gamma = config['g'])
                model.fit(xtrain, ytrain)
                ypred = model.predict(xtest)
                end = time.process_time()
                accuracy.append(metrics.accuracy_score(y_true = ytest, y_pred=ypred))
                sec = (int(end-start))
                #append(c[j])
                #glist.append(gamma[i])
                count += 1
                #j+= 1
                #i+= 1
            d = {'Accuracy': accuracy, 'Seconds': sec, 'C':config['c'], 'Gamma': config['g']}
            df = pd.DataFrame(d)

            #df.to_csv('performance.csv',sep=' ', index = False, header = False)

            #def bestParamdf():
                #a=df.loc[df['Accuracy'].idxmax()]
                #return (a[2], a[3])
            #c, g = bestParamdf()
            #add = 'C ' + str(c) + ' Gamma ' + str(g) + '\n'
            #fs = open('performance.csv', 'a')
            #fs.write(add)
            #fs.close()
            
            #return ({
            #        'loss': float(1- df.loc[df['Accuracy'].idxmax()]['Accuracy']), # remember: HpBandSter always minimizes!
            #        'info': {       'test accuracy':  df.loc[df['Accuracy'].idxmax()],
            #                        'c' : config['c'], 
            #                        'gamma' : config['g'],
            #                        'sec': sec}
            #})
            return ({
                    'loss': 1- float(df.loc[df['Accuracy'].idxmax()]['Accuracy']), # remember: HpBandSter always minimizes!
                    'info': {       'test accuracy':  float(df.loc[df['Accuracy'].idxmax()]['Accuracy']),
                                    'c' : config['c'],
                                    'gamma' : config['g'],
                                    'sec': sec}
            })
    @staticmethod
    def get_configspace():
            
            cs = CS.ConfigurationSpace()

            #----------- my stuff -----------
            kernel_type = CSH.CategoricalHyperparameter(
                    name = 'kernel_type', choices = ['rbf'])
            c = CSH.CategoricalHyperparameter('c', choices=[1, 5, 10])
            gamma = CSH.CategoricalHyperparameter('g', choices=[1e-2, 1e-3, 1e-4])
            cs.add_hyperparameters([c,gamma])

            return cs




if __name__ == "__main__":
    worker = skWorker(run_id='0')
    cs = worker.get_configspace()

    config = cs.sample_configuration().get_dictionary()
    print(config)
    res = worker.compute(config=config, budget=1, working_directory='.')
    print(res)






