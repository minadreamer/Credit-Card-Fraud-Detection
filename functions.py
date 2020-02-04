# Print scores and confusion_matrix
# creates heatmap 
from sklearn.metrics import confusion_matrix
import numpy as np
from sklearn.metrics import precision_score, recall_score,confusion_matrix, classification_report, accuracy_score, f1_score  # Skearns Metrics
import matplotlib.pyplot as plt
import seaborn as sns

def scores(y_val,prediction):
    cm = confusion_matrix(y_val, prediction)
    recall = np.diag(cm) / np.sum(cm, axis = 1)
    precision = np.diag(cm) / np.sum(cm, axis = 0)
    
    print ('Recall:', recall)
    print ('Precision:', precision)
    print ('\n clasification report:\n', classification_report(y_val,prediction))
    print ('\n confussion matrix:\n',confusion_matrix(y_val, prediction))
    print('\n Accuracy Percentage  is : {}%'.format(accuracy_score(y_val,prediction) * 100))
    
    fig, (ax1) = plt.subplots(ncols=1, figsize=(5,5))
    sns.heatmap(cm, 
            xticklabels=['Not Fraud', 'Fraud'],
            yticklabels=['Not Fraud', 'Fraud'],
            annot=True,ax=ax1,
            linewidths= 0.5, cmap='PuRd')
    plt.title('Confusion Matrix', fontsize=14)
    plt.show()
    
    
# Print metrics
def print_metrics(labels, preds):
    print('Precision Score: {}'.format(precision_score(labels, preds)))
    print('Recall Score: {}'.format(recall_score(labels, preds)))
    print('Accuracy Score: {}'.format(accuracy_score(labels, preds)))
    print('F1 Score: {}'.format(f1_score(labels, preds)))
    
# print_metrics(y_val, test_preds)
