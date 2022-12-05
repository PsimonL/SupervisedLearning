import numpy as np

rand_a = np.random.rand(2, 5)
print(rand_a)
print()

rand_b = np.random.rand(1, 5) * 100
print(rand_b)
print()

rand_c = np.vstack((rand_a, rand_b))
print(rand_c)
print()

rand_c = np.hstack((rand_a, np.random.rand(2, 1)))
print(rand_c)
print()

X = rand_c[:, 2]
print(X)
print()


a = 3
b = 8
y = a * X + b
print(y)
print()

X = np.random.randint(low=0, high=10, size=10)
print(X)
print()

X = X * 10
print(X)
print()

idx = np.random.choice(X.shape[0], size=3, replace=False)
print(X)
print(idx)
print(X[idx])












# From Udemy course. No need to do it myself.
df = pd.read_csv(r"housing.data",
                   sep="" +"", engine="python", header=None,
                   names=["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS",
        "RAD", "TAX", "PTRATIO", "B", "LSTAT", "MEDV"])

X = df.loc[:, "LSTAT"].values.reshape(-1, 1)
y = df["MEDV"].values

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

ransac = RANSAC1(max_iters_k=100, treshold=20, min_acceptable_inliers=100)

ransac.fit(X, y, show_partial_results=True)

X_train, X_test, y_train, y_test = train_test_split(X[ransac.inlier_mask],
                                                    y[ransac.inlier_mask],
                                                    test_size=0.3)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

line_X = np.arange(X.min(), X.max())[:, np.newaxis]
line_y = ransac.best_model[0] * line_X + ransac.best_model[1]

plt.figure(figsize=(7, 5))
plt.scatter(X[ransac.inlier_mask], y[ransac.inlier_mask], color="green",
            marker=""."", label="Inliers")
plt.scatter(X[~ransac.inlier_mask], y[~ransac.inlier_mask], color="red",
            marker=""."", label="Outliers")
plt.plot(line_X, line_y, color="blue", linewidth=2, label="RANSAC")
plt.plot(X_test, y_pred, color="red", label="Linear regression")

plt.legend(loc="lower right")
plt.xlabel("Input")
plt.ylabel("Response")
plt.show()