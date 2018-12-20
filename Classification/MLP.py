#----------------MLP Classifier-------
import keras

def mlp(x_train, x_test,y_train, y_test):
    neuralNetwork(x_train, x_test,y_train, y_test)
    evaluation(x_test,y_test)

def neuralNetwork(x_train, x_test,y_train, y_test):
    model = Sequential()
    #Architeture
    model.add(Dense(12, input_dim=5, activation='softmax'))
    model.add(Dense(9, activation='softmax'))
    #Compilation
    #'categorical_crossentropy'
    #‘softmax’
    model.compile(optimizer='sgd', loss='categorical_crossentropy',metrics=['accuracy'])
    #Fiting
    history = model.fit(x_train, y_train, batch_size=10, epochs=100)


def evaluation(x_test,y_test):
    loss, accuracy = model.evaluate(x_test, y_test)
    #Insert other metrics soon