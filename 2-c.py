q2 = pd.read_csv('q2.csv')
y = q2.values

summention = np.dot(np.reshape(y[:, 2], (100, 5)).sum(axis = 1), np.reshape(y[:, 2], (100, 5)).sum(axis = 1))
def pos3(sigma):
    return np.exp(summention*sigma/(2*(5*sigma + 1))) / (sigma*(sigma*5 + 1)**50)

np.random.seed(1234)
samples = [1]
for i in range(10000):
    u = np.random.uniform()
    propose = samples[-1] + np.random.normal(scale = 1)
    prob = min(1, pos3(propose)/pos3(samples[-1]))
    
    if prob < u:
        samples.append(samples[-1])
    else:
        samples.append(propose)

plt.figure(figsize = (10, 8))
plt.title("trace plot")
plt.plot(samples)
plt.show()

