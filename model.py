from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import recall_score, accuracy_score, f1_score, classification_report
from sklearn.preprocessing import StandardScaler

class CreditRiskModel:
    def __init__(self, n_features_to_select=15, n_components=10):
        self.scaler = StandardScaler()
        self.model = SVC(kernel='rbf', C=100.0, gamma='auto')
        self.accuracy_score=0
        self.recall_score=0
        self.classification_report = 0
        self.f1score=0

        self.cols_to_scale = [
            'LIMIT_BAL', 'AGE',
            'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6',
            'BILL_AMT1', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3',
            'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6'
        ]

    def fit(self, X, y):
        # Scaling
        X_scaled = X.copy()
        X_scaled[self.cols_to_scale] = self.scaler.fit_transform(X[self.cols_to_scale])


        self.model.fit(X_scaled, y)

    def predict(self, X):
        # Same transformation as during training
        X_scaled = X.copy()
        X_scaled[self.cols_to_scale] = self.scaler.transform(X[self.cols_to_scale])

        #X_cudf = cudf.DataFrame(X_scaled)
        return self.model.predict(X_scaled)

    def computeScore(self,X, y):
        y_pred = self.predict(X)
        self.accuracy_score = accuracy_score(y, y_pred)
        self.recall_score = recall_score(y, y_pred)
        self.f1score = f1_score(y, y_pred)
        self.classification_report = classification_report(y, y_pred)
        