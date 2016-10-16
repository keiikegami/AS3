def pos4(sigma, i):
    return np.exp(-np.dot(theta_sample[:, i], theta_sample[:, i])/(2*sigma))/(sigma*(2*np.pi*sigma)**50)

np.random.seed(1234)

sigma_sample = [10]
theta_sample = np.ones((len(y), 10000))

for i in range(10000):
    
    if i != 0:
        u = np.random.uniform()
        propose = sigma_sample[-1] + np.random.normal(scale = 1)
        prob = min(1, pos4(propose, i)/pos4(sigma_sample[-1], i))

        if prob < u:
            sigma_sample.append(sigma_sample[-1])
        else:
            sigma_sample.append(propose)
    
        for j in range(100):
            theta_sample[j, i] = np.random.normal(loc = sigma_sample[-1]*sum(y[j*5:j*5+5, 2])/(5*sigma_sample[-1] + 1), scale = np.sqrt(sigma_sample[-1]/(5*sigma_sample[-1] + 1)))

    else:
        for j in range(100):
            theta_sample[j, i] = np.random.normal(loc = sigma_sample[-1]*sum(y[j*5:j*5+5, 2])/(5*sigma_sample[-1] + 1), scale = np.sqrt(sigma_sample[-1]/(5*sigma_sample[-1] + 1)))

# plot sigma
plt.figure(figsize = (10, 8))
plt.title("sigma trace plot")
plt.plot(sigma_sample)
plt.xlim((0, 10000))
plt.show()


# plot first 3 thetas
for i in range(3):
    plt.figure(figsize = (10, 8))
    plt.title("theta_1 trace plot")
    plt.plot(theta_sample[i, :])
    plt.xlim((0, 10000))
    plt.show()